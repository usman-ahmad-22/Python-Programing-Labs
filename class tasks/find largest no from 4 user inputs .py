a=float(input('enter your 1st no : '))
b=float(input('enter your 2nd no : '))
c=float(input('enter your 3rd no : '))
d=float(input('enter your 4rth no : '))
if (a>b and a>c and a>d):
	print('{} is a largest number'.format(a))
elif(b>a and b>c and b>d):
	print('{} is a largest number'.format(b))
elif(c>a and c>b and c>d):
	print('{} is th largest number'.format(c))
else:
	print('{} is th largest number'.format(d))
input()