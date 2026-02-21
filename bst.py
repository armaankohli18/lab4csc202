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

def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    output = inserthelper(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, output) 

def delete (bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    if not lookup(value, bst):
        return bst
    else:
        output = delete_helper(bst.BTree, value, bst.comes_before)
        return BinarySearchTree(bst.comes_before, output)

def delete_helper(btree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        match btree:
            case None:
                return None
            case Node(value=v, left=l, right=r):
                if (not comes_before(value, v)) and (not comes_before(v, value)):
                    if l is None and r is None:
                        return None
                    elif l is not None and r is not None:
                        # find the smallest value in the right subtree
                        smallest = r
                        while smallest.left is not None:
                            smallest = smallest.left
                        # replace the value of the current node with the smallest value
                        new_value = smallest.value
                        # delete the smallest value from the right subtree
                        new_right = delete_helper(r, new_value, comes_before)
                        return Node(new_value, l, new_right)
                    else:
                        return l if l is not None else r
                elif comes_before(value, v):
                    return Node(v, delete_helper(l, value, comes_before), r)
                else:
                    return Node(v, l, delete_helper(r, value, comes_before))