from collections import deque
from functools import wraps

def check_full(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_full():
            raise ValueError("storage full")
        return method(self, *args, **kwargs)

    return wrapper


def check_empty(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_empty():
            raise ValueError("storage empty")
        return method(self, *args, **kwargs)

    return wrapper

class BaseSequence:
    def __init__(self, initial_items: list, capacity=10):
        self.storage = initial_items
        self.capacity = capacity

# Removed @check_empty as no need to check if storage is empty when putting new value
    def put(self, element):
        if self.is_full():
            raise ValueError("storage full")
        self.storage.append(element)

    def is_empty(self):
        return not bool(self.storage)

    def is_full(self):
        return len(self.storage) == self.capacity


class Stack(BaseSequence):
    """A LIFO (last in, first out) data structure
    put - place an item on top of the stack
    pop - remove item from the top of the stack
    is_empty - return True if it's empty
    is_full - return True if it's full
    peek - get an item from the top, but do not remove it
    """

    @check_empty
    def pop(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage[-1]

class Queue(BaseSequence):
    """A FIFO (first in, first out) data structure
    """
    def get_beginning(self):
        return self.storage.pop(0)


class Dequeue(Queue, Stack):
    """
    A sequence that allows you to put and remove items from both ends
    """

    @check_full
    def put_beginning(self, element):
        self.storage.insert(0, element)

# adding tests

test_case = BaseSequence([1, 2, 3, 4, 5, 6, 7, 8, 9])
test_case.put(10)

test_case2 = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])
test_case2.put(10)
print(test_case2.storage)
test_case2.pop()
print(test_case2.storage)
test_case2.peek()

test_case3 = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])
test_case3.put(10)
test_case3.get_beginning()
print(test_case3.storage)

test_case4 = Dequeue([1, 2, 3, 4, 5, 6, 7, 8, 9])
test_case4.put_beginning(0)
print(test_case4.storage)

