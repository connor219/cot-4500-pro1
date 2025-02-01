import numpy as np

def approximation_algorithm(x):
    """Rounds a number to 5 decimal places."""
    return round(x, 5)

def bisection_method(f, a, b, tol=1e-5):
    """Finds root of f using bisection method within [a, b]."""
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

def fixed_point_iteration(g, x0, tol=1e-5, max_iter=100):
    """Performs fixed-point iteration to approximate a root."""
    for _ in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    """Finds root using Newton-Raphson method."""
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0
