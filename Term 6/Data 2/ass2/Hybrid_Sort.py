
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def hybrid_merge_insertion_sort(arr, left, right, threshold):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
        return

    if left < right:
        mid = (left + right) // 2
        hybrid_merge_insertion_sort(arr, left, mid, threshold)
        hybrid_merge_insertion_sort(arr, mid + 1, right, threshold)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 19, 21, 3, 8, 15]
    thresh = 6
    hybrid_merge_insertion_sort(arr, 0, len(arr) - 1, thresh)
    print(arr)
