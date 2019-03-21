# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinarySearch(object):
    """
    二分查找基于已排序好的队列中寻找
    """

    def __init__(self):
        pass

    @classmethod
    def binary_mid(cls, l, h):
        """
        普通二分查找
        :param l:
        :param h:
        :return:
        """
        return l + ((h - l) >> 1)

    @classmethod
    def interpolation_mid(cls, arr, l, h, match):
        """
        插值查找
        :param arr:
        :param l:
        :param h:
        :param match:
        :return:
        """
        interpolate = (h - l) / (arr[h] - arr[l])
        return l + (match - arr[l]) * interpolate

    @classmethod
    def interpolate_search(cls, arr, match):
        """
        插值二分搜索
        :param arr:
        :param match:
        :return:
        """
        size = len(arr)
        l, h = 0, size

        while l < h:
            mid = cls.interpolation_mid(arr, l, h, match)

            if arr[mid] == match:
                return mid
            elif arr[mid] < match:
                l = mid
            else:
                h = mid
        return None

    @classmethod
    def binary_search(cls, arr, match):
        """
        普通二分搜索
        :param arr:
        :param match:
        :return:
        """
        size = len(arr)
        l, h = 0, size

        while l < h:
            mid = cls.binary_mid(l, h)

            if arr[mid] == match:
                return mid
            elif arr[mid] < match:
                l = mid
            else:
                h = mid
        return None

    @classmethod
    def search(cls, arr, match, interpolate=False):
        if interpolate:
            return cls.interpolate_search(arr, match)
        else:
            return cls.binary_search(arr, match)


if __name__ == "__main__":
    arr = [13, 31, 71, 75, 78, 78, 83, 90, 97, 97]

    print("array: ", arr, arr[7])
    binary_search = BinarySearch()
    index = binary_search.search(arr, arr[7])
    print("find index: ", index)
