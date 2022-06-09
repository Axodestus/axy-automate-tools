import random
import sys
import os
import time
from collections import deque

def d_algo():
    pass


def search_in_width(name): 

    # some simple data: graph
    graph = {}
    graph["you"] = ["Alice", "Bob", "Claire", "max"]
    graph["Alice"] = []
    graph["Bob"] = []
    graph["Claire"] = []
    graph["max"] = []

    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person[0] == "m":        # This is bad example to the find person
            if not person in searched:
                print(person + " [Debug] person is a mango seller")
                return True
            else:
                search_queue += graph[person]
                search_queue.append(person)
    return False


# This is basic simple algo for figure out recursion
def factorial(value):
    if value == 1:
        return 1
    return value * fact(x - 1)


def quick_sort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i < pivot]
        greater = [i for i in data[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


# There is function for selection sort.
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
        middle = first + last // 2 - 1 # this is main idea of binary search... 
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

    print("[Debug] Selection_sort")
    print(selection_sort(data))

    print("[Debug] Quick_sort")
    data = [random.randint(1, 100) for x in range(1, 100)]
    print(quick_sort(data))

    print("[Debug] Search_in_width")
    print(search_in_width("you"))


if __name__ == '__main__':
    main()
