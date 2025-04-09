def minimum_deletions(S: str) -> int:
    n = len(S)

    totalA = S.count('A')
    minDeletions = float('inf')
    countB = 0
    remainingA = totalA

    for c in S:
        if c == 'A':
            remainingA -= 1
        else:  # c == 'B'
            countB += 1

        deletions = countB + remainingA
        minDeletions = min(minDeletions, deletions)

    minDeletions = min(minDeletions, totalA, n - totalA)
    return minDeletions

# Test cases
if __name__ == "__main__":
    print("Minimum deletions for 'BAAABAB':", minimum_deletions("BAAABAB"))  # Expected: 2
    print("Minimum deletions for 'BBABAA':", minimum_deletions("BBABAA"))    # Expected: 3
    print("Minimum deletions for 'AABBBB':", minimum_deletions("AABBBB"))    # Expected: 0
