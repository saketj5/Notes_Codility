### 1. Minimum Rounds to Complete All Tasks
# Task: Complete all tasks in rounds of 2 or 3 of the same type.
def minimum_rounds(tasks):
    from collections import Counter
    freq = Counter(tasks)
    rounds = 0
    for count in freq.values():
        if count == 1:
            return -1
        rounds += (count + 2) // 3
    return rounds