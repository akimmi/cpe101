# CPE 101-01
# LAB 6: Polynomial Function Tests
# Name:
# Section:

import unittest
import poly

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_polyadd(self):	# Tests for add function
      poly1 = [2.3, 4.7, 1.0]
      poly2 = [1.2, 2.1, -3.2]
      poly3 = poly.poly_add2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
    
   def test_polyadd1(self):
      poly1 = [0, 1.1, 2.2]
      poly2 = [3, -1, 4]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3, [3, 0.1, 6.2])

   def test_polyadd2(self):
      poly1 = [3,3,3]
      poly2 = [-4,4,23]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3, [-1,7,26])
   
   def test_polymult(self):
      poly1 = [1,2,1]
      poly2 = [1,2,1]
      poly3 = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [1,4,6,4,1])

   def test_polymult1(self):
      poly1 = [5,-2,1]
      poly2 = [1,-3,6]
      poly3 = poly.poly_mult2(poly1, poly2)
      self.assertListAlmostEqual(poly3, [5,-17,37,-15,6])

   def test_polymult2(self):
      poly1 = [4,3,2]
      poly2 = [6,2,1]
      poly3 = poly.poly_mult2(poly1,poly2)
      self.assertListAlmostEqual(poly3, [24,26,22,7,2])
if __name__ == '__main__':
   unittest.main()
