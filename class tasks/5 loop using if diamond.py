print('    WELCOME to * Diamond ')
for i in range(1,10):
	if (i<6):	
	    for j in range(6,i,-1):
	        print('-',end='')
	    for k in range(1,2*i):	
	        print('*',end='')
	else:
	    for l in range(5,i+1):
		    print('-',end='')
	    for m in range(19,2*i,-1):	
	        print('*',end='')
	print()
input()
