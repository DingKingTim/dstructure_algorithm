# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


class InsertSort(object):

    def __init__(self):
        pass

    def sort(self, arr):
        return self._sort(arr)

    def _sort(self, arr):
        size = len(arr)
        i = 0

        # 开始接扑克, 接到两张以上时
        # 和前面的依次比较,保证每次
        # 接的几张牌都是排好序的
        while i < size:
            cur = arr[i]
            pos = i

            # 和前面的牌进行比较
            while pos > 0 and arr[pos-1] > cur:
                arr[pos] = arr[pos-1]
                pos -= 1

            arr[pos] = cur
            i += 1
        return arr


if __name__ == "__main__":
    random.seed()
    arr = [random.randint(0, 500) for _ in range(20)]
    print("Before Sort: ", arr)
    insert_sort = InsertSort()
    res = insert_sort.sort(arr)
    print("After Sort: ", res)
