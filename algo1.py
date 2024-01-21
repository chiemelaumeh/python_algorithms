import math
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
        # print(index)
        i = list[index]
        if i % 2 == 1:
            count += i
        return count + addOddNumbers(list, index+1)
    return count

# print(addOddNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))

# Write a recursive function sum_sub(lis) that takes in a list of integers.
# This function sums all odds numbers, and subtracts all even numbers, and
# returns the final output.


def addOddNumsAndSubtractEvenNums(list, index):
    even = 0
    odd = 0
    # print(even, odd)
    if index > len(list):
        return 0

    i = list[index]
    if i % 2 == 0:
        odd += i

    return odd + addOddNumbers(list, index+1)


# #
# print(addOddNumsAndSubtractEvenNums([5, 8], 0))


# recieve the number, loop from 1 to just before the number
# if number/1 == 0, return true
# else, return falsee

def isPrime(num, count):
    for i in range(2, round(math.sqrt(num))):
        if num % i == 0:
            return False
        return True




# print(isPrime(15, 2))


# Given a natural number n, find the largest integer that is less than or
# equal to √n.

def integerSquare(num):
    return math.floor(math.sqrt(num)) 
print(integerSquare(12))
    
