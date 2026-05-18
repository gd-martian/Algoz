


name= "Alice"
age = 25
height = 5.9
is_student = True

print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Is a student?",is_student)

name=input("What is your name?")
age=input("How old are you?")
print("Hello",name)
print("You are",age,"years old")

number1=45
number2=72
if number1>number2:
    print("The biggest number is:",number1)
else:
    print("The biggest number is:",number2)

number1= int(input("Enter first number: " ))
number2= int(input("Enter second number: "))
if number1>number2:
    print("The biggest number is:",number1)
else:
    print("The bigget number is:", number2)



for i in range(5):
    print("Hello!")

count = 1
while count <= 5:
    print("Count is:", count)
    count = count +1


password= "python123"
guess = input("Enter password:")
while guess != password:
    print("Wrong password! Try again")
    guess = input("Enter password:")

print("Correct password")

# Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Algorithms can loop through collections of data
fruits = ["mango", "banana", "apple", "orange"]

for fruit in fruits:
    print("Fruit:", fruit)


numbers=[34,78,12,99,45,23]
largest= numbers[0]
for number in numbers:
    if number>largest:
        largest=number
print("The largest number ",largest)

#leason 4 Hint: An even number divided by 2 has no remainder. In Python, % gives you the remainder. So 4 % 2 == 0 means 4 is even.
for number in range(1,11):
    if number % 2==0:
        print(number)

def greet(name):
    return "Hello " + name

result = greet("Alice")
print(result)

# Call it multiple times with different arguments!
print(greet("Bob"))
print(greet("Charlie"))

def count(num1,num2):
    total=num1 + num2
    return total
print(count(11,22))
print(count(11,1))
print(count(1,4))


# Function to find the largest number
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Now use it with different lists!
list1 = [34, 78, 12, 99, 45]
list2 = [5, 2, 8, 1, 9]
list3 = [100, 200, 150, 175]

print("Largest in list1:", find_largest(list1))
print("Largest in list2:", find_largest(list2))
print("Largest in list3:", find_largest(list3))


#My own from the above
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print("The largets number is",find_largest([5, 2, 8, 1, 9]))
print("The largets number is",find_largest([100, 200, 150, 175]))

def multiply(num1, num2):
    return num1 * num2

def square(number):
    return multiply(number, number)  # calls multiply!

print(square(4))    # 4 x 4 = 16
print(square(7))    # 7 x 7 = 49

def add(numbers):
    total=0
    for number in numbers:
        total+=number
    return total/len(numbers)  #len counts how many numbers are in the list
print(add([10,20,30,40,50]))


def find_smallest(numbers):
    smallest=numbers[0]
    for number in numbers:
        if number<smallest:
            smallest=number
    return smallest
print(find_smallest([22,5,26,3,6]))

def first(number):
    return number[0]
print(first[1,3,4,5,6])

#LEASON 5
def find(names, target):
    for name in names:
        if name==target:
            return True
    return False
names=["John","Hola","Martin","Anna","Mark"]
print(find(names,"John"))
print(find(names,"Allen"))
print(find(names,"Klac"))
print(find(names,"Anna"))


#if i == j and i is not j:
    # i == j      → do they have the same VALUE?  (e.g. both are 2)
    # i is not j  → are they DIFFERENT items?     (not the same position)
 #   print(i, "is a duplicate!")
def find_duplicates(numbers):
    for i in numbers:
        for j in numbers:
            if i != j and numbers.index(i) != numbers.index(j):
                if i == j:
                    print("duplicate found:", i)

def greet(names):
    for name in names:
        print("Hello "+name)
greet(["Mark","Kal"])
def greet(names):
    for name in names:
        print("Hello", name)
greet(["Mark","Jew"])

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):              # outer loop — number of passes
        for j in range(0, n-i-1):  # inner loop — comparisons per pass
            if numbers[j] > numbers[j+1]:
                # Swap the two neighbours
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

my_list = [64, 34, 25, 12, 22, 11, 90]
print("Sorted:", bubble_sort(my_list))

def bubble_sort(numbers):
    n = len(numbers)
    print(f"Pass {i+1}:", numbers)
    for i in range(n):              # outer loop — number of passes
        for j in range(0, n-i-1):  # inner loop — comparisons per pass
            if numbers[j] > numbers[j+1]:
                # Swap the two neighbours
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print("Sorted:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

#INSERTION SORT
def insertion_sort(numbers):
    for i in range(1, len(numbers)):    # start from second element
        key = numbers[i]                # the element we're inserting
        j = i - 1                       # look at elements before it

        while j >= 0 and numbers[j] > key:
            numbers[j+1] = numbers[j]  # shift element right
            j -= 1                     # move one position left

        numbers[j+1] = key             # insert in correct position

    return numbers

my_list = [64, 34, 25, 12, 22, 11, 90]
print("Sorted:", insertion_sort(my_list))

#Bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    print(f"Pass {i+1}:", numbers)
    for i in range(n):              # outer loop — number of passes
        for j in range(0, n-i-1):  # inner loop — comparisons per pass
            if numbers[j] > numbers[j+1]:
                # Swap the two neighbours
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print("Sorted:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

#More tactical sorting
def largets(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
            return largest
def sorted(numbers):
        for i in range(1, len(numbers)):
             key= numbers[i]
             j =i-1
             while j>=0 and numbers[j]> key:
                  numbers[j+1]=numbers[j]
                  j-=1
                  numbers[j+1]=key
        return numbers
list=[64, 34, 25, 12, 22, 11, 90]
print("Largets number is",largets(list), "and Sort list is:", sorted(list))

#shortcut

list=[64, 34, 25, 12, 22, 11, 90]
print("Largets number is",max(list), "and Sort list is:", sorted(list))



def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

numbers = [64, 34, 25, 12, 22, 11, 90]

sorted_numbers = insertion_sort(numbers)  # Sort first
print("Sorted list is:", sorted_numbers, "and largets is:", sorted_numbers[-1])

#Best 
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
    
def sort_and_find(numbers):
    sorted_list = insertion_sort(numbers)
    largest = sorted_list[-1]
    return sorted_list, largest

sorted_list, largest = sort_and_find([64, 34, 25, 12, 22, 11, 90])
print("Sorted list:", sorted_list)
print("Largest number is:", largest)

#shortcut for the opposite
def contacts(numbers):
    sorted_list = insertion_sort(numbers)
    largest = sorted_list[-1]
    return sorted_list, largest
numbers = [44, 25, 64, 2, 43, 7, 1, 68, 8, 4]
numbers.sort(reverse=True)
print("Sorted list is:", numbers, "Highest number is:", max(numbers))
names = ["Agy","Alice","Bannard","Brenda","Gabiro","Gax","Xedo"]

search = "Gax"  # ← stored in a variable OUTSIDE the function
result = contacts(names, search)

if result != -1:
    print(f"Found '{names[result]}' at position {result}")
else:
    print(f"'{search}' does not exist in your contacts")  # ← use 'search' not 'target'