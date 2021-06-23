import os
from math import radians, sin, cos
from random import random

def cae_max(ang):
    th = radians(ang)
    return (1 - sin(th)) / cos(th)

nome = input("Olá, qual o seu nome? ")
caminho_arquivo = "dados" + os.sep + "arq_{}.txt".format(nome.lower())

if not os.path.exists("dados"):
    os.makedir("dados")

fs = open(caminho_arquivo, "w")

print("#TODO: descr progam")

ang = random() * 90
print("A inclinação do plano é {0:.2f} graus".format(ang))
fs.write(str(ang) + os.linesep)

cac = random() * cae_max(ang)
print("O coeficiente de atrito cinético é {0:.3f}.".format(cac))
fs.write(str(cac) + os.linesep)

h = random()
print("deslocmento vertical do bloco (em relacao a pos de repouso i): {0:.3f} m.".format(h))
fs.write(str(h) + os.linesep)

t = float(input("quanto tempo durou o deslocamento (em segundos): "))
v = float(input("qual a velocidade do bloco o final do intervalo de deslocamento ({0:.03f} m): ".format(h)))

fs.close()  
