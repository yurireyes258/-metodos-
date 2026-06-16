import numpy as np

# ==========================
# FUNCIONES DE PRUEBA
# ==========================

def f1(x):
    return x**3 - 2*x**2 + 5*x - 1

def df1(x):
    return 3*x**2 - 4*x + 5


def f2(x):
    return np.exp(x)

def df2(x):
    return np.exp(x)


def f3(x):
    return np.sin(x)

def df3(x):
    return np.cos(x)


# ==========================
# DERIVADAS DE 7 PUNTOS
# ==========================

def derivada_inicio(f,x,h):
    return (-147*f(x)+360*f(x+h)-450*f(x+2*h)
            +400*f(x+3*h)-225*f(x+4*h)
            +72*f(x+5*h)-10*f(x+6*h))/(60*h)

def derivada_final(f,x,h):
    return (147*f(x)-360*f(x-h)+450*f(x-2*h)
            -400*f(x-3*h)+225*f(x-4*h)
            -72*f(x-5*h)+10*f(x-6*h))/(60*h)

def derivada_central(f,x,h):
    return (-f(x+3*h)+9*f(x+2*h)-45*f(x+h)
            +45*f(x-h)-9*f(x-2*h)+f(x-3*h))/(-60*h)


# ==========================
# PRUEBAS
# ==========================

x = 1
h = 0.01

funciones = [
    ("Polinomial",f1,df1),
    ("Exponencial",f2,df2),
    ("Trigonométrica",f3,df3)
]

for nombre,f,df in funciones:

    real = df(x)

    print("\n====================")
    print(nombre)
    print("====================")

    print("Valor exacto:",real)

    print("Inicio :",derivada_inicio(f,x,h))
    print("Final  :",derivada_final(f,x,h))
    print("Central:",derivada_central(f,x,h))