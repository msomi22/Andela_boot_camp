"""
A prime number that is only devisible by one and it self
Example:
1,3,5,7,11,13,17,19,23 and so one
"""
def prime_number_finder(endpoint):
	for num in range(0,endpoint):
		if num%2 != 0:
			print num 


prime_number_finder(100)