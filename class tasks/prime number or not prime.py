num=int(input('enter a number : '))
for i in range(2,num):
     				#for check factors
	if num%i==0:
		print(num,'is not a prime number')
		print(i,   '*'   ,num//i, 'is = ',num)
		break
else:
	print(num,'is a prime number')

input()