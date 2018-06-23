
a= range(100,1000)
b= range (100,1000)

lista=[]

for i in a:
	for j in b:
		c=i*j
		e=int(str(c)[::-1])
		if e==c:
			lista.append(c)


print(max(lista))
