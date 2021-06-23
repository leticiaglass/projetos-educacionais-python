from math import *
print("Plano Inclinado com atrito 3:")
print("O sistema representa um bloco deslizando por um plano inclinado com atrito e preso por um cabo que passa por uma roldana e prende um segundo bloco.")

g = 9.8  # Aceleração da gravidade em m/s**2

ang = float(input("Digite um valor para o ângulo de inclinação do plano (em graus): "))  # A função recebe o valor do ângulo como string e transforma em um objeto do tipo float

a_max = g - g * sin(radians(ang)) # Cálculo da aceleração máxima, onde +g representa o segundo bloco 

print("Aceleração máxima possível do bloco (desprezando o atrito) é ", a_max, "m/s**2") # Imprimimos o resultado na tela
 
a = float(input("Agora, defina um valor (inferior ao obtido para a aceleração máxima) para a aceleração do bloco pendurado: ")) # A função recebe o valor da aceleração como string e transforma em um objeto do tipo float

cac  = (g - a - g * sin(radians(ang))) / g * cos(radians(ang)) # Cálculo do coeficiente de atrito cinético

print("O coeficiente de atrito cinético é", cac) # Imprimir na tela o valor do atrito 
