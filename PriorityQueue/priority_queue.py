from typing import Generic, TypeVar

T = TypeVar('T')
P = TypeVar('P')

class PriorityQueue(Generic[T, P]):
    
    def enqueue(self, val: T, priority: P) -> None:
        raise NotImplementedError()
    
    def dequeue(self) -> T:
        raise NotImplementedError()
    
    def peek(self) -> T:
        raise NotImplementedError()
    
    def clear(self) -> None:
        raise NotImplementedError()
    
    @property
    def empty(self) -> bool:
        raise NotImplementedError()
    
    @property
    def size(self) -> int:
        raise NotImplementedError()