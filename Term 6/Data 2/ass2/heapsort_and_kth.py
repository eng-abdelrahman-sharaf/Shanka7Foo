import random 

def merge(a1, a2):
    result = []
    i1 = i2 = 0
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            result.append(a1[i1])
            i1 += 1
        else:
            result.append(a2[i2])
            i2 += 1
    while i1 < len(a1):
        result.append(a1[i1])
        i1 += 1
    while i2 < len(a2):
        result.append(a2[i2])
        i2 += 1
    return result


def merge_sort(array):
    if len(array) == 1: return array
    a1 = array[:len(array) // 2]
    a2 = array[len(array) // 2:]

    a1 = merge_sort(a1)
    a2 = merge_sort(a2)
    return merge(a1, a2)

def quick_sort(array, start=0, end=None):
    if end == None:
        end = len(array) - 1
    if start >= end:
        return
    i = start-1
    pivot_idx = random.randint(start, end)
    array[pivot_idx], array[end] = array[end], array[pivot_idx]
    pivot_idx = end
    for j in range(start,end):
        if array[j] <= array[pivot_idx]:
            i += 1
            array[i], array[j] = array[j], array[i]
    i+=1
    array[i], array[pivot_idx] = array[pivot_idx], array[i]
    pivot_idx = i
    quick_sort(array, start, pivot_idx-1)
    quick_sort(array, pivot_idx+1, end)


def max_heapify(array , index, heapSize):
    l = 2*index+1
    r = 2*index+2
    largest = index

    if l<heapSize and array[l] > array[index]:
        largest = l

    if r < heapSize and array[r] > array[largest]:
        largest = r
    
    if largest != index:
        array[largest] , array[index] = array[index] , array[largest]
        max_heapify(array , largest , heapSize)
    

def build_max_heap(array):
    parent = (len(array))//2 - 1
    for idx in range(parent,-1,-1):
        max_heapify(array,idx,len(array))


def heap_sort(array):
    build_max_heap(array)
    for heap_size in range(len(array) , 1 , -1):
        array[0] , array[heap_size-1] = array[heap_size-1] , array[0]
        max_heapify(array,0,heap_size-1)

def find_kth(array,k,start=0,end=None):
    i = start-1
    j = start
    if end == None:
        end = len(array)-1
    pivot_index = random.randint(start,end)
    array[pivot_index], array[end] = array[end], array[pivot_index]
    pivot_index = end

    for j in range(start,end):
        if array[j] <= array[pivot_index]:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[pivot_index] = array[pivot_index], array[i+1]
    pivot_index = i+1
    if k-1 == pivot_index:
        return array[pivot_index]
    elif k-1 < pivot_index:
        return find_kth(array,k,start,pivot_index-1)
    else:
        return find_kth(array,k,pivot_index+1,end)

if __name__ == "__main__":
    array = [random.randint(1,100) for i in range(100)]
    a1 =  array.copy()
    a2 = array.copy()
    a3 = array.copy()
    a4 = array.copy()
    a1 = merge_sort(a1)
    quick_sort(a2)
    heap_sort(a3)
    for i in range(1, 101):
        sorted_arr = sorted(array)
        if find_kth(a4,i) != sorted_arr[i-1]:
            print("Error")
    # sorting is correct
    print(a1 == a2 == a3)