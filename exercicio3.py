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

x = np.linspace(0, 2, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x^3 - x - 2')
plt.axhline(0, color='black', linewidth=1.3, linestyle='--')
plt.axvline(raiz, color='red', linestyle='--', label=f'Raiz ≈ {raiz:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('Método da Bisseção')
plt.show()

