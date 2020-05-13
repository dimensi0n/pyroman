import unittest
import src.main as number
class TestNumbertoRoman(unittest.TestCase):
    def test2(self):
        self.assertEqual(number.toRoman(2), 'II')
    def test10(self):
        self.assertEqual(number.toRoman(10), 'X')
    def test55(self):
        self.assertEqual(number.toRoman(55), 'LV')
    def test100(self):
        self.assertEqual(number.toRoman(100), 'C')
    def test500(self): 
        self.assertEqual(number.toRoman(500), 'D')
    def test1000(self):
        self.assertEqual(number.toRoman(1000), 'M')
if __name__ == '__main__':
    unittest.main()
