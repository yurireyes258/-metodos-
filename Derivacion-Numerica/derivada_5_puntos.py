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
# DERIVADAS DE 5 PUNTOS
# ==========================

def derivada_inicio(f,x,h):
    return (-25*f(x)+48*f(x+h)-36*f(x+2*h)
            +16*f(x+3*h)-3*f(x+4*h))/(12*h)

def derivada_final(f,x,h):
    return (25*f(x)-48*f(x-h)+36*f(x-2*h)
            -16*f(x-3*h)+3*f(x-4*h))/(12*h)

def derivada_central(f,x,h):
    return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)


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