import pytest
from linked_queue import LinkedQueue


def test_enqueue_dequeue_peek():
    q = LinkedQueue()
    arr = list()
    for i in range(1000):
        q.enqueue(i)
        arr.append(i)
    assert len(q) == len(arr)
    while q:
        assert q.peek() == arr[0]
        assert q.dequeue() == arr.pop(0)
        

def test_iter():
    q = LinkedQueue()
    arr = list()
    for i in range(1000):
        q.enqueue(i)
        arr.append(i)
    assert len(q) == len(arr)
    for i in q:
        assert i == arr[i]
        
        
def test_clear_and_raise():
    q = LinkedQueue()
    for i in range(100):
        q.enqueue(i)
    assert len(q) == 100
    q.clear()
    assert len(q) == 0
    with pytest.raises(Exception):
        q.dequeue()
    with pytest.raises(Exception):
        q.peek()
