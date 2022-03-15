from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class IndexOutOfRangeException(Exception):
    def __init__(self) -> None:
        super().__init__("Index out of range!")
        
        
class EmptyListException(Exception):
    def __init__(self) -> None:
        super().__init__("Attempted to remove or retreive data from an empty list!")


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


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self._size: int = 0
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        
        
    def append(self, value: T) -> None:
        """add a new element to the end of the list
        Args:
            value (T): the new value to be added
        """
        new_node = Node(value)
        if self.empty:
            self._head = new_node
        else:
            self._tail.link = new_node
        self._tail = new_node
        self._size += 1
        
        
    def prepend(self, value: T) -> None:
        """add a new element to the front of the list
        Args:
            value (T): the value to be added
        """
        new_node = Node(value)
        if self.empty:
            self._head = self._tail = new_node
        else:
            new_node.link = self._head
            self._head = new_node
        self._size += 1
        
        
    def insert_after(self, value: T, position: int) -> None:
        """insert a new element after a given position
        Args:
            value (T):      the value to be added
            position (int): the position to be inserted after
        """
        self.__check_position(position)
        if self.size == 0 or position == self.size - 1:
            self.append(value)
            return
        new_node = Node(value)
        current = self._head
        for _ in range(position):
            current = current.link
        new_node.link = current.link
        current.link = new_node
        self._size += 1
        
        
    def insert_before(self, value: T, position: int) -> None:
        """insert a new element before a given position
        Args:
            value (T):      the new value to be added
            position (int): the position to be inserted before
        """
        self.__check_position(position)
        if self._size == 0 or position == 0:
            self.prepend(value)
            return
        self.insert_after(value, position - 1)


    def pop_front(self) -> T:
        """remove the element at the front of the list
        Raises:
            `EmptyListException`: raised when the list is empty
        Returns:
            T: the value of the removed element
        """
        if self.empty:
            raise EmptyListException()
        ret_val = self._head.data
        self._head = self._head.link
        self._size -= 1
        return ret_val
    
    
    def pop_back(self) -> T:
        """remove the element at the end of the list
        Raises:
            `EmptyListException`: raised when the list is empty
        Returns:
            T: the value of the removed element
        """
        if self.empty:
            raise EmptyListException()
        if self.size == 1:
            return self.pop_front()
        ret_val = self._tail.data
        current = self._head
        while current.link is not self._tail:
            current = current.link
        current.link = None
        self._tail = current
        self._size -= 1
        return ret_val


    def remove_at(self, position: int) -> T:
        """remove the element at the given position
        Args:
            position (int): the position of the element to be removed
        Raises:
            `EmptyListException`: raised when the list is empty
            `IndexOutOfRangeException`: raised when the position is out of range
        Returns:
            T: the value of the removed element
        """
        if self.empty:
            raise EmptyListException()
        self.__check_position(position)
        if position == 0:
            return self.pop_front()
        prev = self._head
        current = self._head.link
        for _ in range(position):
            prev = current
            current = current.link
        ret_val = self.current.data
        prev.link = current.link
        self._size -= 1
        return ret_val


    def remove(self, value: T) -> bool:
        """remove the first occurence of the element with the given value
        Args:
            value (T): the value to be removed from the list
        Returns:
            bool: true if an element with the same value was found and removed
        """
        position = self.locate(value)
        if position == -1:
            return False
        self.remove(position)
        return True


    def remove_all(self, value: T) -> None:
        """remove all the elements with the given value
        Args:
            value (T): the value to be removed from the list
        """
        current = self._head
        while current.link is not None:
            if current.link.data == value:
                current.link = current.link.link
            else:
                current = current.link
        if self._head.data == value:
            self._head = self._head.link


    def locate(self, value: T) -> int:
        """return the index of the first occurence with the given value
        Args:
            value (T): the value to look for
        Returns:
            int: the index of the first occurence (return -1 if not found)
        """
        current = self._head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            index += 1
            current = current.link
        return -1


    def contains(self, value: T) -> bool:
        """check if the linked list contains one or more elements with the given value
        Args:
            value (T): the value to look for
        Returns:
            bool: true if the list contains at least an element with the given value
        """
        index = self.locate(value)
        if index == -1:
            return False
        return True


    def reverse(self) -> None:
        """reverse the linked list in-place
        """
        prev = None
        current = self._head
        while current is not None:
            temp = current.link
            current.link = prev
            prev = current
            current = temp
        self._head = prev


    def to_list(self) -> List[T]:
        """get an array version of the list
        Returns:
            List[T]: the array version of the linked list
        """
        array = []
        current = self._head
        while current is not None:
            array.append(current.data)
            current = current.link
        return array


    def clear(self) -> None:
        """remove all elements in the linked list
        """
        self._head = None
        self._tail = None
        self._size = 0


    def __get_node_at(self, position: int) -> Node:
        """get the node at the given position
        Args:
            position (int): the position of the node
        Returns:
            Node: the node at the given position
        """
        self.__check_position(position)
        current = self._head
        for _ in range(position):
            current = current.link
        return current


    def __check_position(self, pos: int) -> None:
        """check if a position is correct
        Args:
            pos (int): the position to be checked
        Raises:
            IndexOutOfRangeException: raised when the position is out of range
        """
        if pos < 0 or pos >= self._size:
            raise IndexOutOfRangeException()
        
        
    @property
    def size(self) -> int:
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
    
    
    def __getitem__(self, index):
        return self.__get_node_at(index).data
    
    
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
