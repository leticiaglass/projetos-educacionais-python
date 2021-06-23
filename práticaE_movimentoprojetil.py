#programa principal
from praticaE1_functions import *  #importando as funções

print("Este programa tratará de um problema de movimento de projétil, para isso pode-se"
        "\n imaginar um sistema onde um jogador chuta uma bola em um jogo de futebol.")

# Solicitando os dados ao usuário
g = float(input("Por favor, entre com o valor da gravidade do planeta considerado (em m/s²): "))
tv = float(input("Por favor, entre com o valor do tempo de voo do projétil em (em s): "))
alc = float(input("Por favor, entre com o valor do alcance do projétil (em m): "))

print("Você escolheu g =", g, "m/s²."
       "\n tv = ", tv, "segundos."
       "\n e alc =", alc, "metros.")  # Verificação dos valores digitados pelo usuário.

# Usando o módulo das funções para calcular as incógnitas e printando cada uma:
v0 = vel(g, tv, alc)
print("a velocidade inicial é: ", v0, "m/s².")

tet0 = ang(g, tv, alc)
print("o ângulo de lançamento é: ", tet0, "rad")

v0x = alc / tv
v0y = g * tv / 2 # Definindo variáveis que precisam ser usadas como argumento para tet0
v0 = (v0x ** 2 + v0y ** 2) ** 0.5
tet0 = math.atan2(v0y, v0x)  # Definindo variáveis que precisam ser usadas como argumento para alt
alt = h(g, v0, tet0)
print("a altura é: ", alt, "metros.")

# Solicitando ao usuário dt
npts = int(input("Por favor digite um valor (INTEIRO) para a descretização do tempo: "))

ll = discr(g, tv, alc, npts) # chama a função que constroi a lista

for i in range(0, npts):
    print("t: {0:.3g} s \t x: {1:.3g} m \t  y:  {2:.3g} m".format(ll[i][0], ll[i][1], ll[i][2]))
