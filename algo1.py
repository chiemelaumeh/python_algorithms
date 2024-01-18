# Write a recursive function factorial(n) that takes in a positive
# integer n, and returns the factorial of n (1 x 2 x 3 x … x n)

# SOLUTION
def factorial(n):
    if n != 1:
        return n * factorial(n-1)
    return n


print(factorial(4))
