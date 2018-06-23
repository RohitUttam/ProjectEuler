
'''listprime=[]
for num in range(3,1000000,2):
	prime = True
	for i in range(2,num):
	    if (num%i==0):
	        prime = False
	if prime:	
	 	listprime.append(num)
	if len(listprime)==10002:
		break

print(listprime[10001])'''

skip=[]
l=range(3,1000,3)
skip.extend(l)	


print(18 in skip)