#Linear search
def linear_search(numbers, target):
   for i in range(len(numbers)):
      if numbers[i]==target:
          return i
   return -1
numbers=[15,13,72,8,44,91,6]
result=linear_search(numbers, 44)

if result != -1:
   print(f"found 44 at position {result}")
else:
   print("Not Found")

#Binary search
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

if result != -1:
    print(f"Found 44 at position {result}")
else:
    print("Not found!")

#Binary search 2
def contacts(names, target):
    first = 0                       # start of the contacts list
    last = len(names) - 1           # end of the contacts list

    while first <= last:            # keep searching while list has items left
        middle = (first + last) // 2        # find the middle position
        
        if names[middle] == target:         # did we land on the name we want?
            return middle                   # YES → send back the position
        elif names[middle] < target:        # middle name comes BEFORE target alphabetically
            first = middle + 1              # target is in RIGHT half → move first up
        else:                               # middle name comes AFTER target alphabetically
            last = middle - 1              # target is in LEFT half → move last down

    return -1                       # name not found in contacts

names = ["Agy", "Alice", "Bannard", "Brenda", "Gabiro", "Gax", "Xedo"]   # sorted contacts list
target = "Gabiro"                   # name we are searching for

result = contacts(names, target)    # run the search and save position

if result != -1:                    # -1 means not found, anything else means found
    print(f"Found '{names[result]}' at position {result}")    # show name and position
else:
    print(f"'{target}' does not exist in your contacts")      # name not in list

#Binary search that gets both upper and lower case
def contacts(names, target):
    first = 0
    last = len(names) - 1
    
    # Convert everything to lowercase for comparison
    names_lower = [name.lower() for name in names]
    target_lower = target.lower()
    
    while first <= last:
        middle = (first + last) // 2
        if names_lower[middle] == target_lower:
            return middle
        elif names_lower[middle] < target_lower:
            first = middle + 1
        else:
            last = middle - 1
    return -1

names = ["Agy", "Alice", "Bannard", "Brenda", "Gabiro"]
search = "alice"   # lowercase — will still find Alice!
result = contacts(names, search)

if result != -1:
    print(f"Found '{names[result]}' at position {result}")
else:
    print(f"'{search}' does not exist in your contacts")

#Question
def search(numbers, target):
    for i in range(len(numbers)):      # go through each position one by one
        if numbers[i] == target:       # is this the number we are looking for?
            return i                   # YES → send back the position
    return -1                          # went through everything → not found

result = search([4, 7, 2, 9, 1], 7)   # save the result

if result != -1:                       # was it found?
    print(f"Found {7} at position {result}")   # YES → print position
else:
    print("Not found!")                # NO → tell user

def binary(numbers, target):
    left=0
    right=len(numbers)-1
    while left<=right:
        middle=(left+right)//2
        if numbers[middle]==target:
            return middle
        elif numbers[middle]<target:
            left= middle+1
        else:
            right= middle-1
    return -1
numbers=[1,3,5,6,7,8,10]
target=5
results= binary(numbers,target)
if results!=-1:
    print(f"The number {target} is at position {results}")
else:
    print(f"{target} does not exist in your contacts")


#My code
def contacts(names,target):
    for i in range(len(names)):
        if names[i]==target:
            return i
    return -1
names=["Joe", "Hal", "Martin", "Leno", "Louis", "Rose"]
target="Martin"
result=contacts(names,target)
password=target
guess=input("Enter password:",)
while guess!=password:
    print("Wrong pass word Try Again!")
    guess=input("Enter password:",)
print("Correct Password")

#Find names and position with short code
names = ["Agy", "Alice", "Bannard", "Brenda", "Gabiro"]
search = "Gabiro"
if search in names:
    position = names.index(search)# Check first — otherwise .index() crashes if not found!
    print(f"Found {search} at position {position}")
else:
    print(f"{search} does not exist in your contacts")

#Find name and position even with lower case(no need for a sorted list)
names = ["Gabiro","Agy", "Alice", "Bannard", "Brenda"]
search = "gabiro"
if search.lower() in [name.lower() for name in names]:
    position=[name.lower() for name in names].index(search.lower())
    print(f"Found {names[position]} in position {position} of your contacts")
else:
    print(f"{search} is not in your conatcts")




#Using bisect witch is an inbuilt for binary
import bisect                                              # bring in Python's built in binary search tool

names = ["Agy", "Alice", "Bannard", "Brenda", "Gabiro"]  # sorted contacts list — must be sorted!
search = "Bannard"                                        # name we are looking for

position = bisect.bisect_left(names, search)              # binary search — finds position of name or where it would go

if position < len(names) and names[position] == search:   # two checks — is position inside list AND is name actually there?
    print(f"Found {search} at position {position}")       # both checks passed — name exists!
else:
    print(f"{search} does not exist in your contacts")    # one check failed — name not found

#Modern inbuilt code
numbers = [15, 3, 72, 8, 44, 91, 6]

# Check if item exists — returns True/False
print(44 in numbers)        # True
print(100 in numbers)       # False

# Find position of item
print(numbers.index(44))    # 4

# With error handling — professional way
try:
    position = numbers.index(100)
except ValueError:
    print("Item not found!")

