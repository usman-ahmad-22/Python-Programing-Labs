def fib(n):    # write function for Fibonacci series up to n
 a= 0
 b= 1
 while a < n:
         print(a, end=' ')
         a, b = b, a+b
         print()

# Now call the function we just defined:
print(fib(200))
