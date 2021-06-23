# módulo de funções
from math import * # Importando bibliotecas necessárias para o cálculo

g = 9.8 # Definindo valor da aceleração da gravidade, que servirá de parâmetro futuramente

def a_static(tet0):
    return (1 - sin(tet0)) / cos(tet0) # definindo a função que calcula o atrito estático

def acceleration(tet0):  # definindo a função que calcula a aceleração máxima do bloco 2
    return (g - g * sin(radians(tet0))) / 2

def a_kinetic(tet0, a2):  # definindo a função que calcula o atrito cinético
    return (g * (1 - sin(radians(tet0))) - 2 * a2) / (g * cos(radians(tet0)))
