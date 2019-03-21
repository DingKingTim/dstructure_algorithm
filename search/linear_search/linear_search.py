# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def linear_search(arr, n):
    """
    线性搜索
    :param arr:
    :param n:
    :return:
    """
    for idx, item in enumerate(arr):
        if item == n:
            return idx

    return None


if __name__ == "__main__":
    arr = [1, 5, 9, 6, 4, 3]
    print("search res: ", linear_search(arr, 3))
