import unittest
import map

class TestCases(unittest.TestCase):
    def test_1(self):
        # Add code here.
        pass
    def test_2(self):
        poly1 = [1, 2, 3]
        poly2 = map.cube_all(poly1)
        self.assertEqual(poly2, [1,8,27])
    def test_3(self):
        poly1 = [-2, 4, 9]
        poly2 = map.cube_all(poly1)
        self.assertEqual(poly2, [-8, 64, 729])
    def test_add(self):
        poly1 = [0,5,-7]
        poly2 = map.cube_all(poly1)
        self.assertEqual(poly2, [0,125,-343])

    def test_4(self):
        poly1 = [1,2,3]
        number = 5
        poly2 = map.add_n_to_all(poly1, number)
        self.assertEqual(poly2, [6,7,8])
    def test_5(self):
        poly1= [0, 4, 9]
        number = 3
        poly2 = map.add_n_to_all(poly1, number)
        self.assertEqual(poly2, [3, 7, 12])
    def test_8(self):
        poly1 = [3, 2, 7]
        number = -1
        poly2 = map.add_n_to_all(poly1, number)
        self.assertEqual(poly2, [ 2, 1, 6])

    def test_6(self):
        poly1 = [3, 4, 6, 8, 9]
        poly2 = map.div_by_5_all(poly1)
        self.assertEqual(poly2, [False, False, False, False, False])
    def test_7(self):
        poly1 = [-1, 0, -4, 5, 2]
        poly2 = map.div_by_5_all(poly1)
        self.assertEqual(poly2, [False, True, False, True, False])
    def test_9(self):
        poly1 = [0,5,10,15,20]
        poly2 = map.div_by_5_all(poly1)
        self.assertEqual(poly2, [True, True, True, True, True])
        
if __name__ == '__main__':
    unittest.main()
