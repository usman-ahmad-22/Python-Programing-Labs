low=int(input('enter lower range : '))
high=int(input('enter higher range : '))
if low > high :
#for swap the values
	low= low + high
	high=low - high
	low= low-high
for num in range(low,high+1):
	for i in range (2,num):
		if num%i==0:
			break
	else:
		print(num)

input()
