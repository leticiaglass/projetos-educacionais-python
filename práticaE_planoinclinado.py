# programa principal
from praticaE2_functions import * # Importando todas as funções criadas no módulo de funções

assunto = "Plano inclinado 3." # Definindo assunto e informações relevantes
print(assunto)
print("O tema deste exercício será o seguinte sistema: dois blocos conectados por um fio que passa por uma polia, um pendurado e um sobre um plano inclinado com atrito. Os dois blocos possuem a mesma massa. O fio é rígido e de massa desprezível. Não há atrito no eixo da polia e a massa da polia também é desprezível. Há atrito entre o plano inclinado e o bloco que desliza sobre ele. Neste o caso o sistema está inicialmente em repouso. \nImportante: os coeficientes de atrito cinético e estático são sempre valores entre zero e um, e o cinético é sempre menor ou igual ao estático, nunca maior. E a aceleração da gravidade vale 9.8 m/s**2. " )

# Solicitando o valor do ângulo ao usuário e testando-o
tet0 = float(input("Por favor digite um valor (entre 0 e 90) para o ângulo de inclinação do plano (em graus): "))
if tet0 > 90 or tet0 < 0:
    print("Desculpe, o valor do ângulo que você digitou não é compatível com o problema. Precisamos de um ângulo entre 0 e 90 graus. O programa será encerrado.")
    exit()
else:  # Após passar pela condição, efetuando o cálculo de cae_max e a_max e imprimindo na devida formatação
    cae_max = a_static(radians(tet0))
    print("O atrito estático máximo (antes do sistema sair do repouso) é: {:.3f}".format(cae_max))
    a_max = acceleration(tet0)
    print("E a aceleração máxima do bloco 2 (evidentemente desprezando o atrito) vale: {:.3f} m/s**2.".format(a_max))

# Solicitando valor para a aceleração
a2 = float(input("Agora por favor digite um valor (MENOR QUE a_max) para a aceleração do bloco 2 (em m/s²): "))
while a2 >= a_max:
    print(a_max, a2)
    a2 = float(input("Lembre-se: o valor deve ser MENOR que aceleração máxima! Tente novamente: "))

cac = a_kinetic(tet0, a2)
print("O valor do atrito cinético vale: {:.3f}".format(cac))
print(cac)
