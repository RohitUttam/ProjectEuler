import math
import time
c=1
lista=[]

time1=time.time()
'''for i in range(1,21):
	c=i*(c)
	print(str(i)+'! is: ', c)'''

for j in range(0,3000000000,2520):
	divisible=True
	for i in range(11,21):
		if (j%i)!=0 or (j%i)==j:
			divisible=False
			break
	if divisible:
		lista.append(j)
		break
time2=time.time()

print(time2-time1,'s')
print(c)
print(lista)
