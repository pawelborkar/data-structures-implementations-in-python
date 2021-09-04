from typing import Generic, TypeVar

T = TypeVar('T')

class AVL(Generic[T]):
    def __init__(self) -> None:
        self.size = 0
        self.root = None


    def insert(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            root = new_node
        else:
            pass
    


    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size



    class Node(Generic[T]):
        def __init__(self, data, height=1, right=None, left=None) -> None:
            self.data = data
            self.height = height
            self.right = right
            self.left = left