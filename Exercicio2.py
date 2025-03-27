import numpy as np
import matplotlib.pyplot as plt

def Equacao(a, b, c):
    delta = b**2 - 4*a*c 
    
    if delta < 0:
        return None  
    elif delta == 0:
        x = -b / (2*a)
        return [x]  
    else:
        raiz1 = (-b + np.sqrt(delta)) / (2*a)
        raiz2 = (-b - np.sqrt(delta)) / (2*a)
        return [raiz1, raiz2]
        
a, b, c = 2, 2, -6 #valores inseridos na função Equacao
raizes = Equacao(a, b, c)

#plotando os gráficos
x = np.linspace(-4, 4, 400)
y = a * x**2 + b * x + c

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$2x^2 + 2x - 6$', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', linewidth=0.5)