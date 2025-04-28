import unittest
import pair_sum_sorted_program as Pss

class TestPairSumSorted(unittest.TestCase):
    
    def test_correct_value(self):
        result = Pss.PairSumSorted.find_pair_sum([-5, -2, 3, 4, 6], 7)
        self.assertEqual(result, [3,4])
    
    def test_empty_numbers(self):
        result = Pss.PairSumSorted.find_pair_sum([], 0)
        self.assertEqual(result, [])
    
    def test_single_numbers(self):
        result = Pss.PairSumSorted.find_pair_sum([1], 1)
        self.assertEqual(result, [])
    
    def test_two_numbers_found(self):
        result = Pss.PairSumSorted.find_pair_sum([2,3], 5)
        self.assertEqual(result, [0,1])
    
    def test_two_numbers_not_found(self):
        result = Pss.PairSumSorted.find_pair_sum([2,4], 5)
        self.assertEqual(result, [])
    
    def test_three_numbers_found(self):
        result = Pss.PairSumSorted.find_pair_sum([1, 2, 3], 5)
        self.assertEqual(result, [2,3])
    
    def test_three_numbers_not_found(self):
        result = Pss.PairSumSorted.find_pair_sum([-1, 2, 3], 3)
        self.assertEqual(result, [])
    
    def test_three_numbers_not_found(self):
        result = Pss.PairSumSorted.find_pair_sum([-1, 2, 3], 2)
        self.assertEqual(result, [-1, 3])
    
    def test_all_neg_numbers_not_found(self):
        result = Pss.PairSumSorted.find_pair_sum([-3, -2, -1], -5)
        self.assertEqual(result, [])

# Static code
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()