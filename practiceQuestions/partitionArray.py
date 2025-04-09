### 8. Partition Array into Equal Sum
# Task: Check if array can be split into 2 or 3 equal-sum parts.
def can_partition(arr):
    total = sum(arr)
    if total % 2 == 0:
        target, curr = total // 2, 0
        for num in arr:
            curr += num
            if curr == target:
                return True
    if total % 3 == 0:
        target, curr, count = total // 3, 0, 0
        for num in arr:
            curr += num
            if curr == target:
                curr = 0
                count += 1
        return count >= 3
    return False