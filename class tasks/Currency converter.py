print('*'*40)
print('       welcome to currency convertor')
print('*'*40)
print('USD => PKR : 1')
print('PKR => USD : 2')
choice=int(input('select your choice 1 or 2:\n'))
if choice ==1:
    usd=int(input('enter Amount in USD: '))
    amount=usd*287
    print(usd,'dollar is = {} pakistani rupees'.format(amount))
elif choice==2:
    pkr=int(input('enter Amount in PKR: '))
    amount=pkr//287
    print(pkr,' pakistani ruppes is = {} dollar'.format(amount))
else:
    print('invalid choice')
print('\n[Thank you for using our convertor]')
input()
