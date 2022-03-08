from linked_queue import LinkedQueue
from queue_from_stacks import QueueFromStack




def test(queue):

    passed = True

    print("Testing enqueue() and dequeue()...")

    for i in range(1, 11):
        queue.enqueue(i)


    for i in range(1, 6):

        received = queue.dequeue()

        if received != i:
            passed = False
            print("Should receive ", i, " instead of ", received)


    if passed:
        print("\tPASSED\n")


    print("Testing get_size()...")
    passed = True
    size = len(queue)

    if size != 5:
        passed = False
        print("The size should be 5 instead of ", size)

    if passed:
        print("\tPASSED\n")


    print("Testing get_front()...")
    passed = True

    for i in range(6, 9):

        received = queue.get_front()

        if (received != i):
            passed = False
            print("The received result should be ", i, " instead of ", received)

        queue.dequeue()


    if passed:
        print("\tPASSED\n")


    print("Testing clear()...")
    passed = True
    queue.clear()

    if queue:
        passed = False
        print("The size should be now zero!!!")
        
    if passed:
        print("\tPASSED\n")
    






if __name__ == '__main__':

    queue = LinkedQueue[int]()

    print("\n\nTESTING LINKED QUEUE\n\n")
    test(queue)

    print("\n\nTESTING QUEUE FROM STACKS\n\n")
    test(queue)




