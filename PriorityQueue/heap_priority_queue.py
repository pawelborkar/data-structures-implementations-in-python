from typing import TypeVar, Generic
import heapq
from priority_queue import PriorityQueue, T

# CAN'T USE ON OBJECT
class HeapPriorityQueue(PriorityQueue):

    def __init__(self) -> None:
        self.reset()

    
    def is_empty(self) -> bool:
        return self._size == 0

    
    def enqueue(self, item: T, priority: float) -> None:
        self._size += 1
        heapq.heappush(self.elements, (priority, item))
    

    def dequeue(self) -> T:
        self._size -= 1
        return heapq.heappop(self.elements)[1]


    def get_size(self) -> int:
        return self._size


    def reset(self) -> None:
        self._size = 0
        self.elements: list[tuple[float, T]] = []