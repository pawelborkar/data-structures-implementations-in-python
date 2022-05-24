from queue_interface import QueueInterface, T
from typing import Generic, Optional
from __future__ import annotations


class LinkedQueue(QueueInterface):

    def __init__(self) -> None:
        self._initialize()
        

    def enqueue(self, value) -> None:
        new_node = Node[T](value)

        if self.empty:
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1


    def peek(self) -> T:
        if self.empty:
            raise EmptyQueueException()
        return self._head.value


    def dequeue(self) -> T:
        if self.empty:
            raise EmptyQueueException()

        item = self.peek()
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._size -= 1
        return item
    

    def clear(self) -> None:
        self._initialize()
        
    
    def _initialize(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    
    
    @property
    def empty(self) -> bool:
        return self._size == 0
    
    
    def __bool__(self) -> bool:
        return self._size != 0
    
    
    def __len__(self) -> int:
        return self._size
    
    
    def __iter__(self):
        self._current = self._head
        return self
    
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            item = self._current.value
            self._current = self._current.next
            return item



class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self._value: T = value
        self._next: Optional[Node] = None

    @property
    def value(self) -> T:
        return self._value

    @property
    def next(self) -> Node:
        return self._next
    
    @value.setter
    def value(self, value: T) -> None:
        self.value = value

    @next.setter
    def next(self, next: Optional[Node]) -> None:
        self._next = next
        
        
        
class EmptyQueueException(Exception):
    def __init__(
        self,
        message="Attempted to retrieve value from an empty queue"
    ) -> None:
        super().__init__(message)