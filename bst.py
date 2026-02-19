import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)

BinTree = Union["Node", None]

class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    BTree : BinTree

def lookup_helper(x: Any, bst: BinTree, comes_before: Callable[[Any, Any], bool]) -> bool:
    if bst is None:
        return False
    elif bst.value == x:
        return True
    elif comes_before(x, bst.value):
        return lookup_helper(x, bst.left, comes_before)
    elif comes_before(bst.value, x):
        return lookup_helper(x, bst.right, comes_before)
    
def lookup(x: Any, bst: BinarySearchTree) -> bool:
    return lookup_helper(x, bst.BTree, bst.comes_before) 

def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    output = inserthelper(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, output)

def inserthelper(btree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
    match btree:
        case None:
            return Node(value, None, None)
        case Node(value=v, left=l, right=r):
            if (not comes_before(value, v)) and (not comes_before(v, value)):
                return btree
            if comes_before(value, v):
                return Node(v, inserthelper(l, value, comes_before), r)
            else:
                return Node(v, l, inserthelper(r, value, comes_before))