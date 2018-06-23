'''listprime=[2]
end=20
skip=[]
for num in range(3,end,2):
	if num in skip:
		continue
	else:
		prime = True
		for i in range(2,num):
		    if (num%i==0):
		        prime = False
		if prime:
			skip.extend(range(num,end,num))	
			listprime.append(num)
print(listprime)
#print(skip)'''

'''def longestsum(n):
	listr=[]
	listq=[]
	for i in listprime:
		if i<n:
			listr.append(i)
	listap=listr[::-1]

	m=len(listap)

	r=listr[m-1]

	for i in range(1,m):
		if r-listap[i]>0:
			r=r-listap[i]
		elif r-listap[i]==0:
			listq.append(listap[i])
		else:
			r=listr[m-1]
			break
	return listq

print(longestsum(100))'''
'''p=0
plist=[]
for i in listprime:
	p+=i
	if p in listprime:
		plist.append(p)
print(plist)'''


def capitalize(string):
    #S=str(string)
    sp=str(string).split()
    a=''
    for i in sp:
    	listaa=list(i)
    	listaa[0]=str(listaa[0]).upper
    	j="".join(str(listaa))
    	#a=j + ' '+a 
    return j

if __name__ == '__main__':
	a=capitalize('chris alan')
	print(a)


