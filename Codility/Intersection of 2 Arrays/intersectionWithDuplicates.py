# 1. Intersection with Duplicates
# We are given two arrays a[] and b[], the task is to return intersection of both the arrays in any order. Intersection of two arrays is an array having all common elements in both the arrays. The input arrays may contain duplicates.

# Examples:


# Input: a[] = {1, 2, 1, 3, 1},  b[] = {3, 1, 3, 4, 1}
# Output: {1,  3}
# Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.


# Input: a[] = {1, 2, 3},  b[] = {4, 5, 6}
# Output: {}
# Explanation: No common element in both the arrays.


# Function to find intersection of two arrays
def intersection(a, b):
    res = []

    # Traverse through a[] and search every element a[i] in b[]
    for i in a:
        for j in b:

            # If found, check if the element is already in the result
            if i == j and i not in res:
                res.append(i)

    return res


# Driver code
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersection(a, b)

print(" ".join(map(str, res)))
