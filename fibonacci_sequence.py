"""
 In fibonacci sequence we and first two numbers to get the next one,
 Exampe:
 we start with 0 and 1
 0 + 1 = 1
 1 + 1 = 2
 1 + 2 = 3    and so on
 this will give 0,1,2,3,5,8 and so on
"""
def fibonacii_finder(endpoint):
	numlist = []
	for num in range(endpoint):
		if not (num is None):
			numlist.append(num)
			print numlist
		
		
		
		
		

print fibonacii_finder(8)