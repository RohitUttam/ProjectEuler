user_input= str('pullup')
length=len(user_input)-1

for i in range(0,length):
	palindrome=True
	l=length-i
	if user_input[i]==user_input[l]:
		palindrome=True
	else:
		palindrome=False

print('Palindrome:',palindrome)


