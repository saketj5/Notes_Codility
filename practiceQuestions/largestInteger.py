def solution(A):
    # Create a set to store the unique values in the array
    unique_values = set()

    # Iterate through the array and add each value to the set
    for num in A:
        unique_values.add(num)

    # Iterate through the unique values set
    largest_k = 0
    for num in unique_values:
        # Check if the opposite number exists in the set
        if -num in unique_values:
            largest_k = max(largest_k, abs(num))

    return largest_k

# Input from the user
N = int(input("Enter the number of elements in the array: "))
A = []
print("Enter the elements of the array:")
for _ in range(N):
    element = int(input())
    A.append(element)

result = solution(A)
print("The largest integer K such that both K and -K exist in the array is:", result)