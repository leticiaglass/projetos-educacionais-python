import random

def vmax(Ce, R)
    return sqrt(Ce * R * 9.8)

name = input("Ola, qual o seu nome? ")

arq = open("prova_do(a)_%s" % name, "w")

value = input("%s, por favor digite um valor entre 5 e 10: " % name)

while int(value) < 5 or int(value) > 10:
    print("ops, voce digitou um valor errado!")
    value = input("Digite um valor entre 5 e 10: ")

arq.write("voce digitou o numero %s\n\n" % value)

Ce = random.random() + 0.2

print("O coeficiente de atrito estatico é: %f" % Ce)
arq.write("O coeficiente de atrito estatico é: %f\n\n" % Ce)

v = vmax(Ce, float(R))
