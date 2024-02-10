import os
os.system('cls')
number = float(input("Please enter the number: "))
guess = number/2
while abs ( (guess*guess)- number) > 0.001:
	guess = (guess + number/guess)/2
print(guess)
