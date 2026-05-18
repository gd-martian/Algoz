#Countdown (simplest recursion):
def countdown(n):
    if n == 0:             # BASE CASE — stop here!
        print("Go!")
        return
    print(n)               # print current number
    countdown(n - 1)       # call itself with smaller number

countdown(5)

# Factorial (classic recursion problem):
def factorial(n):
    if n == 1:                    # BASE CASE
        return 1
    return n * factorial(n - 1)  # RECURSIVE CASE

print(factorial(5))   # 120
print(factorial(4))   # 24
print(factorial(3))   # 6

# Sum of a list recursively:
def recursive_sum(numbers):
    if len(numbers) == 0:    # BASE CASE — empty list = 0
        return 0
    return numbers[0] + recursive_sum(numbers[1:])  # first + rest #numbers[1:] means "everything except the first item" — it's called slicing. Each call the list gets shorter until it's empty!


print(recursive_sum([1, 2, 3, 4, 5]))  # 15

#Binary Search Recursively:
def binary_search_recursive(numbers, target, left, right):
    if left > right:                        # BASE CASE — not found
        return -1
    
    middle = (left + right) // 2
    
    if numbers[middle] == target:           # found!
        return middle
    elif numbers[middle] < target:          # search right half
        return binary_search_recursive(numbers, target, middle + 1, right)
    else:                                   # search left half
        return binary_search_recursive(numbers, target, left, middle - 1)

numbers = [3, 6, 8, 15, 44, 72, 91]
result = binary_search_recursive(numbers, 44, 0, len(numbers) - 1)
print(f"Found at position: {result}")


#Modern inbuilt code
# Sum — instead of recursive_sum
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))         # 15 — one word!

# Maximum — instead of find_largest
print(max(numbers))         # 5

# Minimum
print(min(numbers))         # 1

# Factorial — Python has a library!
import math
print(math.factorial(5))    # 120


#test
def mystery(n):
    if n <= 0:
        return 0
    return n + mystery(n - 1)

print(mystery(4))

def binary_search(numbers, target):
    left = 0                           # start of search area
    right = len(numbers) - 1          # end of search area

    while left <= right:
        middle = (left + right) // 2  # find middle position
        
        if numbers[middle] == target:  # found it!
            return middle
        elif numbers[middle] < target: # target is in right half
            left = middle + 1          # move left boundary up
        else:                          # target is in left half
            right = middle - 1         # move right boundary down

    return -1                          # not found

sorted_numbers = [3, 6, 8, 15, 44, 72, 91]
result = binary_search(sorted_numbers, 44)

import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())  # 1000
    
def power(n,up):
    if up ==0:
        return 1
    return n*power(n,up-1)
n=2
print(power(n,-3)) 


def power(n,p):
    if p==0:
        return 1
    if p<0:
        return 1/power(n,-p)
    return n*power(n,p-1)
n=2
print(power(n,-2))

def power(n,up):
    if up ==0:
        return 1
    elif up <0:
        return 1/power(n,-up)
    return n*power(n,up-1)
n=2
print(power(n,-3)) 

def count(n, stop):
    
    if n>stop:
        count(n-1, stop)
        print(n)
   

count(5,-5)
