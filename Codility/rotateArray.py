# Given an array, the task is to cyclically right-rotate the array by one.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]


# Input: arr[] = [2, 3, 4, 5, 1]
# Output: [1, 2, 3, 4, 5]

def rotate(arr):

    # i and j pointing to first and last
    # element respectively
    i, j = 0, len(arr) - 1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rotate(arr)
    for i in range(0, len(arr)):
        print(arr[i], end=' ')
