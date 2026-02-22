import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)

BinTree : TypeAlias = Union["Node", None]

@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree : BinTree

def lookup_helper(x: Any, bst: BinTree, comes_before: Callable[[Any, Any], bool]) -> bool:
    match bst:
        case None:
            return False
        case Node(v, l, r):
            if (not comes_before(x, v)) and (not comes_before(v, x)):
                return True
            if comes_before(x, v):
               return lookup_helper(x, l, comes_before)
            else:
                return lookup_helper(x, r, comes_before)
            
def lookup(x: Any, bst: BinarySearchTree) -> bool:
    return lookup_helper(x, bst.tree, bst.comes_before) 

def inserthelper(btree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
    match btree:
        case None:
            return Node(value, None, None)
        case Node(v, l, r):
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
    output = delete_helper(bst.tree, value, bst.comes_before)
    return BinarySearchTree(bst.comes_before, output)

def delete_helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        match tree:
            case None:
                return None
            case Node(v, l, r):
                if (not comes_before(value, v)) and (not comes_before(v, value)):
                    if l is None and r is None:
                        return None
                    if l is None:
                        return r
                    if r is None:
                        return l
                    old, new = smallest_gone(r)
                    return Node(old, l, new)
                if comes_before(value, v):
                    return Node(v, delete_helper(l, value, comes_before), r)
                else:
                    return Node(v, l, delete_helper(r, value, comes_before))  
                             
def smallest_gone(tree: Node) -> tuple[Any, BinTree]:
    match tree:
        case Node(value=v, l = None, right=r):
            return (v, r)
        case Node(v, l, r):
            smallest, new = smallest_gone(l)
            return (smallest, Node(v, new, r))

         
         
         
         
         
            