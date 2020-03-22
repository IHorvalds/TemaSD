from bubble_sort import bubble_sort
from count_sort import count_sort
from merge_sort import merge_sort
from quicksort import quick_sort, quicksort_inplace
from radix_sort import radix_sort
from timsort import insert_sort
from timsort import tim_sort
from tests import test, averages


if __name__ == "__main__":
    try:
        nr_of_elements = int(float(input("Number of elements in scientific notaion: ")))
    except:
        nr_of_elements = 10**3

    try:
        max_element = int(float(input("Maximum element in scientific notation: ")))
    except:
        max_element = 10**6

    sorts = [bubble_sort, count_sort, insert_sort, merge_sort, quick_sort, quicksort_inplace, radix_sort, tim_sort, sorted]

        

    nr_of_tests = 8
    for _ in range(nr_of_tests):
        test(sorts, nr_of_elements, max_element, 0, nr_of_elements)
    print()
    with open("results_smaller_sample.txt", "w") as f:
        f.write("Nr of tests: " + str(nr_of_tests) + "\n")
        f.write("Nr of elements: " + str(nr_of_elements) + "\n")
        f.write("Maximum elements: " + str(max_element) + "\n\n")
        for name, time in averages.items():
            f.write(name + ": " + str((time/nr_of_tests) * 1000) + " ms\n")
