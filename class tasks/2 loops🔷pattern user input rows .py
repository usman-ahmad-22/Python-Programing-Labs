import os
os.system('cls')

row = int(input('enter no of rows of pyramid  : '))
rows=int(row+1)

for i in range (rows):
	print(' ' * (rows-i-1) + '*' * (2*i-1))
	
for j in range(rows-2,0,-1):
	print(' ' *(rows-j-1) + '*' *(2*j-1))