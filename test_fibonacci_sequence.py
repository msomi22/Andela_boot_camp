
import unittest
import fibonacci_sequence
"""
Test case for fibonacii_finder
"""
class fibonacii_finder_test(unittest.TestCase):
	def testfibonacci(self):
		self.assertTrue(fibonacci_sequence.fibonacii_finder(10),[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) 

if __name__ == '__main__':
    unittest.main()        


