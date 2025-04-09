#Move first letter of S to the end

def count_matching_rotations(S):
    N = len(S)
    count = 0
    
    for i in range(N):
        if S[i] == S[(i - 1) % N]:  # Compare rotated first and last letters
            count += 1
    
    return count

# Example test cases
print(count_matching_rotations("abbaa"))  # Output: 3
print(count_matching_rotations("aaaa"))   # Output: 4
print(count_matching_rotations("abab"))   # Output: 0
