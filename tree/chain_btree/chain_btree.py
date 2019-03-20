# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    """
    树的节点
    data:  存储数据
    left:  存储左子树
    right: 存储右子树
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ChainBinaryTree(object):
    """
    链式二叉树: 将给定序列按照原来序列中的顺序存储到树中, 从上到下从左到右依次存储
    特     征: 序列中的从0开始,后面的 2n+1 存储到左子树, 2n+2 存储到右子树
    """
    def __init__(self):
        self.tree = None

    def save(self, arr):
        """
        数组存储到链式二叉树中
        :param arr: 输入序列
        :return:
        """
        self.tree = self._save(arr, len(arr), 0)

    def _save(self, arr, size, pos):
        """
        :param arr: 输入序列
        :param size: 输入序列长度, 保证序列不越界
        :param pos: 当前节点的序号
        :return: 返回节点
        """

        if pos < size:
            # 存储节点
            node = Node(arr[pos])

            # 序列中当前节点的 2n + 1 存储到左子树
            node.left = self._save(arr, size, pos * 2 + 1)

            # 序列中当前节点的 2n + 1 存储到右子树
            node.right = self._save(arr, size, pos * 2 + 2)

            # 返回当前节点
            return node
        return None

    def len(self):
        return self._len(self.tree)

    def _len(self, tr):
        """
        递归求解序列的长度
        :param tr: 输入树
        :return: 返回树的长度
        """
        if tr is None:
            return 0

        l_size = self._len(tr.left)
        r_size = self._len(tr.right)
        return 1 + l_size + r_size

    def array(self):
        """
        链式二叉树转换为序列(数组)
        :return:
        """
        size = self.len()
        array = [0 for _ in range(size)]
        self._array(self.tree, array, 0)
        return array

    def _array(self, tr, arr, pos):
        """
        原则: 左子树存储到序列的索引 2n + 1处, 右子树存储到序列的索引 2n + 2处
        :param tr:  输入树节点
        :param arr: 序列
        :param pos: 序列当前的位置
        :return:
        """

        if tr is None:
            return

        arr[pos] = tr.data
        # 左子树存储到序列的索引 2n + 1 的位置
        self._array(tr.left, arr, pos * 2 + 1)

        # 右子树存储到序列的索引 2n + 2 的位置
        self._array(tr.right, arr, pos * 2 + 2)

    def pre_travel(self):
        arr = list()
        self._pre_travel(self.tree, arr)
        return arr

    def _pre_travel(self, tr, arr):
        """
        先序遍历: 跟节点 ----> 左子树 ----> 右子树
        :param tr:  输入节点
        :param arr: 用于存储输出节点
        :return:
        """
        if tr is None:
            return

        arr.append(tr.data)
        self._pre_travel(tr.left, arr)
        self._pre_travel(tr.right, arr)

    def mid_travel(self):
        arr = list()
        self._mid_travel(self.tree, arr)
        return arr

    def _mid_travel(self, tr, arr):
        """
        中序遍历:    左子树 ---> 跟 ---> 右子树
        :param tr:  输入节点
        :param arr: 保存输出节点
        :return:
        """
        if tr is None:
            return
        self._mid_travel(tr.left, arr)
        arr.append(tr.data)
        self._mid_travel(tr.right, arr)

    def post_travel(self):
        arr = list()
        self._post_travel(self.tree, arr)
        return arr

    def _post_travel(self, tr, arr):
        """
        后序遍历:    左子树 ---> 右子树 ---> 跟
        :param tr:  输入节点
        :param arr: 保存输出节点
        :return:
        """
        if tr is None:
            return
        self._post_travel(tr.left, arr)
        self._post_travel(tr.right, arr)
        arr.append(tr.data)

    def lr_reverse(self):
        self._lr_reverse(self.tree)

    def _lr_reverse(self, tr):
        """
        翻转左右子树
        :param tr:
        :return:
        """
        if tr:
            tr.left, tr.right = tr.right, tr.left
            self._lr_reverse(tr.left)
            self._lr_reverse(tr.right)


if __name__ == "__main__":
    arr  = [3, 8, 9, 10, 1, 2, 7, 22, 34, 10, 2]
    chain_tree = ChainBinaryTree()

    print("src   array is       :", arr)
    chain_tree.save(arr)
    print("chain tree size      :", chain_tree.len())
    print("chain tree pre       :", chain_tree.pre_travel())
    print("chain tree mid       :", chain_tree.mid_travel())
    print("chain tree post      :", chain_tree.post_travel())
    print("---------------------------------------------------")
    print("array is             :", chain_tree.array())
    print("---------------------------------------------------")
    chain_tree.lr_reverse()
    print("chain tree reverse pre       :", chain_tree.pre_travel())
    print("chain tree reverse mid       :", chain_tree.mid_travel())
    print("chain tree reverse post      :", chain_tree.post_travel())

