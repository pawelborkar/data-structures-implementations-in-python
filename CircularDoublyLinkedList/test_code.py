from circular_doubly_linked_list import CircularDoublyLinkedList

def main():
    llist = CircularDoublyLinkedList[int]()

    for i in range(1, 11):
        llist.append(i)
    print(llist.get_size())
    print(llist.to_array())

    print(llist.remove(5))
    print(llist.remove(8))
    print(llist.to_array())
    


if __name__ == "__main__":
    main()