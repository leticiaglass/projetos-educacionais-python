import os # Importa os dados do sistema
from random import random

g = 9.8 # Definindo g, que será necessário para cáclulos posteiores

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

if len(nova_lista) < 5: # Testa se o arquivo tem todos os 5 dados
    print("Faltam dados na lista. O programa será encerrado.")
    exit()
    
# Atribui aos dados os valores do arquivo
ce = nova_lista[0]
v0 = nova_lista[1]
d = nova_lista[2]
x = nova_lista[3]
v = nova_lista[4]

# calcula a distância miníma de freada
dc = v0 **2 / (2 * ce * g)
# calcula a velocidade do carro na batida
vc = (v0**2 - (2 * ce * g * x ))**1/2

# Testando se o valor do arquivo confere com o valor digitado pelo aluno
if abs(d - dc) / dc > 0.05: # se o erro for maior que 5%
    print("O aluno errou a distância, o valor certo seria d = {}".format(dc))
else:
    print("O aluno acertou a distância miníma. Parabéns!")

if abs(v - vc) / vc > 0.05: # se o erro for maior que 1%
    print("O aluno errou a velocidade, o valor certo seria: v = {}".format(vc))
else:
    print("O aluno acertou a velocidade. Parabéns!")
    
fs.close() # Fecha o arquivo
