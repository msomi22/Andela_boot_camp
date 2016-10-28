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
	for num in range(0,endpoint):
		if endpoint == 0:
			return 0
		elif endpoint == 1:	
			return 1
		else:	
			return fibonacii_finder(endpoint-1) + fibonacii_finder(endpoint-2)
		
print fibonacii_finder(3)