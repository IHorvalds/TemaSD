from bubble_sort import bubble_sort
from count_sort import count_sort
from merge_sort import merge_sort
from quicksort import quick_sort
from radix_sort import radix_sort
from timsort import insert_sort
from timsort import tim_sort
from tests import test


if __name__ == "__main__":
    nr_of_elements = int(float(input("Number of elements in scientific notaion: ")))
    max_element = int(float(input("Maximum element in scientific notation: ")))

    sorts = [bubble_sort, count_sort, insert_sort, merge_sort, quick_sort, radix_sort, tim_sort]

    test(sorts, nr_of_elements, max_element, 0, nr_of_elements)
