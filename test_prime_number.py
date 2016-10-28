import unittest 
import prime_number
"""
Test case for prime_number_finder
"""
class prime_number_finder_test(unittest.TestCase):
	def testprime(self):
		assertEquals(prime_number.prime_finder(100),[])