### 10. Distribute Candy Fairly
# Task: Find max candies each child can get given total.
def max_candy_per_child(n_children, total_candies):
    low, high = 0, total_candies
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * n_children <= total_candies:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best