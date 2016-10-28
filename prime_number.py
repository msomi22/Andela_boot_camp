"""
A prime number that is only devisible by one and it self
Example:
1,3,5,7,11,13,17,19,23 and so one
"""
def prime_finder(endpoint): 
	if endpoint == 2:
		return [2]
	elif endpoint < 2:
		return []

	first=range(3,endpoint+1,2)
	last = endpoint ** 0.5
	nextno=(endpoint+1)/2-1

	i=0
	k=3
	while k <= last:
		if first[i]:
			j=(k*k-3)/2
			first[j]=0

			while j<nextno:
				first[j]=0
				j+=k
		i=i+1
		k=2*i+3

	return [2]+[num for num in first if num] 
       
   
