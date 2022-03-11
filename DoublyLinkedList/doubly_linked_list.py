from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class IndexOutOfRangeException(Exception):
    def __init__(self) -> None:
        super().__init__("Index our of range!")


class Node(Generic[T]):
    def __init__(self, value: T, prev_node=None, next_node=None) -> None:
        self._value: T = value
        self._prev = prev_node
        self._next = next_node

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._prev

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, next_node):
        self._next = next_node

    @previous.setter
    def previous(self, prev_node):
        self._prev = prev_node



class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._size: int = 0
        self._head: Optional[Node] = None


    def get_size(self) -> int:
        return self._size


    def is_empty(self) -> bool:
        return self._size == 0


    def prepend(self, new_value: T) -> None:
        new_node = Node[T](value=new_value, next_node=self._head)
        if not self.is_empty():
            self._head.previous = new_node
        self._head = new_node
        self._size += 1


    def append(self, new_value: T) -> None:
        if self.is_empty():
            self._head = Node(new_value)
        else:
            tail = self.__get_node_at(self._size)
            new_node = Node[T](value=new_value, prev_node=tail)
            tail.next = new_node
        self._size += 1


    def insert_at(self, position: int, new_value: T) -> None:
        if position == 1 or self.is_empty():
            self.prepend(new_value)
        elif position == self._size + 1:
            self.append(new_value)
        else:
            self.__check_position_validity(position, "")
            node_before = self.__get_node_at(position - 1)
            temp = node_before.next
            new_node = Node[T](new_value, node_before, temp)
            node_before.next = new_node
            temp.prev = new_node
            self._size += 1
            
            
    def get(self, position: int) -> T:
        node = self.__get_node_at(position)
        return node.value    


    def remove(self, position=None) -> Optional[Node]:
        # if position is not specified, we remove the first Node
        if position is None:
            position = 1
        self.__check_position_validity(position, "Attempted to remove from an empty list!!!")
        to_be_removed = self.__get_node_at(position)
        to_be_removed.next.prev = to_be_removed.prev
        if position != 1:
            to_be_removed.prev.next = to_be_removed.next
        else:
            self._head = to_be_removed.next
        self._size -= 1
        return to_be_removed


    def reverse(self) -> None:
        # if list is empty, throw exception
        if self.is_empty():
            raise Exception("Attempted to reverse an empty list!!!")
        # if list only has 1 Node, no reverse is needed
        if self._size >= 2:
            current = self._head
            while current is not None:
                temp = current.next
                # if the next one is None, then the current Node is the last one,
                # and since we are reversing, it will become the head
                if temp is None:
                    self._head = current
                # swap the next and prev portions of the current Node
                current.next = current.prev
                current.prev = temp
                # move on to the next Node
                current = temp
            

    def clear(self) -> None:
        self._head = None
        self._size = 0

    
    def print_list(self) -> None:
        current = self._head
        while current is not None:
            print(str(current.value) + " ", end='')
            current = current.next
        print('')

    
    def print_list_in_reverse(self) -> None:
        current = self.__get_node_at(self._size)
        while current is not None:
            print(str(current.value) + " ", end='')
            current = current.prev
        print('')


    def __get_node_at(self, position: int):
        self.__check_position_validity(position, "Attempted to search an empty list!!!")
        current = self._head
        for i in range(1, position):
            current = current.next
        return current

    
    def __check_position_validity(self, position: int, message: str) -> None:
        if self.is_empty():
            raise Exception(message)
        if position > self._size or position <= 0:
            raise Exception("Illegal Position!!!")


    @property
    def size(self) -> int:
        return self._size


    @property
    def empty(self):
        return self.size == 0


    def __len__(self) -> int:
        return self.size


    def __bool__(self) -> bool:
        return self.size != 0


    def __getitem__(self, i) -> T:
        return self.get(i)


    def __iter__(self):
        self._current = self._head
        return self


    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            item = self._current.value
            self._current = self._current.next
            return item
