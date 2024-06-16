import unittest
from algorithms.newton import newton_method

class TestNewtonMethod(unittest.TestCase):
    def test_newton(self):
        def f(x):
            return x**3 - x - 2
        
        def df(x):
            return 3*x**2 - 1
        
        root, iterations = newton_method(f, df, 1.5)
        self.assertAlmostEqual(root, 1.5213797068045678, places=6)  # Adjusted to 6 decimal places for higher precision

if __name__ == '__main__':
    unittest.main()
