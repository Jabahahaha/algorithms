def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    xk = x0
    iterations = [xk]
    
    for i in range(max_iter):
        xk_next = xk - f(xk) / df(xk)
        iterations.append(xk_next)
        
        if abs(xk_next - xk) < tol:
            break
        
        xk = xk_next
    
    return xk, iterations
