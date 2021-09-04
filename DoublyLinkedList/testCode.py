from DoublyLinkedList import DoublyLinkedList

def main():
    my_list = DoublyLinkedList[int]()

    print("\n\n\tTESTING prepend()")
    print("The output DLL should be [9 8 7 6 5 4 3 2 1]")
    print("The size of the DLL should be 9\n")
    for i in range(1, 10):
        my_list.prepend(i)
    print_output(my_list)

    print("\n\n\tTESTING insert_at()")
    print("The output DLL should be [10 9 8 100 7 6 200 5 4 3 2 1 0]")
    print("The size of the DLL should be 13\n")
    my_list.insert_at(newvalue=0, position=10)
    my_list.insert_at(newvalue=10, position=1)
    my_list.insert_at(newvalue=100, position=4)
    my_list.insert_at(newvalue=200, position=7)
    print_output(my_list)

    print("\n\n\tTESTING append()")
    print("The output DLL should be [1 2 3 4 5 6 7 8 9]")
    print("The size of the DLL should be 9\n")
    my_list.clear()
    for i in range(1, 10):
        my_list.append(i)
    print_output(my_list)

    print("\n\n\tTESTING remove()")
    print("The output DLL should be [2 3 6 7 8 9]")
    print("The size of the DLL should be 6\n")
    my_list.remove(5)
    my_list.remove(4)
    my_list.remove()
    print_output(my_list)


    print("\n\n\tTESTING reverse()")
    print("The output DLL should be [9 8 7 6 3 2]")
    print("The size of the DLL should be 6\n")
    my_list.reverse()
    print_output(my_list)

    my_list.clear()
    print("\nThe output DLL should be [2 1]")
    print("The size of the DLL should be 2\n")
    my_list.append(1)
    my_list.append(2)
    my_list.reverse()
    print_output(my_list)

    


def print_output(my_list: DoublyLinkedList):
    print("The DLL is:")
    my_list.print_list()
    print("The DLL in reverse order is:")
    my_list.print_list_in_reverse()
    print("The DLL size is: ", end='')
    print(my_list.get_size())


if __name__ == "__main__":
    main()