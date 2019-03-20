# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

"""
从无序序列中找出最大的 K 个数

堆排序:

   大堆: 从上而下依次减小, 保证顶部最大
   小堆: 从上而下依次增大, 保证顶部最小

分析:

   既然是 top k, 那我们建立一个含有K 个元素的小堆即可,只要输入元素比堆顶大, 怎替换对顶然后调整堆
"""


def ascend_adjust(arr, pos, size):
    """
    小堆调整基本算法: 父节点小于子节点
    :param arr: 输入序列
    :param pos: 当前要调整的节点
    :param size: 堆的大小
    :return:
    """
    father = pos
    son = (father << 1) + 1

    while son < size:
        # 取小的那个儿子比较
        if son + 1 < size and arr[son+1] < arr[son]:
            son += 1

        # 父节点小于子节点停止
        if arr[father] <= arr[son]:
            return

        # 调整顺序
        arr[father], arr[son] = arr[son], arr[father]
        father = son
        son = (father << 1) + 1


def top_k(arr, k):
    father_nodes = (k >> 1) - 1

    # 构建k个元素的堆, 主要是保证小堆成立
    while father_nodes >= 0:
        ascend_adjust(arr, father_nodes, k)
        father_nodes -= 1

    # 从第k个元素开始,逐个比较,
    # 若第i个元素大于顶元素,则直接
    # 替换顶元素,然后调整堆
    i = k
    while i < len(arr):
        if arr[i] > arr[0]:
            arr[0] = arr[i]
            ascend_adjust(arr, 0, k)
        i += 1

    # 返回top k
    return arr[:k]

if __name__ == "__main__":
    random.seed()
    arr = [random.randint(1, 100) for _ in range(50)]
    print("before array: ", arr)
    print("top 5: ", top_k(arr, 5))
