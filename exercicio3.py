import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2
    
def busca(a, b, tol):
    while (b - a) / 2 > tol:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2
    
raiz = busca(1, 2, 1e-4)
print(f"Raiz aproximada: {raiz:.4f}")

