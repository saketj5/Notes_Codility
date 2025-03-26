# #2. Union with Distinct Elements
# We are given two arrays a[] and b[] with distinct elements and the task is to find the union of both the arrays. Union of two arrays is an array having all distinct elements that are present in either array.

# Examples:


# Input: a[] = {1, 2, 3}, b[] = {5, 2, 7}
# Output: {1, 2, 3, 5, 7}
# Explanation: 1, 2, 3, 5 and 7 are the distinct elements present in either array.


# Input: a[] = {2, 4, 5}, b[] = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4, 5}
# Explanation: 1, 2, 3, 4 and 5 are the distinct elements present in either array.


# Python program to find union of two arrays
# with distinct elements


def findUnion(a, b):
    res = a[:]

    # Traverse through b[] and search every element
    # b[i] in a[]
    for i in range(len(b)):

        # check if the element was present in a[]
        # to avoid duplicates
        if b[i] not in a:

            # if not already present then
            # add it to result
            res.append(b[i])

    return res


if __name__ == "__main__":

    a = [1, 2, 3]
    b = [5, 2, 7]

    res = findUnion(a, b)

    for x in res:
        print(x, end=" ")
