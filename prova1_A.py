# módulo das funções parte A
from math import *
g = 9.8 # definindo valor de g, necessário para os demais cálculos

#Definindo uma função que calcula a velocidade inicial
def dist(ce, v0):
    return v0 **2 / (2 * ce * g)

# Definindo uma função que calcula a velocidade
def vel(ce, v0, x):
    return (v0**2 - (2 * ce * g * x ))**1/2

# Definindo uma função cria lista de valores
def discr(ce, v0, d, npts):
    dx = d / (npts - 1)
    ll = []
    for i in range(0, npts):
        x = dx * i
        v = (v0**2 - (2 * ce * g * x ))**1/2
        t = (v0 - v) / (ce * g)
       

        ll.append([t, x, v])
    return ll
