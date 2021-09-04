from typing import Generic, TypeVar

T = TypeVar('T')


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self.size: int = 0
        self.head: self.Node = None
        self.tail: self.Node = None


    def is_empty(self) -> None:
        return self.size == 0


    def add(self, value: T, position=None) -> None:
        self.__check_position(position)
        new_node = self.Node[T](value)
        # if position is not specified, we add to the end of the list
        if position is None or position == self.size:
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.set_link(new_node)
                self.tail = new_node
        else:
            if position == 1:
                new_node.set_link(self.head)
                self.head = new_node
            else:
                nodeBefore = self.__get_node_at(position - 1)
                nodeAfter = nodeBefore.get_link()
                new_node.set_link(nodeAfter)
                nodeBefore.set_link(new_node)
        self.size += 1


    def remove(self, position=None) -> T:
        self.__check_position(position)
        # if the position is not specified then we remove the first Node
        if position is None:
            position = 1
        if position > self.size or position <= 0:
            raise Exception("Illegal Position!!!")
        if position == 1:
            result = self.head.get_data()
            temp = self.head.get_link()
            self.head = temp
        else:
            nodeBefore = self.__get_node_at(position - 1)
            nodeToRemove = nodeBefore.get_link()
            result = nodeToRemove.get_data()
            nodeAfter = nodeToRemove.get_link()
            nodeBefore.set_link(nodeAfter)
        self.size -= 1
        return result


    def remove_value(self, value) -> bool:
        position = self.locate(value)
        if position == -1:
            return False
        self.remove(position)
        return True


    def remove_all_elements_with_value(self, value) -> None:
        current = self.head
        while current.get_link() is not None:
            if current.get_link().get_data() == value:
                current.set_link(current.get_link().get_link())
            else:
                current = current.get_link()
        if self.head.get_data() == value:
            self.head = self.head.get_link()



    def locate(self, value: T) -> int:
        current = self.head
        index = 1
        while current is not None:
            if current.get_data() == value:
                return index
            index += 1
            current = current.get_link()
        return -1


    def contains(self, value: T) -> bool:
        index = self.locate(value)
        if index == -1:
            return False
        return True


    def reverse(self) -> None:
        prev = None
        current = self.head
        while current != None:
            temp = current.get_link()
            current.set_link(prev)
            prev = current
            current = temp
        self.head = prev


    def to_array(self) -> list[T]:
        array = []
        current = self.head
        while current is not None:
            array.append(current.get_data())
            current = current.get_link()
        return array


    def print_list(self) -> None:
        current = self.head
        while current != None:
            print(current.get_data())
            current = current.get_link()


    def get_size(self) -> int:
        return self.size


    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def __get_node_at(self, position):
        if self.is_empty():
            raise Exception("Attempted to find in an empty list!!!")
        self.__check_position(position)
        current = self.head
        for i in range(1, position):
            current = current.get_link()
        return current


    def __check_position(self, pos: int) -> None:
        if pos is None:
            return
        if pos <= 0:
            raise Exception("Position must start from 1")
        if pos > self.size:
            raise Exception("Position exceeded the list's size")


    class Node(Generic[T]):

        def __init__(self, data=None, link=None):
            self.data = data
            self.link = link

        def get_data(self):
            return self.data

        def get_link(self):
            return self.link

        def set_data(self, data):
            self.data = data

        def set_link(self, link):
            self.link = link
