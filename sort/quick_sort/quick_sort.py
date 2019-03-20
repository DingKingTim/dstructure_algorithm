# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


class QuickSort(object):

    def __init__(self):
        pass

    def sort(self, arr):
        self._ascend(arr, 0, len(arr)-1)

    def _ascend(self, arr, l, r):
        if l > r:
            return

        base = arr[l]
        left = l
        right = r

        while left != right:

            # 大于等于基数的要保证在右边
            while left < right and arr[right] > base:
                right -= 1

            # 小于等于基数的要保证在左边
            while left < right and arr[left] <= base:
                left += 1

            # 此时 arr[left] > base, arr[right] < base
            # 因此为了使得满足左边的比基数小,右边的比基数大
            # 交换左右两边
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                print(left, "  ", right, " :", arr)

        # 当 left 和 right 相遇时,遍历完毕,相遇的节点肯定是
        # arr[right] < base, 因此把小的放到左边,交换leift
        # 和基数对应的位置, 此时保证基数左边的比基数小,右边的
        # 比基数大
        arr[l], arr[left] = arr[left], arr[l]
        self._ascend(arr, l, left-1)
        self._ascend(arr, left+1, r)


if __name__ == "__main__":
    random.seed()
    arr = [random.randint(1, 100) for _ in range(10)]
    # arr = [3, 7, 2, 5, 9, 1, 6]

    print("Befor array: ", arr)
    quick_sort = QuickSort()
    quick_sort.sort(arr)
    print("After array: ", arr)


