# Move all negative numbers to beginning and positive to end with constant extra space

# Given an array containing both positive and negative numbers in random order. The task is to rearrange the array elements so that all negative numbers appear before all positive numbers.

# Note:

# Given array does not contain any zeroes.
# Order of resultant array does not matter.
# Example :

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Python program to Move all negative numbers
# to beginning and positive to end

def move(arr):
    arr.sort()
    return arr


if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    ans = move(arr)

    for num in ans:
        print(num, end=" ")
    print()
