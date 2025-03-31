# There is a road consisting of N segments, numbered from 0 to N−1, represented by a string S. Segment S[K] of the road may contain a pothole, denoted by a single uppercase "x" character, or may be a good segment without any potholes, denoted by a single dot, ".".

# For example, string ".x..x" means that there are two potholes in total in the road: one is located in segment S[1] and one in segment S[4]. All other segments are good. The road fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes located within each of these segments. Good or already repaired segments remain good after patching them.

# Your task is to compute the minimum number of patches required to repair all the potholes in the road.

# Write a function:

# int solution(string &S);
# that, given a string S of length N, returns the minimum number of patches required to repair all the potholes.

# Examples:
# Given S=".x..x", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 2-4.
# Given S="x.xxxxx.x.", your function should return 3. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
# Given S="xx.xxx..", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 3-5.
# Given S="xxxx", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 1-3.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [3..100,000);
# string S consists only of the characters "." and/or "x".

# Solve this question in python


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
