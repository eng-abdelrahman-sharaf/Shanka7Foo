import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import random
import time
import matplotlib.pyplot as plt
from ass1.selection_sort import selection_sort
from ass1.insertion_sort import insertion_sort
from ass1.bubble_sort import bubble_sort
from Merge_Sort import merge_sort
from quick_sort import quicksort
from heapsort_and_kth import heap_sort
from heapsort_and_kth import find_kth
from Hybrid_Sort import hybrid_merge_insertion_sort

def compare_sorting_techniques(array_sizes):
    times = [[],[],[],[],[],[]]
    for array_size in array_sizes:
        random_array = [random.randint(0,int(50)) for i in range(array_size)]
        arr_1 = random_array.copy()
        arr_2 = random_array.copy()
        arr_3 = random_array.copy()
        arr_4 = random_array.copy()
        arr_5 = random_array.copy()
        arr_6 = random_array.copy()
        del random_array # free up memory

        t1 = time.time()
        arr_1 = selection_sort(arr_1)
        t1 = time.time() - t1

        t2 = time.time()
        arr_2 = insertion_sort(arr_2)
        t2 = time.time() - t2

        t3 = time.time()
        arr_3 = bubble_sort(arr_3)
        t3 = time.time() - t3

        t4 = time.time()
        arr_4 = merge_sort(arr_4)
        t4 = time.time() - t4

        t5 = time.time()
        arr_5 = quicksort(arr_5,0,len(arr_5)-1)
        t5 = time.time() - t5

        t6 = time.time()
        arr_6 = heap_sort(arr_6)
        t6 = time.time() - t6

        if(not(arr_1 == arr_2 and arr_2 == arr_3 == arr_4 == arr_5 == arr_6)):
            raise Exception(f"Sorting techniques are not equal\n\
                                        Selection : {arr_1} \n\
                                        Insertion : {arr_2} \n\
                                        Bubble    : {arr_3} \n\
                                        Merge     : {arr_4} \n\
                                        Quick     : {arr_5} \n\
                                        Heap      : {arr_6}")
        times[0].append(t1 * 1000)
        times[1].append(t2 * 1000)
        times[2].append(t3 * 1000)
        times[3].append(t4 * 1000)
        times[4].append(t5 * 1000)
        times[5].append(t6 *1000)
    return times


if __name__ == "__main__":
    sizes = [int(i) for i in[10,100,1000,2e3 , 5e3 , 8e3 , 10e3 , 15e3 , 20e3 , 50e3 , 100e3]]
    # sizes = [int(i) for i in [10,100,1000,2e3,5e3 ]]
    times = compare_sorting_techniques(sizes)

    plt.figure(figsize=(10, 6))
    plt.ylabel("Time (ms)")
    plt.xlabel("Array Size")
    plt.title("Sorting Algorithms - Linear Scale")

    plt.plot(sizes, times[0], label="Selection Sort")
    plt.plot(sizes, times[1], label="Insertion Sort")
    plt.plot(sizes, times[2], label="Bubble Sort")
    plt.plot(sizes, times[3], label="Merge Sort")
    plt.plot(sizes, times[4], label="Quick Sort")
    plt.plot(sizes, times[5], label="Heap Sort")

    plt.legend()
    plt.grid()
    plt.show()


    plt.figure(figsize=(10, 6))
    # plt.figure()
    plt.ylabel("time (ms)")
    plt.xlabel("size of array")
    plt.title("Sorting Algorithms - Logarithmic Scale")
    plt.ylabel("Time (ms)")
    plt.xlabel("Array Size")
    plt.xscale("log")

    plt.plot(sizes, times[0], label="Selection Sort")
    plt.plot(sizes, times[1], label="Insertion Sort")
    plt.plot(sizes, times[2], label="Bubble Sort")
    plt.plot(sizes, times[3], label="Merge Sort")
    plt.plot(sizes, times[4], label="Quick Sort")
    plt.plot(sizes, times[5], label="Heap Sort")

    plt.legend()
    plt.show()

    arr = [12, 11, 13, 5, 6, 7, 19, 21, 3, 8, 15]
    thresh = 6
    hybrid_merge_insertion_sort(arr, 0, len(arr) - 1, thresh)
    print(arr)

    arr_for_kth = [3,41,16,25,63,52,40]
    print(find_kth(arr_for_kth, 3,))
