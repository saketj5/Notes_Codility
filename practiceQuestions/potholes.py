def min_patches(S):
    n = len(S)
    patches = 0
    i = 0

    while i < n:
        if S[i] == 'x':  # Found a pothole
            patches += 1  # Apply a patch
            i += 3  # Move ahead by 3 as this patch covers 3 segments
        else:
            i += 1  # Move to the next segment

    return patches

# Example test cases
print(min_patches(".x..x"))        # Output: 2
print(min_patches("x.xxxxx.x."))   # Output: 3
print(min_patches("xx.xxx.."))     # Output: 2
print(min_patches("xxxx"))         # Output: 2
