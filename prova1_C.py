import os  # Importando biblioteca do sistema 
from random import random # importando função random

nome = input("Olá, qual o seu nome? ")
# Criando o arquivo com o nome do aluno
caminho_arquivo = "dados" + os.sep + "arq_{}.txt".format(nome.lower()) 

if not os.path.exists("dados"):  # Testando se existe a pasta
    os.makedir("dados")  # Caso não, criando a pasra

fs = open(caminho_arquivo, "w") # Abrindo o arquivo para escrever nele

print("Este teste será sobre a frenagem de um carro em um movimento retilíneo uniforme. O motorista não trava as rodas do carro na hora da frenagem. \n IMPORTANTE: use 'ponto' como separador para os valores decimais.")

ce = 0.2 + 0.8 * random() # Gerando coeficiente de atrito aleatório entre 0,2 e 1
print("O coeficiente de atrito estático vale {0:.2f}".format(ce)) # Imprimindo na tela o valor gerado
fs.write(str(ce) + os.linesep) # Gravando esse valor no arquivo

v0 = 40 + 100 * random() # Gerando uma velocidade inicial aleatória 
print("A velocidade inicial é {0:.3f} m/s.".format(v0)) # Imprimindo na tela o valor gerado
fs.write(str(v0) + os.linesep) # Gravando no arquivo

# Solocitando valores para d e testando se é um valor numérico.
# Só sai do laço quando o usuário digitar certo
while True: 
    try:
        d = float(input("Digite o valor para a distância de frenagem (em metros): "))
        break
    except ValueError:
        print("Você deve digitar um valor (apenas números), tente novamente: ") 
fs.write(str(d) + os.linesep) # Grava no arquivo

# Impondo uma nova condição ao usuário
print("Agora vamos considerar que existe um obstáculo no caminho (a uma distância x do início da frenagem), e que o carro mesmo freiando irá bater nele.")
x = random () * d # Gerando um valor entre 0 e d, ou seja, a batida acontecerá!
print("A distância do obstáculo é {0:.3f} metros.".format(x)) # Imprimindo na tela o valor gerado
fs.write(str(x) + os.linesep) # Gravando no arquivo

# Solicitando ao aluno o valor da velocidade do carro na batida, testando e gravando o valor no arquivo
while True:
    try:
        v = float(input("Qual será o valor da velocidade do carro na hora da batida (em km/h)? "))
        break
    except ValueError:
        print("Você deve digitar um valor (apenas números): ")
fs.write(str(v) + os.linesep)

fs.close()  # Fechando o arquivo
