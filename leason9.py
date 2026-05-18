def merge(left, right):
    result = []        # this will hold our merged list
    i = 0              # pointer for left list
    j = 0              # pointer for right list

    # Compare items from both lists and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])   # append adds item to end of list
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One list finished — add whatever remains from the other
    result.extend(left[i:])    # extend adds all items from a list
    result.extend(right[j:])

    return result
left=[27,43]
right=[3,9]
print(merge(left,right))


def merge(left, right):
    result = []        # this will hold our merged list
    i = 0              # pointer for left list
    j = 0              # pointer for right list

    # Compare items from both lists and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])   # append adds item to end of list
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One list finished — add whatever remains from the other
    result.extend(left[i:])    # extend adds all items from a list
    result.extend(right[j:])

    return result
def merge_sort_visible(numbers, depth=0):
    indent = "  " * depth    # indent shows recursion depth
    print(f"{indent}Splitting: {numbers}")

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort_visible(numbers[:middle], depth + 1)
    right = merge_sort_visible(numbers[middle:], depth + 1)

    merged = merge(left, right)
    print(f"{indent}Merged: {merged}")
    return merged

merge_sort_visible([38, 27, 43, 3, 9, 82])

#THIS TO UNDERSTAND

#MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

players = [
    ("Alice", 850), ("Bob", 1200), ("Charlie", 450),
    ("Diana", 990), ("Eve", 1200), ("Frank", 750)
]

sorted_players = merge_sort(players)

print("🏆 LEADERBOARD 🏆")
for i in range(len(sorted_players)):
    name, score = sorted_players[i]
    print(f"{i+1}. {name:<10} - {score} points")

#QUICK SORT
players = [
    ("Alice", 850),
    ("Bob", 1200),
    ("Charlie", 450),
    ("Diana", 990),
    ("Eve", 1200),
    ("Frank", 750)
]

def quicksort_players(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2][1]          # grab the SCORE from the middle player

    left  = [x for x in arr if x[1] > pivot]   # scores HIGHER than pivot
    mid   = [x for x in arr if x[1] == pivot]  # scores EQUAL to pivot
    right = [x for x in arr if x[1] < pivot]   # scores LOWER than pivot

    return quicksort_players(left) + mid + quicksort_players(right)


sorted_players = quicksort_players(players)

print("🏆 LEADERBOARD 🏆")
for i, (name, score) in enumerate(sorted_players, start=1):
    print(f"{i}. {name:<10} - {score} points")



#SHORTEST CODE FOR THE ABOVE TWO
players = [
    ("Alice", 850), ("Bob", 1200), ("Charlie", 450),
    ("Diana", 990), ("Eve", 1200), ("Frank", 750)
]

sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

print("🏆 LEADERBOARD 🏆")
for i, (name, score) in enumerate(sorted_players, start=1):
    print(f"{i}. {name:<10} - {score} points")