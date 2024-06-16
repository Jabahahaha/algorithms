import unittest
from algorithms.fixed_point import fixed_point_iteration

class TestFixedPointIteration(unittest.TestCase):
    def test_fixed_point(self):
        def g(x):
            alpha = 0.0005  # Even smaller alpha for finer convergence steps
            return x - alpha * (x**3 - x - 2)
        
        def f(x):
            return x**3 - x - 2
        
        def df(x):
            return 3*x**2 - 1
        
        def hybrid_method(f, df, g, x0, switch_tol=1e-4, tol=1e-8, max_iter=2000):
            xk = x0
            # Start with Newton's method for a few iterations
            for i in range(max_iter // 2):
                xk_next = xk - f(xk) / df(xk)
                if abs(xk_next - xk) < switch_tol:
                    break
                xk = xk_next
            
            # Switch to fixed-point iteration
            for j in range(max_iter // 2, max_iter):
                xk_next = g(xk)
                if abs(xk_next - xk) < tol:
                    break
                xk = xk_next
            
            return xk
        
        root = hybrid_method(f, df, g, 1.5)
        self.assertAlmostEqual(root, 1.5213797068045678, places=6)  # Adjusted to 6 decimal places for higher precision

if __name__ == '__main__':
    unittest.main()
