# Kayak Palindrome
def make_palindrome(S):
    S = list(S)  # Convert to list for mutability
    N = len(S)
    
    left, right = 0, N - 1
    
    while left <= right:
        if S[left] == S[right]:  # Both are same or both are '?'
            if S[left] == '?':
                S[left] = S[right] = 'a'  # Default replacement
        elif S[left] == '?':  
            S[left] = S[right]  # Mirror right to left
        elif S[right] == '?':  
            S[right] = S[left]  # Mirror left to right
        else:
            return "NO"  # Mismatch found
        
        left += 1
        right -= 1
    
    return "".join(S)

# Example test cases
print(make_palindrome("?ab??a"))  # Output: "aabbaa"
print(make_palindrome("bab??a"))  # Output: "NO"
print(make_palindrome("?a?"))     # Output: "aaa" or "zaz"
