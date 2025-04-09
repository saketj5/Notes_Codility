def max_digit_sum_below(S: str) -> str:
    original = int(S)
    max_sum = sum(int(d) for d in str(original - 1))
    best_number = str(original - 1)

    for i in range(len(S)):
        if S[i] == '0':
            continue

        prefix = S[:i]
        reduced_digit = str(int(S[i]) - 1)
        suffix = '9' * (len(S) - i - 1)
        candidate = prefix + reduced_digit + suffix

        # Strip leading zeros, make sure it's still < original
        if candidate.lstrip('0') == '':
            continue

        candidate_int = int(candidate)
        if candidate_int >= original:
            continue

        digit_sum = sum(int(d) for d in candidate)
        if digit_sum > max_sum:
            max_sum = digit_sum
            best_number = candidate

    return best_number


# Example usage
print(max_digit_sum_below("899"))   # Expected: "889" or "898" (sum of 25)
print(max_digit_sum_below("10"))    # Expected: "9"
print(max_digit_sum_below("98"))    # Expected: "89"
print(max_digit_sum_below("1000"))  # Expected: "999"
