import math

assunto = "Movimento de Projétil"  # Definir a variável assunto
print(assunto) # Imprimir a variável na tela

print("Agora você deverá digitar alguns valores para o movimento do projétil. Para isso, você pode imaginar que está chutando uma bola em um jogo de futebol, por exemplo, e definir valores adequados a essa situação.") # Apenas uma recomendação para o usuário

g = float(input("Por favor entre com o valor da aceleração da gravidade do seu planeta (em m/s²): "))
tv = float(input("Por favor entre com o valor do tempo de voo do projétil (em segundos): "))
alc = float(input("Por favor entre com o valor do alcance do projétil (em metros): ")) # Recebendo os valores das variáveis como string e transformando em float.

v0x = alc / tv
v0y = g * tv / 2
v0 = (v0x ** 2 + v0y ** 2) ** 0.5 # cálculo da velocidade inicial
tet0 = math.atan( v0y / v0x)  # cálculo do ângulo de lançamento
alt = (v0 * math.sin(tet0)) ** 2 / (2 * g) # cálculo da altura

print("A velocidade inicial é", v0, "m/s.")
print("O ângulo de lançameno do projétil", tet0, "radianos.")
print("A altura do movimento é", alt, "m.")


