import pytest
from linked_priority_queue import LinkedPriorityQueue
from heap_priority_queue import HeapPriorityQueue
from priority_queue import PriorityQueue


def test_linked_pqueue():
    __test(LinkedPriorityQueue())


def test_heap_pqueue():
    pass


def __test(priority_queue: PriorityQueue):
    vals = [4, 5, 6, 7, 2, 1]
    prio = [0, 1, 2, 3, 4, 5] 

    for i in range(len(vals)):
        priority_queue.enqueue(vals[i], prio[i])
        assert len(priority_queue) == i + 1
    # output should be 4 5 6 7 2 1
    i = 0
    while priority_queue:
        assert vals[i] == priority_queue.dequeue()
        i += 1

    for i in range(len(vals)):
        priority_queue.enqueue(vals[len(vals) - i - 1], prio[i])
    i = 0
    arr = [1, 2, 7, 6, 5, 4]
    # output should be 1 2 7 6 5 4
    while not priority_queue.empty:
        assert priority_queue.dequeue() == arr[i]
        i += 1

    for i in range(len(vals)):
        priority_queue.enqueue(vals[i], vals[i])
    i = 0
    arr = sorted(vals)
    # output should be 1 2 4 5 6 7
    while not priority_queue.empty:
        assert priority_queue.dequeue() == arr[i]
        i += 1

    # output should be 4, 6
    priority_queue.enqueue(4, 0)
    priority_queue.enqueue(5, 2)
    priority_queue.enqueue(6, 1)
    assert priority_queue.dequeue() == 4
    assert priority_queue.dequeue() == 6

    priority_queue.clear()
    assert priority_queue.empty
    assert len(priority_queue) == 0 and priority_queue.size == 0
    with pytest.raises(Exception):
        priority_queue.dequeue()
    with pytest.raises(Exception):
        priority_queue.peek()
    
    priority_queue.enqueue(4, 3)
    priority_queue.enqueue(3, 3)
    priority_queue.enqueue(2, 3)
    priority_queue.enqueue(1, 3)
    priority_queue.enqueue(6, 4)
    priority_queue.enqueue(5, 4)
    # output should be 1 2 3 4 5 6
    for i in [1, 2, 3, 4, 5, 6]:
        assert priority_queue.dequeue() == i
