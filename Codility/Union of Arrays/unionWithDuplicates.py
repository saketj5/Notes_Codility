# Union and Intersection of Two Unsorted Arrays – Complete Tutorial


#### Union of Two Arrays ###
# Union of two unsorted arrays combines all unique elements from both arrays into a single array. The resultant array can be in any order. There are several methods to find the Union of two unsorted arrays based on whether the input arrays contain duplicate elements or not:

# Union with Duplicates: When the input arrays may contain duplicate elements.
# Union with Distinct Elements: When the input arrays consist of distinct elements only.
# 1. Union with Duplicates
# We are given two arrays a[] and b[] and the task is to find the union of both the arrays. Union of two arrays is an array having all distinct elements that are present in either array. The input arrays may contain duplicates.

# Examples:


# Input : a[] = {1, 2, 3, 2, 1}, b[] = {3, 2, 2, 3, 3, 2}
# Output : {3, 2, 1}
# Explanation: Each element in the output either belongs to array a or array b, and we need to print only one occurrence of such elements.


# Input : a[] = {1, 2, 3}, b[] = {4, 5, 6}
# Output : {1, 2, 3, 4, 5, 6}
# Explanation: Each element in the output either belongs to array a or array b, and we need to print only one occurrence of such elements.

# Python program to find union of two arrays

def findUnion(a, b):
    st = set()

    # Put all elements of a[] in st
    for i in range(len(a)):
        st.add(a[i])

    # Put all elements of b[] in st
    for i in range(len(b)):
        st.add(b[i])

    res = []

    # iterate through the set
    # to fill the result array
    for it in st:
        res.append(it)

    return res


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = findUnion(a, b)

    for i in range(len(res)):
        print(res[i], end=' ')
