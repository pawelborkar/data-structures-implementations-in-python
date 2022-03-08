from collections import deque
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data, left=None, right=None) -> None:
        self._data = data
        self._left_child = left
        self._right_child = right

    @property
    def data(self):
        return self._data

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    @data.setter
    def data(self, data):
        self._data = data

    @left_child.setter
    def left_child(self, left_child):
        self._left_child = left_child

    @right_child.setter
    def right_child(self, right_child):
        self._right_child = right_child


class BinarySearchTree(Generic[T]):

    def __init__(self) -> None:
        self._size = 0
        self._height = -1
        self.root = None

    def insert(self, value: T) -> None:
        """
        insert a new value to the binary search tree
        @return: whether the function call changed the tree
        """
        new_node = Node(value)

        # if the tree is empty, then the new node will be the root
        if self.empty:
            self.root = new_node
            self._height = 0
        # else, look for the appropriate location for the new node
        else:
            # if tree is not empty, then we know there's at least 1 node which is root
            # and height is at least 0, which is root's level
            current = self.root
            height = 0

            # perform the BST insert logic
            while True:
                height += 1
                parent = current

                if value > current.data:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        break

                elif value <= current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        break

            if height >= self._height:
                self._height = height
        self._size += 1

    def search(self, value: T) -> Optional[Node]:
        """
        search for a node with specific value in the tree
        @return: the node with the given value
        """
        if self.empty:
            return None

        current = self.root
        while current is not None:
            if value > current.data:
                current = current.right_child
            elif value < current.data:
                current = current.left_child
            else:
                return current
        return None

    def delete(self, value: T) -> bool:
        """
        delete the node with the desired value
        @return: whether the call changed the tree
        """
        prev_size = self._size
        self.__delete(self.root, value)
        self._height = self.__calculate_tree_height(self.root)
        if prev_size > self._size:
            return True
        return False

    def __delete(self, root: Optional[Node], value: T):
        """
        helper function for delete
        """
        if root is None:
            return None
        if value > root.data:
            root.right_child = self.__delete(root.right_child, value)
        elif value < root.data:
            root.left_child = self.__delete(root.left_child, value)
        else:
            if root.left_child is None:
                temp = root.right_child
                self._size -= 1
                return temp
            elif root.right_child is None:
                temp = root.left_child
                self._size -= 1
                return temp

            inorder_successor = self.__find_min_value_node(root.right_child)
            root.data = inorder_successor.data
            root.right_child = self.__delete(root.right_child, inorder_successor.data)
        return root

    @staticmethod
    def __find_min_value_node(root: Optional[Node]) -> Optional[Node]:
        """
        find the node with the minimum value in the subtree
        @return: the node with minimum value
        """
        current = root
        while current.left_child is not None:
            current = current.left_child
        return current

    def clear(self) -> None:
        """
        remove all nodes from the tree
        """
        self.root = None
        self._size = 0

    def level_order_traversal(self) -> List[List[T]]:
        """
        traverse the tree level by level and return the list of
        values of the nodes in the tree level by level
        """
        queue = deque()
        queue.append(self.root)
        arr = list()
        temp = list()

        while queue:
            if len(arr) == self._height + 1:
                return arr
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current is not None:
                    temp.append(current.data)
                    queue.append(current.left_child)
                    queue.append(current.right_child)
                else:
                    temp.append(None)
            arr.append(temp)
            temp = list()
        return arr

    def inorder_traversal(self) -> List[T]:
        """
        Perform an inorder traversal and return the list
        of values of the nodes in the tree in inorder rule
        """
        arr = list()
        self.__inorder_traversal(self.root, arr)
        return arr

    def __inorder_traversal(self, parent: Optional[Node], arr: List[T]) -> None:
        """
        helper function for inorder traversal
        """
        if parent is None:
            return
        # inorder traverse: left -> parent -> right
        self.__inorder_traversal(parent.left_child, arr)
        arr.append(parent.data)
        self.__inorder_traversal(parent.right_child, arr)

    def preorder_traversal(self) -> List[T]:
        """
        Perform a preorder traversal and return the list of
        values of the nodes in the tree in preorder rule
        """
        arr = list()
        self.__preorder_traversal(self.root, arr)
        return arr

    def __preorder_traversal(self, parent: Optional[Node], arr: List[T]) -> None:
        """
        helper function for preorder traversal
        """
        if parent is None:
            return
        # preorder traverse: parent -> left -> right
        arr.append(parent.data)
        self.__preorder_traversal(parent.left_child, arr)
        self.__preorder_traversal(parent.right_child, arr)

    def postorder_traversal(self) -> List[T]:
        """
        Perform a postorder traversal and return the list of
        values of the nodes in the trees in postorder rule
        """
        arr = list()
        self.__postorder_traversal(self.root, arr)
        return arr

    def __postorder_traversal(self, parent: Optional[Node], arr: List[T]) -> None:
        """
        helper function for post order traversal
        """
        if parent is None:
            return
        # postorder traverse: left -> right -> root
        self.__postorder_traversal(parent.left_child, arr)
        self.__postorder_traversal(parent.right_child, arr)
        arr.append(parent.data)

    def __calculate_tree_height(self, root: Optional[Node]) -> int:
        """
        re-calculate the height for the tree
        """
        if root is None:
            return -1
        left_height = self.__calculate_tree_height(root.left_child)
        right_height = self.__calculate_tree_height(root.right_child)
        return max(left_height, right_height) + 1

    @property
    def height(self) -> int:
        return self._height

    @property
    def empty(self) -> bool:
        return self._size == 0

    @property
    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self.size

    def __bool__(self) -> bool:
        return self.size != 0
