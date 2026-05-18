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