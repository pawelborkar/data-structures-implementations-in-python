from linked_stack import LinkedStack
from array_stack import ArrayStack



def test(my_stack):

    passed = True
    print("\nTesting push() and pop()...")

    for i in range(1, 11):
        my_stack.push(i)


    for i in range(1, 5):

        k = 11 - i
        received = my_stack.pop()

        if received != k:
            passed = False
            print("\tThe returned number should be ", k, "instead of ", received)


    if passed:
        print("\tPASSED")


    print("\nTesting getSize()...")
    size = my_stack.get_size()

    if size != 6:
        passed = False
        print("\tthe size should be 6 instead of ", size)

    if passed:
        print("\tPASSED")


    print("\nTesting peek()...")
    peek = my_stack.peek()

    if peek != 6:
        passed = False
        print("Should be 6 instead of ", peek)

    my_stack.push(40)

    peek = my_stack.peek()

    if peek != 40:
        passed = False
        print("Should be 40 instead of ", peek)


    if passed:
        print("\tPASSED")


    try:
        end = my_stack.get_size()
        for i in range (1, end + 1):
            my_stack.pop()
            
        my_stack.pop()

        print('FAILED for not throwing exception')

    except Exception as e:
        print("\nException has been thrown for popping an empty stack as excepted...")
        print('\tPASSED')





if __name__ == '__main__':

    my_stack = LinkedStack()

    print('\n\n\tTESTING LINKED STACK\n\n')
    test(my_stack)

    my_stack = ArrayStack()

    print('\n\n\n\n\n\tTESTING ARRAY STACK\n\n')
    test(my_stack)

    print('\n\n\n*** End of Test ***\n')


    