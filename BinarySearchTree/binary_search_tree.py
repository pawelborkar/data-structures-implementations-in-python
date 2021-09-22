from collections import deque
from typing import Generic, TypeVar

T = TypeVar('T')


class BinarySearchTree(Generic[T]):

    def __init__(self) -> None:
        self.size = 0
        self.height = -1
        self.root = None
        

        
    

    def insert(self, value: T) -> bool:
        '''
        insert a new value to the binary search tree
        @return: whether the function call changed the tree
        '''
        new_node = self.Node(value)

        # if the tree is empty, then the new node will be the root
        if self.is_empty():
            self.root = new_node
            self.height = 0

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

                elif value < current.data:

                    current = current.left_child

                    if current is None:
                        parent.left_child = new_node
                        break

                # BST does not allow duplicates
                else:
                    return False

            if height >= self.height:
                self.height = height

        self.size += 1

        return True





    def search(self, value: T) -> 'Node':
        '''
        search for a node with specific value in the tree
        @return: the node with the given value
        '''
        if self.is_empty():
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
        '''
        delete the node with the desired value
        @return: whether the call changed the tree
        '''
        prev_size = self.size
        self.__delete(self.root, value)

        self.height = self.__calculate_tree_height(self.root)

        if prev_size > self.size:
            return True
        
        return False


    def __delete(self, root: 'Node', value: T):
        '''
        helper function for delete
        '''
        if root is None:
            return None

        if value > root.data:
            root.right_child = self.__delete(root.right_child, value)

        elif value < root.data:
            root.left_child = self.__delete(root.left_child, value)

        else:

            if root.left_child is None:
                temp = root.right_child
                self.size -= 1
                return temp

            elif root.right_child is None:
                temp = root.left_child
                self.size -= 1
                return temp

            inorder_successor = self.__find_min_value_node(root.right_child)

            root.data = inorder_successor.data

            root.right_child = self.__delete(root.right_child, inorder_successor.data)

        return root





    def __find_min_value_node(self, root: 'Node') -> 'Node':
        '''
        find the node with the minimum value in the subtree
        @return: the node with minimum value
        '''
        current = root

        while current.left_child is not None:
            current = current.left_child

        return current





    def get_size(self) -> int:
        '''
        return the size of the tree
        '''
        return self.size





    def get_height(self) -> int:
        '''
        return the height of the tree
        '''
        return self.height

    



    def is_empty(self) -> bool:
        '''
        return whether the tree is empty
        '''
        return self.size == 0

    



    def clear(self) -> None:
        '''
        delete every nodes in the tree
        '''
        self.root = None
        self.size = 0





    def level_order_traversal(self) -> list[list[T]]:
        '''
        traverse the tree level by level and return the list of
        values of the nodes in the tree level by level
        '''
        queue = deque()
        queue.append(self.root)

        arr = list()
        temp = list()

        while queue:
            
            if len(arr) == self.height + 1:
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





    def inorder_traversal(self) -> list[T]:
        '''
        Perform an inorder traversal and return the list
        of values of the nodes in the tree in inorder rule
        '''
        arr = list()
        self.__inorder_traversal(self.root, arr)
        return arr


    def __inorder_traversal(self, parent: 'Node', arr: list[T]) -> None:
        '''
        helper function for inorder traversal
        '''
        if parent is None:
            return

        # inorder traverse: left -> parent -> right

        self.__inorder_traversal(parent.left_child, arr)
        arr.append(parent.data)
        self.__inorder_traversal(parent.right_child, arr)

    



    def preorder_traversal(self) -> list[T]:
        '''
        Perform a preorder traversal and return the list of
        values of the nodes in the tree in preorder rule
        '''
        arr = list()
        self.__preorder_traversal(self.root, arr)
        return arr


    def __preorder_traversal(self, parent: 'Node', arr: list[T]) -> None:
        '''
        helper function for preorder traversal
        '''
        if parent is None:
            return

        # preorder traverse: parent -> left -> right
        arr.append(parent.data)
        self.__preorder_traversal(parent.left_child, arr)
        self.__preorder_traversal(parent.right_child, arr)





    def postorder_traversal(self) -> list[T]:
        '''
        Perform a postorder traversal and return the list of
        values of the nodes in the trees in postorder rule
        '''
        arr = list()
        self.__postorder_travelsal(self.root, arr)
        return arr

    def __postorder_travelsal(self, parent: 'Node', arr: list[T]) -> None:
        '''
        helper function for post order traversal
        '''
        if parent is None:
            return

        # postorder traverse: left -> right -> root

        self.__postorder_travelsal(parent.left_child, arr)
        self.__postorder_travelsal(parent.right_child, arr)
        arr.append(parent.data)





    def __calculate_tree_height(self, root: 'Node') -> int:
        '''
        re-calculate the height for the tree
        '''
        if root is None:
            return -1

        left_height = self.__calculate_tree_height(root.left_child)
        right_height = self.__calculate_tree_height(root.right_child)

        return max(left_height, right_height) + 1





    #####################################
    ############ NODE class #############
    class Node(Generic[T]):

        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left_child = left
            self.right_child = right