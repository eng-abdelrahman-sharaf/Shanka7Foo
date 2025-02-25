def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j >0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            print(arr)
            j -= 1
    return arr


def elekhtyar_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]

    return arr


def alfoka3a_sort (arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr





print(alfoka3a_sort([8,10,44,12,-6]))
