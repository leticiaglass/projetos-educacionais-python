from math import *

assunto = "Plano Inclinado 3."
print(assunto)

print("O tema deste exercício será o sistema já considerado na Prática B (dois blocos conectados por um fio que passa por uma polia, um pendurado e um sobre um plano inclinado com atrito). Os dois blocos possuem a mesma massa. O fio é rígido e de massa desprezível. Não há atrito no eixo da polia e a massa da polia também é desprezível. Há atrito entre o plano inclinado e o bloco que desliza sobre ele. Mas diferentemente da prática B, neste o caso o sistema está inicialmente em repouso.\nImportante: os coeficientes de atrito cinético e estático são sempre valores entre zero e um, e o cinético é sempre menor ou igual ao estático, nunca maior. E a aceleração da gravidade vale 9.8 m/s**2. " )

g = 9.8 # Definindo g, que é necessário para o cálculo da aceleração
ang = radians(float(input("Digite um valor para o ângulo de inclinação do plano (em graus e entre 0 e 90): "))) # Entrando com o valor do ângulo

if ang < 0 or ang > pi/2: # Aplicando as condições para o ângulo.
    print("O ângulo que você digitou não é válido, o programa será encerrado.") 
else:  # Caso a váriavel seja compátivel o programa executa as funções seguintes.
    a_max = g - g * sin(ang) # Cálculo da aceleração máxima possível
    print("A aceleração máxima possível do bloco pendurado para este ângulo é de: ", a_max)
    # Todas as funções abaixo estão dentro do primeiro "else"
    a = float(input("Agora digite um valor para a aceleração do bloco, que seja menor que a máxima possível: ")) # Entrando com o valor da aceleração.
    if a > a_max: # Aplicando as condições para a aceleração
        print("O valor de aceleração que você digitou é maior que a aceleração máxima possível. O programa será encerrado.")
    else:
        ac = (g * cos(ang)  -  a) / g * sin(ang)
        print("O valor do atrito cinético é: ", ac)
        # Novamente as funções abaixo estão dentro do else anterior.
        ae = float(input("Por último digite um valor compatível com o problema para o atrito estático do bloco: "))
        if ae < ac: # Testando a primeira condição.
            print("O valor é incompatível. Lembre-se o valor de atrito cinético nunca é maior que o de atrito estático. O programa será encerrado.")
        elif ae < 0 or ae > 1: # Passou da primeira, testando a segunda.
            print("O valor não é compatível, é menor que zero ou maior que um. O programa será encerrado.")
        else: # Se passar da segunda chegamos a mensagem final.
            print("Parabéns, você acertou." )
