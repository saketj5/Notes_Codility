# Given two arrays a[] and b[] with distinct elements of size n and m respectively, the task is to find intersection (or common elements) of the two arrays. We can return the answer in any order.

# Note: Intersection of two arrays can be defined as a set containing distinct common elements between the two arrays.

# Examples:

# Input: a[] = { 5, 6, 2, 1, 4 }, b[] = { 7, 9, 4, 2 }
# Output: { 2, 4 }
# Explanation: The only common elements in both arrays are 2 and 4.

# Input: a[] = { 4, 5, 2, 3 } , b[] = { 1, 7 }
# Output: { }
# Explanation: There are no common elements in array a[] and b[]

# Python program for intersection of two arrays with
# distinct elements using hash set

def intersect(a, b):

    # Put all elements of a[] in hash set
    st = set(a)
    res = []
    for i in range(len(b)):

        # If the element is in st
        # then add it to result array
        if b[i] in st:
            res.append(b[i])

    return res


if __name__ == "__main__":
    a = [5, 6, 2, 1, 4]
    b = [7, 9, 4, 2]

    res = intersect(a, b)
    for num in res:
        print(num, end=" ")
