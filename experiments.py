import random
import sys
import os
import time



def find_smallest(data):
    smallest = data[0]
    smallest_index = 0
    for i in range(1, len(data)): 
        if data[i] < smallest:
            smallest = data[i]
            smallest_index = i
    return smallest_index


def selection_sort(data):
    new_data = []
    for i in range(len(data)):
        smallest_index = find_smallest(data)
        new_data.append(data.pop(smallest_index))
    return new_data


def binary_search(value):
    data = [x for x in range(20)]
    i = 0
    first = 0
    last = len(data) - 1
    while first <= last:
        middle = first + last // 2 - 1 # this is main line of algo
        guess = data[middle]
        if guess == value:
            return middle
        if middle > value:
            last = middle - 1
        else:
            first = middle + 1
    return -1


def main():
    print("This is experiments with some algo")
    data = [random.randint(1, 100) for x in range(1, 100)]
        
    print(binary_search(5))
    print(selection_sort(data))


if __name__ == '__main__':
    main()
