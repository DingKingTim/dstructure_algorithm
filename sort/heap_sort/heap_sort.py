# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class HeapSort(object):

    def __init__(self):
        pass

    def ascend_heap_adjust(self, arr, pos, end):
        """
        小堆调整, 子节点比父节点大, 从上到下升
        :param arr:
        :param pos:
        :param end:
        :return:
        """
        father = pos
        son = (father << 1) + 1

        while son < end:
            if son + 1 < end and arr[son+1] < arr[son]:
                son += 1

            if arr[father] <= arr[son]:
                return

            arr[father], arr[son] = arr[son], arr[father]
            father = son
            son = (father << 1) + 1

    def descend_heap_adjust(self, arr, pos, end):
        """
        根节点比子节点大, 从上到下下降
        :param arr:
        :param pos:
        :param end:
        :return:
        """

        father = pos

        # 当前节点的子节点: 2 * pos + 1
        son = (father << 1) + 1

        while son < end:
            # 首先比较两个子节点,去最大子节点的索引
            if son + 1 < end and arr[son+1] > arr[son]:
                son += 1

            # 判断儿子是否小于父亲
            if arr[son] <= arr[father]:
                return

            # 儿子大于父亲,交换
            arr[son], arr[father] = arr[father], arr[son]

            #交换之后,儿子的数据被存储到了父亲,我们还要检测
            #交换之后有没偶满足儿子节点大于孙子节点,设置新的
            #父亲节点,继续检测
            father = son
            son = (father << 1) + 1

    def big_heap_sort(self, arr):
        size = len(arr)

        """
        对于给定序列,索引【0, ..., size/2 -1]是我们的父节点
        """
        father_nodes = (size >> 1) - 1
        print("father nodes: ", father_nodes)

        """
        从最后一个父节点开始,也就是从下往上调整,保证下面的子节点
        比他的父节点小, 这轮结束保证了父节点从上往下数据是递减的
        那么根节点最大
        """
        while father_nodes >= 0:
            self.descend_heap_adjust(arr, father_nodes, size)
            print("father nodes: ", father_nodes, arr)
            father_nodes -= 1

        print(arr)
        i = size - 1
        while i > 0:
            """
            调整后每次都是根节点最大,交换根节点和最后一个节点,相当于
            把最大的放到了最后面,然后把最后一个节点排除在调整的范围
            内,再次调整
            """
            arr[0], arr[i] = arr[i], arr[0]

            self.descend_heap_adjust(arr, 0, i - 1)
            i -= 1

    def small_heap_sort(self, arr):
        """

        :param arr:
        :return:
        """
        size = len(arr)

        """
        对于给定序列,索引【0, ..., size/2 -1]是我们的父节点
        """
        father_nodes = (size >> 1) - 1

        """
        从最后一个父节点开始,也就是从下往上调整,保证下面的子节点
        比他的父节点小, 这轮结束保证了父节点从上往下数据是递减的
        那么根节点最大
        """
        while father_nodes >= 0:
            self.ascend_heap_adjust(arr, father_nodes, size)
            father_nodes -= 1

        i = size - 1
        while i > 0:
            """
            调整后每次都是根节点最大,交换根节点和最后一个节点,相当于
            把最大的放到了最后面,然后把最后一个节点排除在调整的范围
            内,再次调整
            """
            arr[0], arr[i] = arr[i], arr[0]
            self.ascend_heap_adjust(arr, 0, i - 1)
            i -= 1




