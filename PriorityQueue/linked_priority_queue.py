from typing import Generic, TypeVar


T = TypeVar('T')
P = TypeVar('P')


class LinkedPriorityQueue(Generic[T, P]):

    def __init__(self) -> None:
        self.reset()




    # add new node to the queue
    # The lower the priority is, the faster it gets to be poped
    def enqueue(self, val: T, priority: P) -> None:

        new_node = PriorityNode(val, priority)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:

            if priority > self.tail.get_priority():
                self.tail.set_next(new_node)
                self.tail = new_node

            elif priority <= self.head.get_priority():
                new_node.set_next(self.head)
                self.head = new_node

            else:
                current = self.head
                while current.get_next() is not None and current.get_next().get_priority() < priority:
                    current = current.get_next()

                temp = current.get_next()
                current.set_next(new_node)
                new_node.set_next(temp)

        self.size += 1




    # pop the node at the top of the queue
    # time complexity: O(1)
    def dequeue(self) -> T:

        if self.is_empty():
            raise Exception('Attempted to dequeue an empty queue!!!')

        temp = self.peek()
        self.head = self.head.get_next()
        self.size -= 1

        # if the new head is None, then the queue is empty
        if self.head is None:
            self.reset() 

        return temp




    # get the value in the front of the queue
    # time complexity: O(1)
    def peek(self) -> T:

        if self.is_empty():
            raise Exception('Attempted to peek an empty queue!!!')

        return self.head.get_value()




    # get the size of the queue
    def get_size(self) -> int:
        return self.size




    # check if the queue is empty
    def is_empty(self) -> bool:
        return self.size == 0




    def reset(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0




#######################
#### PRIORITY NODE ####
class PriorityNode(Generic[T, P]):

    def __init__(self, value: T, priority: P, next:'PriorityNode'=None) -> None:
        self.value = value
        self.priority = priority
        self.next = next


    def get_value(self) -> T:
        return self.value


    def get_priority(self) -> int:
        return self.priority


    def get_next(self):
        return self.next


    def set_next(self, next):
        self.next = next