import unittest
import random

class test_ran(unittest.TestCase):
    def test_sum(self):
        result=random.myfunct(30,20,"sum")
        self.assertEqual(random.myfunct(-1,1,"sum"),0)
        self.assertEqual(random.myfunct(-11, 10, "sum"), -1)
        self.assertEqual(random.myfunct(10, -5, "sum"), 5)
        self.assertEqual(random.myfunct(-5, -5, "sum"), -10)

    def test_sub(self):
        result=random.myfunct(32,11,"sub")
        self.assertEqual(result,21)

    def test_mul(self):
        result=random.myfunct(23,2,"mul")
        self.assertEqual(result,46)
        with self.assertRaises(ValueError):
            random.myfunct(1,-2,"mul")

if __name__=='__main__':
    unittest.main()



