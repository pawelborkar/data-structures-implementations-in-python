from typing import Generic, TypeVar

T = TypeVar('T')

class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.size: int = 0
        self.head: self.Node = None


    def get_size(self) -> int:
        return self.size


    def is_empty(self) -> bool:
        return self.size == 0


    def prepend(self, newValue: T) -> None:
        newNode = self.Node[T](value=newValue, next=self.head)
        if not self.is_empty():
            self.head.prev = newNode
        self.head = newNode
        self.size += 1


    def append(self, newValue: T) -> None:
        if self.is_empty():
            self.head = self.Node(newValue)
        else:
            tail = self.__get_node_at(self.size)
            newNode = self.Node[T](value=newValue, prev=tail)
            tail.next = newNode
        self.size += 1


    def insert_at(self, newvalue: T, position: int) -> None:
        if position == 1 or self.is_empty():
            self.prepend(newvalue)
        elif position == self.size + 1:
            self.append(newvalue)
        else:
            self.__check_position_validity(position, "")
            nodeBefore = self.__get_node_at(position - 1)
            temp = nodeBefore.next
            newNode = self.Node[T](newvalue, nodeBefore, temp)
            nodeBefore.next = newNode
            temp.prev = newNode
            self.size += 1


    def remove(self, position=None):
        # if position is not specified, we remove the first Node
        if position is None:
            position = 1
        self.__check_position_validity(position, "Attempted to remove from an empty list!!!")
        toBeRemoved = self.__get_node_at(position)
        toBeRemoved.next.prev = toBeRemoved.prev
        if position != 1:
            toBeRemoved.prev.next = toBeRemoved.next
        else:
            self.head = toBeRemoved.next
        self.size -= 1
        return toBeRemoved


    def reverse(self) -> None:
        # if list is empty, throw exception
        if self.is_empty():
            raise Exception("Attempted to reverse an empty list!!!")
        # if list only has 1 Node, no reverse is needed
        if self.size >= 2:
            current = self.head
            while current is not None:
                temp = current.next
                # if the next one is None, then the current Node is the last one,
                # and since we are reversing, it will become the head
                if temp is None:
                    self.head = current
                # swap the next and prev portions of the current Node
                current.next = current.prev
                current.prev = temp
                # move on to the next Node
                current = temp
            


    def clear(self) -> None:
        self.head = None
        self.size = 0

    
    def print_list(self) -> None:
        current = self.head
        while current != None:
            print(str(current.value) + " ", end='')
            current = current.next
        print('')

    
    def print_list_in_reverse(self) -> None:
        current = self.__get_node_at(self.size)
        while current != None:
            print(str(current.value) + " ", end='')
            current = current.prev
        print('')


    def __get_node_at(self, position: int):
        self.__check_position_validity(position, "Attempted to search an empty list!!!")
        current = self.head
        for i in range(1, position):
            current = current.next
        return current

    
    def __check_position_validity(self, position: int, message: str) -> None:
        if self.is_empty():
            raise Exception(message)
        if position > self.size or position <= 0:
            raise Exception("Illegal Position!!!")


    # The Node class
    class Node(Generic[T]):
        def __init__(self, value: T, prev=None, next=None) -> None:
            self.value: T = value
            self.prev: self = prev
            self.next: self = next