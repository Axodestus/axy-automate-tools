import random


def main():
    print("hello world")


def binary_search(value):
    data = [x for x in range(20)]
    i = 0
    first = 0
    last = len(data) - 1
    while first <= last:


        middle = first + last // 2 - 1
        guess = data[middle]
        if guess == value:
            return middle
        if middle > value:
            last = middle - 1
        else:
            first = middle + 1
    return -1


if __name__ == '__main__':
    print(binary_search(5))