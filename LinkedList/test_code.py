from linked_list import LinkedList

if __name__ == '__main__':
    print("TESTING LINKED LIST")

    llist = LinkedList[int]()

    for i in range(1, 6):
        llist.add(i)  # list should be 1, 2, 3, 4, 5, 6

    passed = True
    print("\nTesting size...")
    if llist.count != 5 or len(llist) != 5:
        passed = False
        print("Size should be 5 instead of ", len(llist))
    if passed:
        print("\tPASSED")

    passed = True
    print("Testing contains()...")
    for i in range(1, 6):
        if not llist.contains(i):
            print("The list should contain ", i)
            passed = False
    if passed:
        print("\tPASSED")

    passed = True
    print("Testing remove()...")
    for i in range(1, 6):
        removed = llist.remove()
        if removed != i:
            passed = False
            print("The removed value should be ", i, "instead of ", removed)
    if passed:
        print("\tPASSED")

    passed = True
    print("Testing reverse()...")
    llist.clear()
    for i in range(1, 6):
        llist.add(i)
    llist.reverse()
    for i in range(1, 6):
        removed = llist.remove()
        if removed != (6 - i):
            print("The removed value should be ", (6 - i), "instead of ", removed)
            passed = False
    if passed:
        print("\tPASSED")

    passed = True
    print('Testing remove_value()...')
    test_arr = []
    llist.clear()
    for i in range(1, 11):
        llist.add(i)
        test_arr.append(i)
    for j in range(3, 6):
        llist.remove_value(j)
        test_arr.remove(j)
    test_arr.remove(10)
    llist.remove_value(10)
    llist_arr = llist.to_list()
    for i in range(len(test_arr)):
        if test_arr[i] != llist_arr[i]:
            passed = False
            break
    if passed:
        print("\tPASSED")
        
    passed = True
    print('Testing remove_all_elements_with_value()...')
    llist.clear()
    llist.add(2)
    llist.add(1)
    llist.add(3)
    llist.add(2)
    llist.remove_all_elements_with_value(2)
    llist_arr = llist.to_list()
    test_arr = [1, 3]
    for i in range(len(test_arr)):
        if llist_arr[i] != test_arr[i]:
            passed = False
    llist.clear()
    for i in range(10):
        llist.add(1)
    llist.remove_all_elements_with_value(1)
    if llist.to_list():
        passed = False
    if passed:
        print("\tPASSED")

    


    
    
