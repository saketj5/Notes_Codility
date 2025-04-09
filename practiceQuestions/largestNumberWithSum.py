### 6. Largest Number with Sum of Digits <= K
# Task: Find largest number <= 10^18 with digit sum <= K.
def largest_with_digit_sum(k):
    res = []
    while k > 9:
        res.append('9')
        k -= 9
    if k:
        res.append(str(k))
    return int(''.join(res))
