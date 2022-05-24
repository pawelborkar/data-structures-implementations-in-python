from typing import Generic, TypeVar

T = TypeVar('T')

class QueueInterface(Generic[T]):
    
    def enqueue(self, value: T) -> None:
        raise NotImplementedError()
    
    def peek(self) -> T:
        raise NotImplementedError()
    
    def dequeue(self) -> T:
        raise NotImplementedError()
    
    def clear() -> None:
        raise NotImplementedError()