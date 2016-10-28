"""
A prime number that is only devisible by one and it self
Example:
1,3,5,7,11,13,17,19,23 and so one
"""
def prime_finder(endpoint):
	start = 2
	while start <= endpoint:
	    is_prime=True
	    for i in range(2, start):
	        if start%i == 0:
	            is_prime=False
	            break;
	    if is_prime==True:
	        print start
	    start = start+1
	

#prime_finder(100)    
       
   
