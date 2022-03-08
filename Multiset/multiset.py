from typing import TypeVar, Generic

T = TypeVar('T')


class Multiset(Generic[T]):
    def __init__(self) -> None:
        self._initialize()

    def add(self, value: T, frequency=1) -> None:
        if value not in self._bag:
            item = {value: frequency}
        else:
            old_frequency = self._bag[value]
            new_frequency = old_frequency + frequency
            item = {value: new_frequency}
        self._bag.update(item)
        self._size += frequency

    def remove(self, value, frequency=1) -> None:
        if self.empty:
            raise Exception('Attempted to remove from an empty bag')
        elif value not in self._bag:
            raise Exception('Attempted to remove non-existed value')
        elif self._bag[value] < frequency:
            raise Exception('Attempted to remove more than available frequency')
        elif self._bag[value] == frequency:
            del self._bag[value]
        else:
            new_frequency = self._bag[value] - frequency
            item = {value: new_frequency}
            self._bag.update(item)
        self._size -= frequency

    def clear(self) -> None:
        self._initialize()

    def _initialize(self) -> None:
        self._bag = dict()
        self._size = 0

    def get_frequency(self, value) -> int:
        return self._bag[value]

    def contains(self, value) -> bool:
        return value in self._bag

    @property
    def empty(self) -> bool:
        return self._size == 0

    @property
    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return not self.empty
