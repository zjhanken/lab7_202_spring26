import unittest

from lab7_1 import MinHeap, insert, extract, heapify_up, heapify_down


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        heap = MinHeap(heap=[])
        result = insert(heap, 5)
        self.assertEqual(result.heap, [5])

    def test_insert_multiple(self):
        heap = MinHeap(heap=[])
        heap = insert(heap, 5)
        heap = insert(heap, 3)
        heap = insert(heap, 7)
        self.assertEqual(heap.heap, [3, 5, 7])

    def test_extract(self):
        heap = MinHeap(heap=[1, 5, 3])
        min_val, new_heap = extract(heap)
        self.assertEqual(min_val, 1)
        self.assertEqual(new_heap.heap, [3, 5])

    def test_extract_twice(self):
        heap = MinHeap(heap=[1, 5, 3])
        first_val, heap = extract(heap)
        second_val, heap = extract(heap)
        self.assertEqual(first_val, 1)
        self.assertEqual(second_val, 3)
        self.assertEqual(heap.heap, [5])

    def test_heapify_up(self):
        heap = [5, 10, 8, 20, 15, 9, 1]
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])


if __name__ == "__main__":
    unittest.main()
