import unittest 
import prime_number
"""
Test case for prime_number_finder
"""
class prime_number_finder_test(unittest.TestCase):
	def testprime(self):
		self.assertEquals(prime_number.prime_finder(40),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

if __name__ == '__main__':
    unittest.main()    		