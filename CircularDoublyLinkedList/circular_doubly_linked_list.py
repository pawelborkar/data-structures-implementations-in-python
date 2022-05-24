from typing import Generic, TypeVar, Optional
from __future__ import annotations

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, prev_node=None, next_node=None) -> None:
        self._value: T = value
        self._prev = prev_node
        self._next = next_node

    @property
    def value(self) -> T:
        return self._value

    @property
    def next(self) -> Optional[Node]:
        return self._next

    @property
    def previous(self) -> Optional[Node]:
        return self._prev

    @value.setter
    def value(self, value: T) -> None:
        self._value = value

    @next.setter
    def next(self, next_node: Optional[Node]) -> None:
        self._next = next_node

    @previous.setter
    def previous(self, prev_node: Optional[Node]) -> None:
        self._prev = prev_node



class CircularDoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._size: int = 0
        self._head: Optional[Node] = None


    def append(self, new_value: T) -> None:
        """
        insert a new node to the end of the linked list
        """
        if self.empty:
            new_node = Node[T](new_value)
            new_node.next = new_node.previous = new_node
            self._head = new_node
        else:
            tail = self._head.previous
            new_node = Node[T](new_value, tail, self._head)
            self._head.previous = new_node
            tail.next = new_node
        self._size += 1


    def insert_at(self, new_value: T, position: int) -> None:
        pass


    def remove_at(self, position=None) -> T:
        """
        remove the node at the input position from the linked list
        @return: the value of the node removed
        """
        # if position is not specified, we remove the first Node
        if position is None:
            position = 1
        self.__check_position_validity(position, "Attempted to remove from an empty list!!!")
        to_be_removed = self.__get_node_at(position)
        to_be_removed.next.previous = to_be_removed.prev
        if position != 1:
            to_be_removed.prev.next = to_be_removed.next
        else:
            self._head = to_be_removed.next
        self._size -= 1
        return to_be_removed.value


    def remove(self, value: T) -> int:
        """
        remove the first node with the input value found
        @return: the position of the node removed,
                if the value was not found and no node was removed, return -1
        """
        current = self._head
        for i in range(self._size):
            if current.value == value:
                current.next.previous = current.previous
                current.previous.next = current.next
                return i + 1
            current = current.next
        return -1
            

    def clear(self) -> None:
        """
        clear the linked list
        """
        self._head = None
        self._size = 0


    def to_array(self) -> list:
        """
        @return: an array version of the linked list
        """
        arr = list()
        current = self._head
        for i in range(self._size):
            arr.append(current.value)
            current = current.next
        return arr


    def __get_node_at(self, position: int):
        """
        @return: the node at the input position
        """
        self.__check_position_validity(position, "Attempted to search an empty list!!!")
        current = self._head
        for i in range(1, position):
            current = current.next
        return current

    
    def __check_position_validity(self, position: int, empty_message: str) -> None:
        """
        check if the input position is in valid range. If not, throw an exception
        """
        if self.empty:
            raise Exception(empty_message)
        if position > self._size or position <= 0:
            raise Exception("Illegal Position!!!")


    @property
    def size(self) -> int:
        return self._size


    @property
    def empty(self) -> bool:
        return self._size == 0


    def __len__(self) -> int:
        return self.size


    def __bool__(self) -> bool:
        return self.size != 0


    def __iter__(self):
        self._current = self._head
        self._loop = False
        return self


    def __next__(self):
        if self._loop:
            raise StopIteration
        else:
            item = self._current.value
            self._current = self._current.next
            if self._current is self._head:
                self._loop = True
            return item
