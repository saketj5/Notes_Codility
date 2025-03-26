# Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Python Program to reverse an array using inbuilt methods

# function to reverse an array
def reverse_array(arr):
    arr.reverse()


if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverse_array(arr)

    print(" ".join(map(str, arr)))
