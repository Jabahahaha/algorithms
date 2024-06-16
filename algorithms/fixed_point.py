def fixed_point_iteration(g, x0, tol=1e-8, max_iter=2000):
    xk = x0
    iterations = [xk]
    
    for i in range(max_iter):
        xk_next = g(xk)
        iterations.append(xk_next)
        
        if abs(xk_next - xk) < tol:
            break
        
        xk = xk_next
    
    return xk, iterations
