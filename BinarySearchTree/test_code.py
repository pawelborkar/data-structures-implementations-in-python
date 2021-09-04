from binary_search_tree import BinarySearchTree


def main():
    bst = BinarySearchTree[int]()
    print('\n\nFIRST BST:')
    arr1 = [5, 1, 0, 4, 3, 6, 8, 7, 9]
    for i in arr1:
        bst.insert(i)
    print('\nBreadth First Search:')
    bst.breadth_first_traversal()
    print('\nInorder Search:')
    bst.inorder_traversal()
    print('\nPreorder Search:')
    bst.preorder_traversal()
    print('\nPostorder Search:')
    bst.postorder_traversal()
    
    bst.clear()

    print('\n\nSECOND BST:')
    arr2 = [5, 6, 3, 4, 2]
    for i in arr2:
        bst.insert(i)
    print('\nBreadth First Search:')
    bst.breadth_first_traversal()
    print('\nInorder Search:')
    bst.inorder_traversal()
    print('\nPreorder Search:')
    bst.preorder_traversal()
    print('\nPostorder Search:')
    bst.postorder_traversal()


if __name__ == "__main__":
    main()


###### The initial BST should look like:

#                          5
#                     1        6
#                  0     4        8
#                       3        7  9
