import unittest
import nested

class TestCases(unittest.TestCase):
      def test_1(self):
          poly1 = [[1,2],[2,3,4], [-2,5]]
          poly2 = nested.product(poly1)
          self.assertEqual(poly2, [2,24,-10])
     
      def test_2(self):
          poly1 = [[1,1], [2,2], [3,3,3]]
          poly2 = nested.product(poly1)
          self.assertEqual(poly2, [1,4,27])


      def test_3(self): 
          poly1 = [[0,0], [-2,-2,-2]]
          poly2 = nested.product(poly1)
          self.assertEqual(poly2, [0,-8])
if __name__ == '__main__':
   unittest.main()
