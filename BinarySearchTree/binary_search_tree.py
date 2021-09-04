from typing import Generic, TypeVar

T = TypeVar('T')


class BinarySearchTree(Generic[T]):

    def __init__(self) -> None:
        self.size = 0
        self.height = None
        self.root = None
        
    

    def insert(self, value):
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
                    raise Exception("Duplicate found: " + str(value) + " !!!")
            if height >= self.height:
                self.height = height + 1
        self.size += 1




    def search(self, value):
        if self.is_empty():
            raise Exception("Attempted to search an empty tree!!!")
        current = self.root
        while current is not None:
            if value > current.data:
                current = current.right_child
            elif value < current.data:
                current = current.left_child
            else:
                return current
        return None



    def breadth_first_traversal(self):
        if self.is_empty():
            raise Exception("Attempted to traverse an empty tree!!!")
        for i in range (self.height):
            self.__get_current_level(self.root, i)
        


    def preorder_traversal(self):
        self.__preorder_traversal(self.root)


    def postorder_traversal(self):
        self.__postorder_travelsal(self.root)


    def inorder_traversal(self):
        self.__inorder_traversal(self.root)


    def delete(self, value):
        pass


    def get_size(self):
        return self.size


    def get_height(self):
        return self.height

    
    def is_empty(self):
        return self.size == 0

    
    def clear(self):
        self.root = None
        self.size = 0


    def __get_current_level(self, parent, level):
        if parent is None:
            return
        if level == 0:
            print(parent.data, end='  ')
        else:
            self.__get_current_level(parent.left_child, level - 1)
            self.__get_current_level(parent.right_child, level - 1)
        
    
    # inorder: left -> parent -> right
    def __inorder_traversal(self, parent):
        if parent is None:
            return
        # use recursion to print the left child first
        self.__inorder_traversal(parent.left_child)
        print(parent.data, end='  ')
        self.__inorder_traversal(parent.right_child)

    
    # preorder: parent -> left -> right
    def __preorder_traversal(self, parent):
        if parent is None:
            return
        print(parent.data, end='  ')
        self.__preorder_traversal(parent.left_child)
        self.__preorder_traversal(parent.right_child)


    # postorder: left -> right -> root
    def __postorder_travelsal(self, parent):
        if parent is None:
            return
        self.__postorder_travelsal(parent.left_child)
        self.__postorder_travelsal(parent.right_child)
        print(parent.data, end='  ')




    #####################################
    ############ NODE class #############
    class Node(Generic[T]):
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left_child = left
            self.right_child = right