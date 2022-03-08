import unittest
import heapq
import random
from heap import Heap


min_heap = Heap(True)
max_heap = Heap(False)

std_min_heap = []
std_max_heap = []


class TestMethods(unittest.TestCase):

    def test_insert(self):
        for i in range(100):
            
            for j in range(10):
                rand = random.randint(1, 10000)
                
                min_heap.insert(rand)
                heapq.heappush(std_min_heap, rand)
                
                max_heap.insert(rand)
                heapq.heappush(std_max_heap, rand * -1)
                
            self.assertEqual(min_heap.to_list(), std_min_heap)
        
        
    def test_remove(self):
        pass
        
        
    def test_size(self):
        self.assertEqual(min_heap.size(), len(std_min_heap))
        



if __name__ == "__main__":
    unittest.main()