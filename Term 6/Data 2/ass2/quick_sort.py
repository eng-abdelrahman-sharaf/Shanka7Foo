

def max_heapify(arr,idx,heap_size):
    l = idx*2 +1
    r = idx*2 + 2
    largest = idx
    if  r < heap_size and arr[l] > arr[r]:
        largest = l
    elif l < heap_size and arr[l] > arr[largest]:
        largest = r
    if  largest != idx:
        arr[idx],arr[largest] = arr[largest],arr[idx]
        max_heapify(arr,largest,heap_size)

def heapsort(arr):
    n = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        max_heapify(arr, i , n)
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        max_heapify(arr,0,i)
    return arr


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right


def quicksort(arr, low , high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

    return arr





