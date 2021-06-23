import os # Importa os dados do sistema
from math import radians, sin, cos, sqrt # Importa as funções matemáticas
from random import random

g = 9.8 # Define o valor de g necessário para os cálculos posteriores

def cae_max(ang):  # Define a função que calcula o atrito máximo
    th = radians(ang)
    return (1 - sin(th)) / cos(th)

nome = input("Qual o nome do aluno? ") # Solicita o nome do arquivo a ser procurado
caminho_arquivo = "dados" + os.sep + "arq_{}.txt".format(nome.lower())

try: # Testando se o arquivo existe
    fs = open(caminho_arquivo, "r")
except IOError:
    print("Não existe arquivo para este aluno! O programa será encerrado.")
    exit()

try:  # Testa se o arquivo tem dados escritos
    lines = fs.readlines()
except ValueError:
    print("Não foi possível ler o arquivo. O programa será encerrado.")
    exit()

nova_lista = [] # Cria uma nova lista 
for line in lines:  # Exclui da leitura as linhas que estiverem em branco (linhas entre os dados) 
    if len(line) == 1:
        continue
    nova_lista.append(float(line)) 

if len(nova_lista) < 5: # Testa se o arquivo tem todos os dados
    print("Faltam dados na lista. O programa será encerrado.")
    exit()
    
# Atribui aos dados os valores do arquivo
ang = nova_lista[0]
cac = nova_lista[1]
h = nova_lista[2]
t = nova_lista[3]
v = nova_lista[4]

# calcula aceleraçao do bloco
th = radians(ang)
a = g - g * sin(th) - cac * g * cos(th)

# calcula o tempo de delocamento
tc = sqrt((2 * h) / a) 

# calcula a velocida
vc = a * t # também poderimos calcular por torricelli: sqrt(2 * a * h)

# Testando se o valor do arquivo confere com o valor digitado pelo aluno
if abs(t - tc) / tc > 0.01: # se o erro for maior que 1%
    print("O aluno errou o tempo, o valor certo seria t = {}".format(tc))
else:
    print("O aluno acertou o tempo. Parabéns!")

if abs(v - vc) / vc > 0.01: # se o erro for maior que 1%
    print("O aluno errou a velocidade, o valor certo seria: v = {}".format(vc))
else:
    print("O aluno acertou a velocidade. Parabéns!")
    
fs.close() # Fecha o arquivo
