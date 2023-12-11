#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for a in range(n):
        for k in range(0, n - a - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]

#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [h for h in arr if h < pivot]
    middle = [h for h in arr if h == pivot]
    right = [h for h in arr if h > pivot]
    return quick_sort(left) + middle + quick_sort(right)

unsorted_list = [14, 27, 8, -42, 11, 35, -9, 56, 23]

#using Bubble Sort
bubble_sort_result = unsorted_list.copy()
bubble_sort(bubble_sort_result)
print("Bubble Sort Result:", bubble_sort_result)
#The Output will be:[-42, -9, 8, 11, 14, 23, 27, 35, 56]

#using Quick Sort
quick_sort_result = quick_sort(unsorted_list.copy())
print("Quick Sort Result:", quick_sort_result)
#The Output:[-42, -9, 8, 9, 11, 14, 23, 27, 35, 56]

# Complexity Classes (Bubble Sort): O(n^2)
# Complexity Classes (Quick Sort): O(n log n)
