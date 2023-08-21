#Recursion is when a function calls itself

#Factorial 

# n! = n * (n-1)!          ! = it means factorial
# if n! is 0, return 1

def factorial(n):
    if n >= 1:
        return n * factorial(n - 1)
    else:
        return 1


print(f"This is f(0): {factorial(0)}")
print(f"This is f(1): {factorial(1)}")
print(f"This is f(2): {factorial(2)}")
print(f"This is f(3): {factorial(3)}")
print(f"This is f(4): {factorial(4)}")