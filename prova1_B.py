# Programa principal - parte B

from prova1_A import *  # Importando as funções criadas na parte A da prova

# Dando ao usuário uma breve descrição do sistema trabalhado e informações relevantes
print("O tema de estudo deste exercício é uma freada de carro em um movimento sobre uma estrada reta horizontal. Detalhe: o motorista freia sem travar as rodas do carro.")
print("IMPORTANTE: não esqueça que os valores decimais devem ser digitados utilizando 'ponto' como separador e não 'vírgula'. ")

# Solicitando o valor do atrito cinético ao usuário e testando-o
ce = float(input("Por favor entre com um valor para o atrito estático entre o pneu do carro e a estrada (LEMBRE-SE o atrito é um valor entre 0,2 e 1) : "))
while ce > 1 or ce < 0.2:
    ce = float(input("O valor que você digitou não é um valor razoável (ou há um erro de digitiação), por favor digite novamente um valor para o coeficiente de atrito estático : "))

# Solicitando um valor de velocidade inicial ao usuário e testando-o
vi = float(input("Por favor entre com um valor para a velocidade inicial do carro (em km/h): "))
while vi > 200:
    vi= float(input("A velocidade que você digitou é muito grande, tente novamente com um valor menor :"))
# Transformando v0 para unidades do SI utilizadas no módulo desse programa
v0 = vi / 3.6

# Calculando a distância de frenagem a partir da função definida no módulo do programa 
d = dist(ce, v0)
print("A distância de frenagem do carro vale: {:.3f} metros.".format(d))

# Solicitando o valor para a discretização do movimento e testanto
npts = int(input("Por último digite um valor (INTEIRO) para o número de pontos que deseja conhecer detalhes do movimento: "))
while npts < 5 or npts > 100:
    npts = int(input("O número de pontos deve estar em um intervalo de 5 a 100, para que não seja curto e nem longo demais, por favor digite novamente: "))

ll = discr(ce, v0, d, npts) # chama a função que constroi a lista

for i in range(0, npts):
    print("t: {0:.4g} s \t x: {1:.4g} m \t  v:  {2:.4g} m/s".format(ll[i][0], ll[i][1], ll[i][2])) # Imprime a lista

