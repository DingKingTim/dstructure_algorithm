# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


class BubleSort(object):

    def __init__(self):
        pass

    def sort(self, arr):
        size = len(arr)

        # 冒泡排序总共进行 n - 1 次
        for i in range(1, size):
            # 把最大的交换到最后
            for j in range(size-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    random.seed()
    arr = [random.randint(1, 100) for _ in range(100)]

    print("Befor array: ", arr)
    bubble_sort = BubleSort()
    bubble_sort.sort(arr)
    print("After array: ", arr)
