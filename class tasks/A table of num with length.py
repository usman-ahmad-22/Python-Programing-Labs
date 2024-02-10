import os
os.system('cls')

num=int((input('enter table number= ')))
len=int(input('enter product length of table= '))
for i in range (1,len+1):
	print(num,'	*	',i,' 	=',num*i,)
input()
