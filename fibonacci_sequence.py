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
	init = 0
	first_Value = 0
	second_Value = 1
	while(init < endpoint):
		if(init <= 1):
			num = init
		else:
		 	num = first_Value + second_Value
		 	first_Value = second_Value
		 	second_Value = num
		print(num) 
		init = init + 1 	

print fibonacii_finder(8)