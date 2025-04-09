### 4. Schedule Maximum Number of Meetings
# Task: Schedule maximum non-overlapping meetings.
def max_meetings(start, end):
    meetings = sorted(zip(start, end), key=lambda x: x[1])
    count, current_end = 0, 0
    for s, e in meetings:
        if s >= current_end:
            count += 1
            current_end = e
    return count