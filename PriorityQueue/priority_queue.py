from typing import Generic, TypeVar
import heapq

T = TypeVar('T')

# CAN'T USE ON OBJECT

class PriorityQueue(Generic[T]):
    def __init__(self):
        self.reset()
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def enqueue(self, item: T, priority: float):
        self.size += 1
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self) -> T:
        self.size -= 1
        return heapq.heappop(self.elements)[1]

    def get_size(self):
        return self.size

    def reset(self):
        self.size = 0
        self.elements: list[tuple[float, T]] = []







###################################
######### PRIORITY QUEUE ##########
class LinkedPriorityQueue:
    def __init__(self):
        self.reset()

    # add new node to the queue
    # The lower the priority is, the faster it gets to be poped
    def enqueue(self, val, priority):
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
    def dequeue(self):
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
    def peek(self):
        if self.is_empty():
            raise Exception('Attempted to peek an empty queue!!!')
        return self.head.get_value()

    # get the size of the queue
    def get_size(self):
        return self.size

    # check if the queue is empty
    def is_empty(self):
        return self.size == 0

    def reset(self):
        self.head = None
        self.tail = None
        self.size = 0



#######################
#### PRIORITY NODE ####
class PriorityNode:
    def __init__(self, value, priority, next=None):
        self.value = value
        self.priority = priority
        self.next = next

    def get_value(self):
        return self.value

    def get_priority(self):
        return self.priority

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next