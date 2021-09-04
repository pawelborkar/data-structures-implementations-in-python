from stack import LinkedStack, ArrayStack


if __name__ == '__main__':
    myStack = LinkedStack()
    #myStack = ArrayStack()

    passed = True
    print("Testing push() and pop()...")
    for i in range(1, 11):
        myStack.push(i)

    for i in range(1, 5):
        k = 11 - i
        received = myStack.pop()
        if received != k:
            passed = False
            print("\tThe returned number should be ", k, "instead of ", received)

    if passed:
        print("\tPASSED")

    print("Testing getSize()...")
    size = myStack.get_size()
    if size != 6:
        passed = False
        print("\tthe size should be 6 instead of ", size)

    if passed:
        print("\tPASSED")

    print("Testing peek()...")
    peek = myStack.peek()
    if peek != 6:
        passed = False
        print("Should be 6 instead of ", peek)
    myStack.push(40)
    peek = myStack.peek()
    if peek != 40:
        passed = False
        print("Should be 40 instead of ", peek)

    if passed:
        print("\tPASSED")

    print(">>>>>>>>>>>> An exception should be thrown!!!")
    end = myStack.get_size()
    for i in range (1, end + 1):
        myStack.pop()
    myStack.pop()