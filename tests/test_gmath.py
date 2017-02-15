import unittest
from gmath import factoring

class TestGMath(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(factoring.gcd(1, 1), 1)
        self.assertEqual(factoring.gcd(6, 42), 6)
        self.assertEqual(factoring.gcd(6, -42), 6)
        self.assertEqual(factoring.gcd(-6, 42), 6)
        self.assertEqual(factoring.gcd(-6, -42), 6)

if __name__ == "__main__":
    unittest.main(exit=False)