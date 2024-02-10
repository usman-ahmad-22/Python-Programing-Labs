import os
os.system('cls')
char=(input("enter character type\n" ))
quantity=(int(input("enter character quantity in integers\n" )))
for i in range(quantity):
	print(char, end='')
