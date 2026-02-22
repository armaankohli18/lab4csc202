import math
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)
from bst import *

@dataclass(frozen=True)
class Point2D:
  x : float
  y : float

class BSTTests(unittest.TestCase):
  def test_alphabet(self):
    def alphabet(a : str, b : str) -> bool:
      return a < b
    bst = BinarySearchTree(alphabet, None)
    bst = insert(bst, "bob")
    bst = insert(bst, "armaan")
    bst = insert(bst, "ashlyn")
    bst = delete(bst, 'armaan')

    self.assertEqual(lookup("bob", bst), True)
    self.assertEqual(lookup("ashlyn", bst), True)
    self.assertEqual(lookup("armaan", bst), False)

  def test_points(self):
    def distance(point: Point2D) -> float:
      return math.sqrt((point.x**2 + point.y**2))
    
    def closer_to_origin(point1: Point2D, point2: Point2D) -> bool:
      return distance(point1) < distance(point2)
    
    bst = BinarySearchTree(closer_to_origin, None)
    bst = insert(bst, Point2D(1, 1))
    bst = insert(bst, Point2D(5, 7))
    bst = insert(bst, Point2D(6, 7))
    bst = delete(bst, Point2D(6, 7))

    self.assertEqual(lookup(Point2D(1,1), bst), True)
    self.assertEqual(lookup(Point2D(5,7), bst), True)
    self.assertEqual(lookup(Point2D(6, 7), bst), False)

  def test_reverse(self):
    def reverse(val:int, val2:int) -> bool:
      return val > val2
    
    bst = BinarySearchTree(reverse, None)
    bst = insert(bst, 5)
    bst = insert(bst, 6)
    bst = insert(bst, 7)
    bst = delete(bst, 7)

    self.assertEqual(lookup(5, bst), True)
    self.assertEqual(lookup(6, bst), True)
    self.assertEqual(lookup(7, bst), False)





if (__name__ == '__main__'):
  unittest.main()
