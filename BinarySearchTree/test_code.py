from binary_search_tree import BinarySearchTree




def print_tree_information(bst: 'BinarySearchTree'):

    print()

    print('Tree height:', bst.get_height())
    print('Tree size:', bst.get_size())

    print('\nLevel Order Traversal:')
    print(bst.level_order_traversal())

    print('\nInorder Traversal:')
    print(bst.inorder_traversal())

    print('\nPreorder Traversal:')
    print(bst.preorder_traversal())

    print('\nPostorder Traversal:')
    print(bst.postorder_traversal())
    




def main():

    bst = BinarySearchTree[int]()

    print('\n\nFIRST BST:')
    print('----------------------------------------------------')

    arr1 = [5, 1, 0, 4, 3, 6, 8, 7, 9]

    for i in arr1:
        bst.insert(i)

    print(bst.height)

    print_tree_information(bst)
    
    
    print('\n\n***** After removing 4, 7, 8, and 5...\n')

    bst.delete(4)
    bst.delete(7)
    bst.delete(8)
    bst.delete(5)

    print_tree_information(bst)
    



    bst.clear()

    print('\n\nSECOND BST:')
    print('----------------------------------------------------')

    arr2 = [7, 6, 8, 4, 10, 20, 1, 16, 12, 11, 15, 3, 2]

    for i in arr2:
        bst.insert(i)

    print_tree_information(bst)


    print('\n\n***** After removing 7, and 8...\n')
    
    bst.delete(7)
    bst.delete(8)

    print_tree_information(bst)





if __name__ == "__main__":
    main()