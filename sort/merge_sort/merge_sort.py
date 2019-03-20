# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


class MergeSort(object):

    def __init__(self):
        pass

    def sort(self, arr):
        return self._split(arr)

    def _merge(self, la, ra):
        """
        两个数组从最左边开始,比较合并
        [3, 8, 9]   [2, 6]

        1. l < len(la) and r < len(ra): [2, 3, 6]
        2. l<len(la): [2, 3, 6, 8, 9]

        :param la: 数组1
        :param ra: 数组2
        :return: 合并后的数组
        """
        l = 0
        r = 0

        # 合并占用额外的空间
        result = []

        while l < len(la) and r < len(ra):
            if la[l] < ra[r]:
                result.append(la[l])
                l += 1
            else:
                result.append(ra[r])
                r += 1

        # 判断是否有剩余,放入剩余的元素
        while l < len(la):
            result.append(la[l])
            l += 1

        while r < len(ra):
            result.append(ra[r])
            r += 1

        return result

    def _split(self, arr):
        """
        数组拆分,从中间开始拆分,拆分规则如下:
        mid = len(arr) / 2

        :param arr:
        :return:
        """
        size = len(arr)
        if size == 1:
            return arr

        mid = (size >> 1)
        la = self._split(arr[:mid])
        ra = self._split(arr[mid:])
        return self._merge(la, ra)


if __name__ == "__main__":
    random.seed()
    arr = [random.randint(0, 500) for _ in range(20)]
    print("Before Sort: ", arr)
    merge_sort = MergeSort()
    res = merge_sort.sort(arr)
    print("After Sort: ", res)

