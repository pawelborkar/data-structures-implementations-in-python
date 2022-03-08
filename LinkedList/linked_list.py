from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self._size: int = 0
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None


    def add(self, value: T, position=None) -> None:
        self.__check_position(position)
        new_node = Node[T](value)
        # if position is not specified, we add to the end of the list
        if position is None or position == self._size:
            if self.empty:
                self._head = new_node
                self._tail = new_node
            else:
                self._tail.link = new_node
                self._tail = new_node
        else:
            if position == 1:
                new_node.link = self._head
                self._head = new_node
            else:
                node_before = self.__get_node_at(position - 1)
                node_after = node_before.link
                new_node.link = node_after
                node_before.link = new_node
        self._size += 1


    def remove(self, position=None) -> T:
        self.__check_position(position)
        # if the position is not specified then we remove the first Node
        if position is None:
            position = 1
        if position > self._size or position <= 0:
            raise Exception("Illegal Position!!!")
        if position == 1:
            result = self._head.data
            temp = self._head.link
            self._head = temp
        else:
            node_before = self.__get_node_at(position - 1)
            node_to_remove = node_before.link
            result = node_to_remove.data
            node_after = node_to_remove.link
            node_before.link = node_after
        self._size -= 1
        return result


    def remove_value(self, value) -> bool:
        position = self.locate(value)
        if position == -1:
            return False
        self.remove(position)
        return True


    def remove_all_elements_with_value(self, value) -> None:
        current = self._head
        while current.link is not None:
            if current.link.data == value:
                current.link = current.link.link
            else:
                current = current.link
        if self._head.data == value:
            self._head = self._head.link



    def locate(self, value: T) -> int:
        current = self._head
        index = 1
        while current is not None:
            if current.data == value:
                return index
            index += 1
            current = current.link
        return -1


    def contains(self, value: T) -> bool:
        index = self.locate(value)
        if index == -1:
            return False
        return True


    def reverse(self) -> None:
        prev = None
        current = self._head
        while current is not None:
            temp = current.link
            current.link = prev
            prev = current
            current = temp
        self._head = prev


    def to_list(self) -> List[T]:
        array = []
        current = self._head
        while current is not None:
            array.append(current.data)
            current = current.link
        return array


    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0


    def __get_node_at(self, position):
        if self.empty:
            raise Exception("Attempted to find in an empty list!!!")
        self.__check_position(position)
        current = self._head
        for i in range(1, position):
            current = current.link
        return current


    def __check_position(self, pos: int) -> None:
        if pos is None:
            return
        if pos <= 0:
            raise Exception("Position must start from 1")
        if pos > self._size:
            raise Exception("Position exceeded the list's size")
        
        
    @property
    def count(self) -> int:
        return self._size


    @property
    def empty(self) -> bool:
        return self._size == 0
        
        
    def __len__(self) -> int:
        return self._size
    
    
    def __bool__(self) -> bool:
        return self._size != 0
    
    
    def __iter__(self):
        self._current = self._head
        return self
    
    
    def __next__(self):
        if not self._current:
            raise StopIteration
        else:
            item = self._current.data
            self._current = self._current.link
            return item
        
        
    def __str__(self) -> str:
        result = ""
        current = self._head
        while current is not None:
            result += str(current.data)
            if current is not self._tail:
                result += ", "
            current = current.link
        return result



class Node(Generic[T]):

    def __init__(self, data=None, link=None):
        self._data = data
        self._link = link

    @property
    def data(self):
        return self._data

    @property
    def link(self):
        return self._link

    @data.setter
    def data(self, data):
        self._data = data

    @link.setter
    def link(self, link):
        self._link = link
