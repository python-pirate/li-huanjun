from demo import *
import random

def test_select_sort():
    for x in range(10000):
        arr = [random.randint(10, 99) for _ in range(10)]

        select_sort(arr)

        i = 0
        while i < len(arr) - 1:
            assert(arr[i] >= arr[i + 1])
            i += 1
