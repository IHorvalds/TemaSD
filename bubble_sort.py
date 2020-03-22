from tests import test

def bubble_sort(v, *args):
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[j] < v[i]:
                v[i], v[j] = v[j], v[i]
    return v


if __name__ == "__main__":
    # test(bubble_sort, 10**5, 10**3)
    test(bubble_sort, 10**6, 10**4)