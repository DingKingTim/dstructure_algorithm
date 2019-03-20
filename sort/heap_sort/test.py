# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from heap_sort import HeapSort
from datetime import datetime


def ascend_sort():
    heap_sort = HeapSort()
    arr = [3, 8, 9, 10, 1, 2, 7, 22, 34, 10, 2]
    print("Before Sort Array: ", arr)
    start = datetime.now()
    heap_sort.big_heap_sort(arr)
    end = datetime.now() - start
    print("After Sort Array: ", arr)
    print("Heap Sort Lost Time: ", end)


def decend_sort():
    heap_sort = HeapSort()
    arr = [3, 8, 9, 10, 1, 2, 7, 22, 34, 10, 2]
    print("Before Sort Array: ", arr)
    start = datetime.now()
    heap_sort.small_heap_sort(arr)
    end = datetime.now() - start
    print("After Sort Array: ", arr)
    print("Heap Sort Lost Time: ", end)

if __name__ == "__main__":
    ascend_sort()
    print()
    print()
    decend_sort()
