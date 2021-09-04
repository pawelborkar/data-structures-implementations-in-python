from typing import TypeVar, Generic

T = TypeVar('T')

class Multiset(Generic[T]):
    def __init__(self) -> None:
        self.reset()


    def add(self, value: T, frequency=1) -> None:
        if value not in self.bag:
            item = {value: frequency}
        else:
            old_frequency = self.bag[value]
            new_frequency = old_frequency + frequency
            item = {value: new_frequency}
        self.bag.update(item)
        self.size += frequency


    def remove(self, value, frequency=1) -> None:
        if self.is_empty():
            raise Exception('Attempted to remove from an empty bag')
        elif value not in self.bag:
            raise Exception('Attempted to remove unexisted value')
        elif self.bag[value] < frequency:
            raise Exception('Attempted to remove more than available frequency')
        elif self.bag[value] == frequency:
            del self.bag[value]
        else:
            new_frequency = self.bag[value] - frequency
            item = {value: new_frequency}
            self.bag.update(item)
        self.size -= frequency


    def reset(self):
        self.bag = dict()
        self.size = 0


    def get_frequency(self, value) -> int:
        return self.bag[value]


    def contains(self, value) -> bool:
        return value in self.bag


    def is_empty(self) -> bool:
        return self.size == 0

    
    def get_size(self) -> int:
        return self.size


    