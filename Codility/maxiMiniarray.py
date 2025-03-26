# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9


# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#               Maximum element is: 35

# Python program to find Maximum and minimum of an array using minimum number of comparisons
def set_min(A):
    mini = float('inf')  # Initialize mini as positive infinity
    for num in A:
        if num < mini:
            mini = num
    return mini


def set_max(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi


# Driver code
if __name__ == "__main__":
    A = [4, 9, 6, 5, 2, 3]
    N = len(A)
    print("Minimum element is:", set_min(A))
    print("Maximum element is:", set_max(A))
