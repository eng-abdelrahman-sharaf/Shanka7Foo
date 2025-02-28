def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swap:
            break
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] ,arr[i]
    return arr 

def insertion_sort(arr):
    for i in range(1,len(arr)):
        swap_index = i
        for j in range(i-1,-1,-1):
            if arr[j] <= arr[swap_index]:
                break
            arr[swap_index], arr[j] = arr[j], arr[swap_index]
            swap_index = j
    return arr
