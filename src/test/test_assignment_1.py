import pytest
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson

def test_approximation_algorithm():
    assert approximation_algorithm(3.1415926535) == 3.14159

def test_bisection_method():
    f = lambda x: x**2 - 4
    assert abs(bisection_method(f, 0, 3) - 2) < 1e-5

def test_fixed_point_iteration():
    g = lambda x: (x + 2/x) / 2
    assert abs(fixed_point_iteration(g, 1) - np.sqrt(2)) < 1e-5

def test_newton_raphson():
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    assert abs(newton_raphson(f, df, 3) - 2) < 1e-5
