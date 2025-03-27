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