import numpy as np

# ==========================
# DERIVADAS DE 3 PUNTOS
# ==========================

def derivada_inicio(f, x, h):
    return (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)

def derivada_final(f, x, h):
    return (3*f(x) - 4*f(x-h) + f(x-2*h))/(2*h)

def derivada_central(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)

# ==========================
# ENTRADA DE DATOS
# ==========================

expr = input("Ingrese la función f(x): ")

f = lambda x: eval(expr)

x = float(input("Ingrese x: "))
h = float(input("Ingrese h: "))

print("\nRESULTADOS")
print("3 puntos extremo inicial :", derivada_inicio(f, x, h))
print("3 puntos extremo final   :", derivada_final(f, x, h))
print("3 puntos punto medio     :", derivada_central(f, x, h))