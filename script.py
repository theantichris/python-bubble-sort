def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

def bubble_sort(arr):
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            if arr[idx] > arr[idx + 1]:
                # swap elements
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    
nums = [5, 2, 9, 1, 5, 6]
print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
