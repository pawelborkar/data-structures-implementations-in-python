from typing import TypeVar, Generic
import heapq


T = TypeVar('T')


# CAN'T USE ON OBJECT
class HeapPriorityQueue(Generic[T]):

    def __init__(self) -> None:
        self.reset()

    
    def is_empty(self) -> bool:
        return self.size == 0

    
    def enqueue(self, item: T, priority: float) -> None:
        self.size += 1
        heapq.heappush(self.elements, (priority, item))
    

    def dequeue(self) -> T:
        self.size -= 1
        return heapq.heappop(self.elements)[1]


    def get_size(self) -> int:
        return self.size


    def reset(self) -> None:
        self.size = 0
        self.elements: list[tuple[float, T]] = []