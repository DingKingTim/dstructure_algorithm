# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
hash 搜索
"""

HASH_SIZE = 20

HashDict = {}


class Hash(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v


def hash_key(k):
    """
    用于产生hash 的key
    """
    return k % HASH_SIZE


def insert(k, v):
    """
    插入
    """
    hash = Hash(k, v)
    key = hash_key(k)

    """
    hash 的key被占用，加1重新计算
    """
    while HashDict.has_key(key):
        key += 1
        key = key % HASH_SIZE

    """
    周到未被占用的hash，存储
    """
    HashDict[key] = hash

def search(k):
    hk = hash_key(k)

    while HashDict.has_key(hk):
        if HashDict[hk].key == k:
            return HashDict[hk].val
        hk += 1
        hk = hk % HASH_SIZE

    return None


if __name__ == "__main__":
    insert(3, 30)
    insert(4, 40)
    insert(3000, 50)
    insert(20, 60)
    insert(9, 70)

    print("search 3: ", search(3))
    print("search 4: ", search(4))
    print("search 3000: ", search(3000))
    print("search 20: ", search(20))
    print("search 9: ", search(9))


