from typing import Deque
from priority_queue import PriorityQueue, LinkedPriorityQueue

def main():
    priority_queue = LinkedPriorityQueue()
    vals = [4, 5, 6, 7, 2, 1]
    prio = [0, 1, 2, 3, 4, 5] 

    for i in range(len(vals)):
        priority_queue.enqueue(vals[i], prio[i])
    # output should be 4 5 6 7 2 1
    while not priority_queue.is_empty():
        print(priority_queue.dequeue(), end=' ')

    print()

    for i in range(len(vals)):
        priority_queue.enqueue(vals[len(vals) - i - 1], prio[i])
    # output should be 1 2 7 6 5 4
    while not priority_queue.is_empty():
        print(priority_queue.dequeue(), end=' ')

    print()

    for i in range(len(vals)):
        priority_queue.enqueue(vals[i], vals[i])
    # output should be 1 2 4 5 6 7
    while not priority_queue.is_empty():
        print(priority_queue.dequeue(), end=' ')

    print()

    # output should be 4, 6
    priority_queue.enqueue(4, 0)
    priority_queue.enqueue(5, 2)
    priority_queue.enqueue(6, 1)
    print(priority_queue.dequeue(), end=' ')

    print()

    # output should be True
    priority_queue.reset()
    print(priority_queue.is_empty())

    print()


    priority_queue.enqueue(4, 3)
    priority_queue.enqueue(3, 3)
    priority_queue.enqueue(2, 3)
    priority_queue.enqueue(1, 3)
    priority_queue.enqueue(6, 4)
    priority_queue.enqueue(5, 4)

    # output should be 1 2 3 4 5 6
    while not priority_queue.is_empty():
        print(priority_queue.dequeue(), end=' ')


if __name__ == "__main__":
    main()