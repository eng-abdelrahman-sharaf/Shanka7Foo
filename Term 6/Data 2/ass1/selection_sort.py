def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):
    for i in range(len(array)):
        j=i
        while j>0 and array[j-1]>array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == '__main__':
    print(bubble_sort([7,6,2,-3,8,4,2,0,6]))
    print(selection_sort([7,6,2,-3,8,4,2,0,6]))
    print(insertion_sort([7,6,2,-3,8,4,2,0,6]))
