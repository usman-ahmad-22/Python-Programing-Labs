print('    WELCOME to * triangle ')
for i in range(1,6):
	for j in range(6,i,-1):
		print('-',end='')
	for k in range(1,2*i):	
		 print('*',end='')
				   
	print('')
	#if we want to print even pattern then change range starting no 1 to 0
input() 