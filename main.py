from enum import Enum
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QVBoxLayout, QPlainTextEdit


class TokenType(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EOF = "\0"
    NUMBER = "NUMBER"


class Token:
    def __init__(self, token_type, source):
        self.token_type = token_type
        self.source = source

class Lexer:
    DICTIONARY = {
        "+": TokenType.ADD,
        "-": TokenType.SUB,
        "*": TokenType.MUL,
        "/": TokenType.DIV,
        "NUMBER": TokenType.NUMBER
    }

    def __init__(self, source):
        self.tokens = []
        self.source = "5 + 5"  # for debug
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.source):
            current_char = self.peek(0)
            if current_char.isdigit():
                self.tokenize_number()
            elif current_char in self.DICTIONARY.keys():
                self.tokenize_operator()
            else:
                self.pos = self.pos + 1

        return self.tokens

    def tokenize_operator(self):
        current_char = self.peek(0)
        token_type = self.DICTIONARY[current_char]

        token = Token(token_type, current_char)
        self.tokens.append(token)
        self.next()

    def tokenize_number(self):
        buffer = ""
        current_char = self.peek(0)
        while current_char.isdigit():
            buffer = buffer + current_char
            current_char = self.next()

        token = Token(TokenType.NUMBER, buffer)
        self.tokens.append(token)


    def peek(self, relative_position):
        position = self.pos + relative_position
        if position > len(self.source):
            return "\0"
        return self.source[self.pos]


    def next(self):
        self.pos = self.pos + 1
        return self.peek(self.pos)


class Expression:
    def __init__(self):
        self.value = None # Number

    def evaluate(self):
        pass


class BinaryExpression(Expression):
    def __init__(self, operation, expression1, expression2):
        self.operation = operation
        self.expression1 = expression1
        self.expression2 = expression2

    def evaluate(self):
        if self.operation == TokenType.ADD:
            return self.expression1.evaluate() + self.expression2.evaluate()


class NumberExpression(Expression):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        return self.expression.value


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def expression(self):
        return self.add()

    def add(self):
        return self.mul()

    def mul(self):
        return self.primary()

    def primary(self):
        pass

    def match(self, token_type):
        current_token = self.peek(0)

        if current_token.type == token_type:
            self.pos = self.pos + 1
            return True
        return False

    def peek(self, relative_position):
        position = self.pos + relative_position
        if position > len(self.tokens):
            return TokenType.EOF
        return self.tokens[self.pos]


def main():
    source = "5 + 5"

    lexer = Lexer(source)
    for i in lexer.tokenize():
        print(i.token_type)
        print(i.source)

    print(TokenType.NUMBER.value)

    # UI Experimental
    app = QApplication([])
    window = QWidget()

    line_edit = QPlainTextEdit("hello world")
    line_edit.setFixedHeight(150)
    line_edit2 = QPlainTextEdit("fooo")
    line_edit2.setFixedHeight(150)
    button1 = QPushButton("Click")
    button1.clicked.connect(lambda: button_clicked(lexer, line_edit))

    layout = QVBoxLayout()
    layout.addWidget(line_edit)
    layout.addWidget(line_edit2)
    layout.addWidget(button1)

    window.setLayout(layout)
    window.setBaseSize(200, 200)
    window.show()
    app.exec()

def button_clicked(lexer, line_edit):
    for i in lexer.tokenize():
        line_edit.appendPlainText(i.source)



if __name__ == '__main__':
    main()
