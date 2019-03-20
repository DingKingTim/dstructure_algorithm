# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

class SelectSort(object):

    def __init__(self):
        pass

    def sort(self, arr):
        self._sort(arr)

    def _sort(self, arr):

        for i in range(len(arr)):
            mi = i
            j = i + 1

            while j < len(arr):
                if arr[j] < arr[mi]:
                    mi = j
                j += 1

            arr[mi], arr[i] = arr[i], arr[mi]


if __name__ == "__main__":
    random.seed()
    arr = [random.randint(1, 100) for _ in range(10)]
    # arr = [3, 7, 2, 5, 9, 1, 6]

    print("Befor array: ", arr)
    select_sort = SelectSort()
    select_sort.sort(arr)
    print("After array: ", arr)




