num=int(input('Enter a number : '))
for i in range(num+1,num*num):
	for j in range(2,i):
		if i%j ==0:
			break
	else:
		print('prime number after ',num,'is\n',i)
		break
input()