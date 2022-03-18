import unittest
from src.sort import SortArray

class TestSortArray(unittest.TestCase):
    def setUp(self):
        self.array = ["Wrexham","Amlwch", "Machynlleth","Dolgellau","Bala"]
        self.SortArray = SortArray()

    def test_basic_sort(self):
        self.assertEqual(["Amlwch","Bala", "Dolgellau","Machynlleth","Wrexham"], self.SortArray.standard_sort(self.array))

    def test_reverse_sort(self):
        self.assertEqual(["Wrexham","Machynlleth","Dolgellau","Bala","Amlwch"], self.SortArray.reverse_sort(self.array))
    
    def test_sort_by_length(self):
        self.assertEqual(["Bala","Amlwch","Wrexham","Dolgellau","Machynlleth"], self.SortArray.sortLength(self.array))