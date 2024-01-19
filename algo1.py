# Write a recursive function factorial(n) that takes in a positive
# integer n, and returns the factorial of n (1 x 2 x 3 x … x n)

# SOLUTION
def factorial(n):
    while n != 1:
        return n * factorial(n-1)
    return n


# print(factorial(4))


# Write a recursive function sum_odd(list) that takes in a list of integers,
# and returns the sum of only odd numbers inside the list.
def addOddNumbers(list, index):
    count = 0
    while index < len(list):
        if list[index] % 2 == 1:
            count += list[index]
        return count + addOddNumbers(list, index+1)
    return count
print(addOddNumbers([1,2,3,4,5,6,7,8,9,10],0))