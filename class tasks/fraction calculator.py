print('*'*40)
print('welcome to fraction calculator')
print('*'*40)
print('a/b operator c/d')
a=float(input('enter 1st value a:'))
b=float(input('enter 2nd value b:'))
c=float(input('enter 3rd value c:'))
d=float(input('enter 4rth value d:'))
optr=(input('choose operator +,-,*,/ : '))
if optr=='+':
    print('additonal fraction= ',a/b+c/d)
    x=(a*d)+(c*b)
    y=b*d
    print('in p/q form= ',x,'/',y)
elif optr=='-':
    print('subtractionl fraction= ',a/b-c/d)
    x=(a*d)-(c*b)
    y=b*d
    print('in p/q form= ',x,'/',y)
elif optr=='*':
    print('multiplicational fratcion= ',a/b*c/d)
    x=a*c
    y=b*d
    print('in p/q form= ',x,'/',y)
elif optr=='/':
    print('divisional fraction= ',(a/b)/(c/d))
    x=a*d
    y=b*c
    print('in p/q form= ',x,'/',y)
else:
    print('invalid operator')
input()