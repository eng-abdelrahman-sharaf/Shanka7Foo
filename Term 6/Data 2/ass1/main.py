import random
import time
import matplotlib.pyplot as plt
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort

def compare_sorting_techniques(array_sizes):
    times = [[],[],[]]
    for array_size in array_sizes:
        random_array = [random.randint(0,int(50)) for i in range(array_size)]
        arr_1 = random_array.copy()
        arr_2 = random_array.copy()
        arr_3 = random_array.copy()
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
        if(not(arr_1 == arr_2 and arr_2 == arr_3)):
            raise Exception(f"Sorting techniques are not equal\n\
                            arr 1 : {arr_1} \n\
                            arr 2 : {arr_2} \n\
                            arr 3 : {arr_3}")
        times[0].append(t1)
        times[1].append(t2)
        times[2].append(t3)
    return times


if __name__ == "__main__":
    plt.figure()
    sizes = [int(i) for i in [10,100,1000,2e3 ]]
    # sizes = [int(i) for i in[10,100,1000,2e3 , 5e3 , 8e3]]
    times = compare_sorting_techniques(sizes)
    plt.ylabel("time (s)")
    plt.xlabel("size of array")
    plt.plot(sizes, times[0], label="Selection Sort")
    plt.plot(sizes, times[1], label="Insertion Sort")
    plt.plot(sizes, times[2], label="Bubble Sort")
    plt.legend()
    plt.show()

