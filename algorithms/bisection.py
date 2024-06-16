def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    
    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return c, iterations
