#Juan sebastian Guzman Franco 
# Este programa nos permite encontrar la ecuación que nos describe 
#el comportamiento de los datos extraidos mediante un 
#experimiento, usando polinomios de lagrange.
# en este experimento se mide la deflexión de una barra empotrada 
#con una carga en el extremo 

#importamos librerias necesarias 
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Ingresamos los datos encontrados en el experimento 
xi = np.array([0, 5.7, 11.1, 16.4, 21.5, 26.7, 31.5, 36.7, 41.3, 46.1, 50.6, 55.1, 59.8, 64.3, 68.7])
fi = np.array([0, -1.5, -2.3, -3.1, -4.2, -5.3, -6.5, -7.2, -9.2, -10.6, -11.9, -13.3, -14.7, -16.1, -17.4])

# Procedimiento
# Conocer cuantos elementos tiene xi 
n = len(xi)
# Asignamos un carácter X
x = sym.Symbol('x')
# Inicializamos el polinomio
polinomio = 0
# Desplazamos i dentro del rango
for i in range(0,n,1):
    # Para calcular el primer termino de la Langrage, es necesario calcular un numerador que se obtiene por multiplicaciones
    numerador = 1
    denominador = 1
    # El numerador debe recorrer todos los puntos del vector xi
    for j in range(0,n,1):
        if (i != j):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
        # Calculamos los terminos de lagrange
        termino = (numerador/denominador)*fi[i]
    # Acumulamos los terminos
    polinomio = polinomio + termino
    
# Simplificamos la ecuación
polisimple = sym.expand(polinomio)

# Forma lamda del polinomio px, referencia x y el polinomio que se desea convertir
px = sym.lambdify(x, polinomio)

# Vectores para graficas
muestras = 13 # Numero cualquiera
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

# Salida
print('polinomio')
print(polinomio)
print(' ')
print('polinomio simplificado')
print(polisimple)

# Grafica
plt.plot(xi,fi, 'o')
plt.plot(p_xi,pfi)
plt.show()

Evaluamos en un punto 
print(' ')
print('Evaluación del polinomio')
print(px(12))
