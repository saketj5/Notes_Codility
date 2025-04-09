### 7. Fix the Road with Limited Resources
# Task: Fix all potholes ('x') with K patches of length 3.
def can_fix_potholes(s, k):
    s = list(s)
    i = 0
    patches = 0
    while i < len(s):
        if s[i] == 'x':
            patches += 1
            i += 3
        else:
            i += 1
    return patches <= k
