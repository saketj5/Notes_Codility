
def min_rooms_required(A):
    A.sort()  # Sort guests based on their tolerance level
    rooms = 0
    i = 0
    N = len(A)
    
    while i < N:
        size = A[i]  # Room should accommodate at most 'size' guests
        rooms += 1   # Open a new room
        i += size    # Move 'size' guests forward
        
    return rooms

# Example test cases
print(min_rooms_required([1, 1, 1, 1, 1]))   # Output: 5
print(min_rooms_required([2, 1, 4]))         # Output: 2
print(min_rooms_required([2, 7, 2, 9, 8]))   # Output: 2
print(min_rooms_required([7, 3, 1, 1, 4, 5, 4, 9]))  # Output: 4
