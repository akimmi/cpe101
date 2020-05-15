import unittest
import filter

class TestCases(unittest.TestCase):
   def test_1(self):
      # Add code here.
      pass
   def test_2(self):
      poly1= [-3,-2,-1,2,5,9]
      poly2 = filter.are_even(poly1)
      self.assertEqual(poly2, [-2,2])
   def test_3(self):
      poly1 = [2,4,5,7,8]
      poly2 = filter.are_even(poly1)
      self.assertEqual(poly2, [2,4,8])
   def test_4(self):
      poly1 = [0,-4]
      poly2 = filter.are_even(poly1)
      self.assertEqual(poly2, [0,-4])

   def test_8(self):
      poly1 = [2,4,6,7,9,1]
      number = 3
      poly2 = filter.are_divisible_by_n(poly1, number)
      self.assertEqual(poly2, [6,9])
   def test_9(self):
      poly1 = [2,3,4]
      number =1
      poly2 = filter.are_divisible_by_n(poly1, number)
      self.assertEqual(poly2, [2,3,4])
   def test_10(self):
      poly1 = [10, 6, 20, 23, 2, 25]
      number = 5
      poly2 = filter.are_divisible_by_n(poly1, number)
      self.assertEqual(poly2, [10, 20, 25])
    
   def test_11(self):
      poly1 = [1,1,1,2,3]
      poly2 = filter.remove_duplicates(poly1)
      self.assertEqual(poly2, [1,2,3])
   
   def test_12(self):
      poly1 = [1,1,1,1]
      poly2 = filter.remove_duplicates(poly1)
      self.assertEqual(poly2, [1])

   def test_13(self):
      poly1 = [1,2,3]
      poly2 = filter.remove_duplicates(poly1)
      self.assertEqual(poly2, [1,2,3])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

