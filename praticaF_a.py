import os  # Importando biblioteca do sistema 
from math import radians, sin, cos # importando funções matemáticas
from random import random # importando função random

# Criando uma função que calcule o atrito
def cae_max(ang):
    th = radians(ang)
    return (1 - sin(th)) / cos(th)

nome = input("Olá, qual o seu nome? ")
caminho_arquivo = "dados" + os.sep + "arq_{}.txt".format(nome.lower()) # Criando o arquivo com o nome do aluno

if not os.path.exists("dados"):  # Testando se existe a pasta
    os.makedir("dados")  # Caso não, criando a pasra

fs = open(caminho_arquivo, "w") # Abrindo o arquivo para escrever nele

print("O sistema deste trabalho é um plano inclinado com uma roldana e dois blocos ligados, um sobre o plano e o segundo pendurado. Os dois blocos possuem a mesma massa. O fio é rígido e de massa desprezível. Não há atrito no eixo da polia e a massa da polia também é desprezível. Há atrito entre o plano inclinado e o bloco que desliza sobre ele. O sistema está inicialmente em repouso. \n IMPORTANTE: use 'ponto' como separador para os valores decimais.")

ang = random() * 90 # Gerando ângulo aleatório entre 0 e 90
print("A inclinação do plano é {0:.2f} graus".format(ang)) # Imprimindo na tela o valor gerado
fs.write(str(ang) + os.linesep) # Gravando esse valor no arquivo

cac = random() * cae_max(ang) # Gerando coeficiente de atrto aleatório 
print("O coeficiente de atrito cinético é {0:.3f}.".format(cac)) # Imprimindo na tela o valor gerado
fs.write(str(cac) + os.linesep) # Gravando no arquivo

h = random() # Gerando altura aleatória entre 0 e 1 
print("O deslocamento vertical do bloco (em relação à posição de repouso i) é: {0:.3f} m.".format(h)) # Informando valor ao usuário
fs.write(str(h) + os.linesep)# Gravando no arquivo

# Solocitando valores para t e v e testando se é um valor numérico.
# Só sai do laço quando o usuário digitar certo
while True: 
    try:
        t = float(input("Digite o valor para o tempo de deslocamento do bloco 2 (em segundos): "))
        break
    except ValueError:
        print("Você deve digitar um valor (apenas números)") 
fs.write(str(t) + os.linesep)

while True:
    try:
        v = float(input("Digite a velocidade do bloco no final do intervalo de deslocamento ({0:.03f} m): ".format(h)))
        break
    except ValueError:
        print("Você deve digitar um valor com apenas números.")
fs.write(str(v) + os.linesep)

fs.close()  # Fechando o arquivo
