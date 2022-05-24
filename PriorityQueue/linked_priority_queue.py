from priority_queue import PriorityQueue, T, P
from typing import Generic

class LinkedPriorityQueue(PriorityQueue):

    def __init__(self) -> None:
        self._initialize()


    def enqueue(self, val: T, priority: P) -> None:
        new_node = PriorityNode(val, priority)
        if self.empty:
            self._head = new_node
            self.tail = new_node
        else:
            if priority > self.tail.priority:
                self.tail.next = new_node
                self.tail = new_node
            elif priority <= self._head.priority:
                new_node.next = self._head
                self._head = new_node
            else:
                current = self._head
                while current.next is not None and current.next.priority < priority:
                    current = current.next
                temp = current.next
                current.next = new_node
                new_node.next = temp
        self._size += 1


    def dequeue(self) -> T:
        if self.empty:
            raise Exception('Attempted to dequeue an empty queue!!!')
        temp = self.peek()
        self._head = self._head.next
        self._size -= 1
        # if the new head is None, then the queue is empty
        if self._head is None:
            self.clear()
        return temp


    def peek(self) -> T:
        if self.empty:
            raise Exception('Attempted to peek an empty queue!!!')
        return self._head.value


    def clear(self) -> None:
        self._initialize()
        
        
    def _initialize(self):
        self._head = None
        self.tail = None
        self._size = 0
        
        
    @property
    def empty(self) -> bool:
        return self._size == 0
    
    
    @property
    def size(self) -> int:
        return self._size
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def __bool__(self) -> bool:
        return self.size != 0
    
    
    def __iter__(self):
        self._current = self._head
        
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            item = self._current.value
            self._current = self._current.next
            return item


class PriorityNode(Generic[T, P]):

    def __init__(self, value: T, priority: P, next:'PriorityNode'=None) -> None:
        self._value = value
        self._priority = priority
        self._next = next

    @property
    def value(self) -> T:
        return self._value
    
    @value.setter
    def value(self, value) -> None:
        self._value = value

    @property
    def priority(self) -> P:
        return self._priority
    
    @priority.setter
    def priority(self, priority) -> None:
        self._priority = priority

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next