import unittest
from algorithms.bisection import bisection

class TestBisection(unittest.TestCase):
    def test_bisection(self):
        def f(x):
            return x**3 - x - 2
        
        root, iterations = bisection(f, 1, 2)
        self.assertAlmostEqual(root, 1.521, places=3)

if __name__ == '__main__':
    unittest.main()
