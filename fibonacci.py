#!/usr/bin/python3
def fib(n):
    if n > 1:
       return fib(n-1) + fib (n-2)
    return n
k = int(input ())
for i in range (k):
    print (i, fib(i))