import unittest
from str_funcs import *

class TestCases(unittest.TestCase):
      def test_vowel_extractor(self):
         self.assertEqual(vowel_extractor('Akimmi'), 'Aii')
         self.assertEqual(vowel_extractor('tanginamo'), 'aiao')
         self.assertEqual(vowel_extractor('ANIKETH'), 'AIE')

      def test_str_translate(self):
         self.assertEqual(str_translate('hi there!', 'e' , 'E'), 'hi thErE!')
         self.assertEqual(str_translate('bae', 'a', 'A'), 'bAe')
         self.assertEqual(str_translate('translate', 'a', 'b'), 'trbnslbte')
         self.assertEqual(str_translate('string', 'i', '1'), 'str1ng')
     
      def test_rot_13(self):
         self.assertEqual(rot_13('m'), 'z')
         self.assertEqual(rot_13('M'), 'Z')
         self.assertEqual(rot_13('e'), 'r')
      #range functions
      def test_make_substring(self):
         self.assertEqual(make_substring('assembly', 4,7,1), 'mbl')
         self.assertEqual(make_substring('electricity', 1,5,2), 'lc')
         self.assertEqual(make_substring('pusheeniscute', 4, 12, 3), 'eiu')
      
      def test_is_palindrome(self):
         self.assertTrue(is_palindrome('Bob'))
         self.assertFalse(is_palindrome('oob'))
         self.assertTrue(is_palindrome('radar'))

      def test_count_characters(self):
         self.assertEqual(count_characters('count characters', 'w'), -1)
         self.assertEqual(count_characters('kim navarro', 'R'), 2)
         self.assertEqual(count_characters('aniketh bhat', 'a'), 2)
if __name__ == '__main__':
   unittest.main()
