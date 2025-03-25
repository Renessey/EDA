from sympy import symbols, Eq, solve

def eq1(x):
    return 0.5 * x + 0.5

def eq2(x):
    return -x + 2

x, y = symbols('x y')
eq1 = Eq(y, 0.5 * x + 0.5)
eq2 = Eq(y, -x + 2)

solucao = solve((eq1, eq2), (x, y))

print(f"Solução do sistema: x = {solucao[x]:.2f}, y = {solucao[y]:.2f}")
