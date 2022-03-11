import pytest
from doubly_linked_list import DoublyLinkedList


def test_add():
    dll = DoublyLinkedList()
    arr = list()
    for i in range(100):
        dll.append(i)
        arr.append(i)
    for i in range(-99, 0, 1):
        dll.prepend(i)
        arr.insert(0, i)
    for i in range(0, 100, 5):
        dll.insert_at(i + 1, 1000)
        arr.insert(i, 1000)

    assert len(dll) == len(arr) == dll.size
    assert dll and not dll.empty
    
    for i in range(-99, 100, 1):
        assert dll[i] == arr[i]
    
    
def test_remove():
    pass


def test_reverse():
    pass


def test_iter():
    dll = DoublyLinkedList()
    arr = list()
    for i in range(100):
        dll.append(i)
        arr.append(i)
    for i in dll:
        assert i == arr[i]


def test_clear_and_raise():
    pass
