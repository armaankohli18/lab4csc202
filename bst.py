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
