from typing import TypeVar, Generic, List

T = TypeVar('T')


class Heap(Generic[T]):

    def __init__(self, is_min_heap: bool) -> None:
        self._arr = []
        self._is_min = is_min_heap

    def insert(self, value: T) -> None:
        self._arr.append(value)

        if self.is_empty():
            return

        size = self.size - 1
        for i in range(size // 2 - 1, -1, -1):
            self.__heapify(i)

    def remove(self, value: T) -> bool:
        pass

    def contains(self, value: T) -> bool:
        return value in self._arr
    
    def to_list(self) -> List[T]:
        return self._arr

    @property
    def top(self) -> T:
        return self._arr[0]

    @property
    def size(self) -> int:
        return len(self._arr)

    @property
    def empty(self) -> bool:
        return self.size == 0

    def __heapify(self, idx: int) -> None:
        target = idx  # set the current index as target index
        lidx = 2 * idx + 1  # get the left child's index
        ridx = 2 * idx + 2  # get the right child's index

        lchild = self._arr[lidx]  # left child
        rchild = self._arr[ridx]  # right child

        # if the heap is min heap
        if self._is_min:
            # find the minimum element
            if lchild < self._arr[target]:
                target = lidx
            if rchild < self._arr[target]:
                target = ridx
        else:
            # find the maximum element
            if lchild > self._arr[target]:
                target = lidx
            if rchild > self._arr[target]:
                target = ridx

        # swap the elements at target and current index    
        temp = self._arr[idx]
        self._arr[idx] = self._arr[target]
        self._arr[target] = temp
