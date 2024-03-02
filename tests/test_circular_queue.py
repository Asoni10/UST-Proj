import unittest
from circular_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_enqueue(self):
        cq = CircularQueue(max_length=3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        self.assertEqual(len(cq.queue), 3)

    def test_dequeue(self):
        cq = CircularQueue(max_length=3)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.dequeue()
        self.assertEqual(len(cq.queue), 2)

if __name__ == "__main__":
    unittest.main()
