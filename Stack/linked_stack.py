from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class LinkedStack(Generic[T]):

    def __init__(self) -> None:
        self._initialize()

    def push(self, item: T) -> None:
        self._size += 1
        self._initialized = True
        new = Node(item)
        new.next = self._head.next
        self._head.next = new

    def peek(self) -> T:
        if not self.initialized or self.empty:
            raise Exception("Attempted to peek an empty stack!!!")
        return self._head.next.value

    # pop the value
    def pop(self) -> T:
        if not self.initialized or self.empty:
            raise Exception("Attempted to pop an empty stack!!!")
        top_value = self.peek()
        self._head.next = self._head.next.next
        self._size -= 1

        return top_value

    def clear(self):
        self._initialize()

    def _initialize(self) -> None:
        self._initialized = False
        self._head = Node(None)
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def empty(self) -> bool:
        return self._size == 0

    @property
    def initialized(self) -> bool:
        return self._initialized

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size != 0


class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self._value = value
        self._next = None

    @property
    def value(self) -> T:
        return self._value

    @property
    def next(self) -> Optional[Optional[Node]]:
        return self._next

    @value.setter
    def value(self, value) -> None:
        self._value = value

    @next.setter
    def next(self, next_node) -> None:
        self._next = next_node
