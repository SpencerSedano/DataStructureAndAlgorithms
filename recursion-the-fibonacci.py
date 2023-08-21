# 1 . 1 . 2 . 3 . 5 . 8

#The Fibonacci Sequence
'''
Each number is equeal to the sum of
the preceding two numbers
'''
#When it doesn't call itself and returns a number, it is called a base case


def Fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    if n < 0:
        print("Not a valid number")

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
 
print(Fibonacci(8))