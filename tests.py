import unittest
from calc import Calc

class TestStringMethods(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)
    
    def test_sumar(self):
        calc = Calc
        result = calc.sumar(2,2)
        self.assertEqual(4, result)

    def test_restar(self):
        # 4 - 2  = 2
        calc = Calc
        result =  calc.restar(4,2)
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()