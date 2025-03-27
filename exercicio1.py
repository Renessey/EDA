import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

def eq1(x):
    return 0.5 * x + 0.5

def eq2(x):
    return -x + 2

# Definição das equações
x, y = symbols('x y')
eq1_sym = Eq(y, 0.5 * x + 0.5)
eq2_sym = Eq(y, -x + 2)

# Resolvendo o sistema
solucao = solve((eq1_sym, eq2_sym), (x, y))
sol_x, sol_y = float(solucao[x]), float(solucao[y])

# Criando pontos para o gráfico
x_vals = np.linspace(-2, 4, 100)
y_vals_eq1 = [eq1(xi) for xi in x_vals]
y_vals_eq2 = [eq2(xi) for xi in x_vals]

# Criando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals_eq1, label=r'$y = 0.5x + 0.5$', color='blue')
plt.plot(x_vals, y_vals_eq2, label=r'$y = -x + 2$', color='red')
plt.scatter([sol_x], [sol_y], color='black', zorder=3, label=f'Solução ({sol_x:.2f}, {sol_y:.2f})')

# Configurações do gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução do Sistema de Equações')
plt.show()

print(f"Solução do sistema: x = {sol_x:.2f}, y = {sol_y:.2f}")
