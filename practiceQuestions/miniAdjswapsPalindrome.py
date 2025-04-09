### 3. Minimum Adjacent Swaps to Make a Palindrome
# Task: Convert string to palindrome using adjacent swaps.
def min_swaps_to_palindrome(s):
    from collections import Counter
    if sum(v % 2 for v in Counter(s).values()) > 1:
        return -1

    s = list(s)
    swaps = 0
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            k = j
            while k > i and s[k] != s[i]:
                k -= 1
            if k == i:
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1
            else:
                while k < j:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    swaps += 1
                    k += 1
                i += 1
                j -= 1
    return swaps