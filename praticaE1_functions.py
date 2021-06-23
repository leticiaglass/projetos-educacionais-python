#modulo de funções
import math
# Definindo as funções que recebem os dados e calculam as variáveis
def vel(g, tv, alc): 
    v0x = alc / tv
    v0y = g * tv / 2
    v0 = (v0x ** 2 + v0y ** 2) ** 0.5 # cálculo da velocidade inicial
    return v0

def ang(g, tv, alc):
    v0x = alc / tv
    v0y = g * tv / 2
    return math.atan2(v0y, v0x)  # cálculo do ângulo de lançamento

def h(g, v0, tet0):
    v0x = v0 * math.cos(tet0)
    v0y = v0 * math.sin(tet0)
    return (v0 * math.sin(tet0)) ** 2 / (2 * g) # cálculo da altura

def discr(g, tv, alc, npts): # Definindo a função que constroi uma lista com os dados
    dt = tv / (npts - 1)
    ll = []
    for i in range(0, npts):
        t = dt * i
        x = (alc / tv) * t   # isto é: v0x * t
        y = (g * tv / 2) * t - g * t**2 / 2 # v0y * t - g * t**2

        ll.append([t, x, y])
    return ll
        
             
