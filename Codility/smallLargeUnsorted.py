# K’th Smallest/Largest Element in Unsorted Array | Expected Linear Time

# Given an array of distinct integers and an integer k, where k is smaller than the array’s size, the task is to find the k’th smallest element in the array.

# Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: The sorted array is [3, 4, 7, 10, 15, 20], so the 3rd smallest element is 7.


# Input: arr = [7, 10, 4, 3, 20, 15], k = 4
# Output: 10
# Explanation: The sorted array is [3, 4, 7, 10, 15, 20], so the 4th smallest element is 10.

# Python program to find K’th Smallest/
# Largest Element in Unsorted Array
import random

# Partition function: Rearranges elements
# around a pivot (last element)


def partition(arr, l, r):
    x = arr[r]
    i = l

    # Iterate through the subarray
    for j in range(l, r):

        # Move elements <= pivot to the left partition
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place the pivot in its correct position
    arr[i], arr[r] = arr[r], arr[i]
    return i

# Randomizes the pivot to avoid worst-case performance


def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = random.randint(0, n - 1)
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return partition(arr, l, r)

# function to find the k'th smallest element using QuickSelect


def quickSelect(arr, l, r, k):

    # Check if k is within the valid range of the current subarray
    if 0 < k <= r - l + 1:

        # Partition the array and get the pivot's final position
        pos = randomPartition(arr, l, r)

        # If pivot is the k'th element, return it
        if pos - l == k - 1:
            return arr[pos]

        # If pivot's position is larger than k, search left subarray
        if pos - l > k - 1:
            return quickSelect(arr, l, pos - 1, k)

        # Otherwise, search right subarray and adjust k
        # (k is reduced by the size of the left partition)
        return quickSelect(arr, pos + 1, r, k - (pos - l + 1))

    # Return infinity for invalid k (error handling)
    return float('inf')


def kthSmallest(arr, k):
    n = len(arr)
    return quickSelect(arr, 0, n - 1, k)


if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    k = 3
    print(kthSmallest(arr, k))
