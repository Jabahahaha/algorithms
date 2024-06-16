import matplotlib.pyplot as plt

def plot_convergence(iterations, f, real_solution=None, plot_mode='function_value'):
    function_values = [f(x) for x in iterations]
    step_sizes = [abs(iterations[i] - iterations[i-1]) for i in range(1, len(iterations))]
    if real_solution is not None:
        distances_to_real_solution = [abs(x - real_solution) for x in iterations]
    else:
        distances_to_real_solution = None

    plt.figure(figsize=(10, 6))
    
    if plot_mode == 'function_value':
        plt.plot(function_values, label='Function Value f(x_k)')
        plt.ylabel('f(x_k)')
    elif plot_mode == 'step_size':
        plt.plot(step_sizes, label='Step Size |x_k - x_(k+1)|')
        plt.ylabel('|x_k - x_(k+1)|')
    elif plot_mode == 'distance_to_solution' and real_solution is not None:
        plt.plot(distances_to_real_solution, label='Distance to Real Solution |x_k - x*|')
        plt.ylabel('|x_k - x*|')
    else:
        raise ValueError("Invalid plot mode or real solution not provided for distance to solution.")
    
    plt.xlabel('Iteration Number')
    plt.title(f'Convergence Plot ({plot_mode.replace("_", " ").title()})')
    plt.legend()
    plt.grid(True)
    plt.show()
