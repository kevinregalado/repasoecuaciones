# ===== archivo: utils.py =====
import random

# Genera ecuación ax + b = c con solución entre 1 y 10

def generar_ecuacion():
    x = random.randint(1, 10)
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x

# Formatea la ecuación para mostrar

def formatear_ecuacion(a, b, c):
    if b >= 0:
        return f"{a}x + {b} = {c}"
    else:
        return f"{a}x - {abs(b)} = {c}"
