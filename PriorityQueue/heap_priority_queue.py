from __future__ import annotations

from typing import List
from priority_queue import T, P, PriorityQueue


class HPriorityQueue(PriorityQueue):

    def __init__(self, is_min: bool) -> None:
        self._arr: List[self.PNode] = list()
        self._is_min: bool = is_min

    def enqueue(self, val: T, prio: P) -> None:
        new_node = self.PNode(val, prio)
        self._arr.append(new_node)

        if self.size == 1:
            return

        size = self.size - 1
        for i in range(size // 2 - 1, -1, -1):
            self._heapify(i)

    def dequeue(self) -> T:
        ret_val = self.peek()
        return ret_val

    def peek(self) -> T:
        return self._arr[0].val

    def clear(self) -> T:
        self._arr.clear()

    @property
    def size(self) -> int:
        return len(self._arr)

    @property
    def empty(self) -> bool:
        return self.size == 0

    def _heapify(self, idx: int) -> None:
        target_idx = idx
        lidx = idx * 2 + 1
        ridx = idx * 2 + 2

        lchild = self._arr[lidx]
        rchild = self._arr[ridx]

        if self._is_min:
            if lchild < self._arr[target_idx]:
                target_idx = lidx
            if rchild < self._arr[target_idx]:
                target_idx = ridx
        else:
            if lchild > self._arr[target_idx]:
                target_idx = lidx
            if rchild > self._arr[target_idx]:
                target_idx = ridx
        self._arr[idx], self._arr[target_idx] = self._arr[target_idx], self._arr[idx]

    class PNode:

        def __init__(self, val: T, priority: P) -> None:
            self._val = val
            self._priority = priority

        @property
        def priority(self) -> P:
            return self._priority

        @property
        def val(self) -> T:
            return self._val

        def __lt__(self, other):
            self.priority < other.priority

        def __eq__(self, other):
            self.priority < other.priority
 