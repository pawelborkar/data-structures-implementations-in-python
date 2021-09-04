from Queue import LinkedQueue
from queueFromStack import QueueFromStack

if __name__ == '__main__':

    myQueue = LinkedQueue[int]()
    passed = True

    print("TESTING QUEUE\n\n")

    print("Testing enqueue() and dequeue()...")
    for i in range(1, 11):
        myQueue.enqueue(i)
    for i in range(1, 6):
        received = myQueue.dequeue()
        if received != i:
            passed = False
            print("Should receive ", i, " instead of ", received)
    if passed:
        print("\tPASSED\n")

    print("Testing get_size()...")
    passed = True
    size = myQueue.get_size()
    if size != 5:
        passed = False
        print("The size should be 5 instead of ", size)
    if passed:
        print("\tPASSED\n")

    print("Testing get_front()...")
    passed = True
    for i in range(6, 9):
        received = myQueue.get_front()
        if (received != i):
            passed = False
            print("The received result should be ", i, " instead of ", received)
        myQueue.dequeue()
    if passed:
        print("\tPASSED\n")

    print("Testing clear()...")
    passed = True
    myQueue.clear()
    if myQueue.get_size() != 0:
        passed = False
        print("The size should be now zero!!!")
    if passed:
        print("\tPASSED\n")
    



