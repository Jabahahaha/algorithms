from algorithms.bisection import bisection
from algorithms.fixed_point import fixed_point_iteration
from algorithms.newton import newton_method
from utils.plotting import plot_convergence

def main():
    def f(x):
        return x**3 - x - 2
    
    def df(x):
        return 3*x**2 - 1
    
    def g(x):
        alpha = 0.01  # Stable and small alpha for fixed-point iteration
        return x - alpha * (x**3 - x - 2)
    
    a, b = 1, 2
    x0 = 1.5
    real_solution = 1.5213797068045678  # Known root for f(x) = x^3 - x - 2

    # Bisection method
    root_bisection, iterations_bisection = bisection(f, a, b)
    print(f"Bisection Method: Root = {root_bisection}")
    plot_convergence(iterations_bisection, f, real_solution, plot_mode='function_value')
    plot_convergence(iterations_bisection, f, real_solution, plot_mode='step_size')
    plot_convergence(iterations_bisection, f, real_solution, plot_mode='distance_to_solution')
    
    # Fixed Point Iteration method
    root_fixed_point, iterations_fixed_point = fixed_point_iteration(g, x0)
    print(f"Fixed Point Iteration: Root = {root_fixed_point}")
    plot_convergence(iterations_fixed_point, f, real_solution, plot_mode='function_value')
    plot_convergence(iterations_fixed_point, f, real_solution, plot_mode='step_size')
    plot_convergence(iterations_fixed_point, f, real_solution, plot_mode='distance_to_solution')
    
    # Newton's method
    root_newton, iterations_newton = newton_method(f, df, x0)
    print(f"Newton's Method: Root = {root_newton}")
    plot_convergence(iterations_newton, f, real_solution, plot_mode='function_value')
    plot_convergence(iterations_newton, f, real_solution, plot_mode='step_size')
    plot_convergence(iterations_newton, f, real_solution, plot_mode='distance_to_solution')

if __name__ == "__main__":
    main()
