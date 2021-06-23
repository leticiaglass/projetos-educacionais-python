from math import radians, pi, cos, sin #Importa apenas as funções necessárias para o programa

titulo = "Projétil com Obstáculo 3" #Imprimindo o título e a descrição do programa 
print(titulo)
print("Considere o movimento do projétil sem arraste do ar, supondo que trata-se de um jogo de bola dentro de um ginásio cujas paredes não são muito distantes da quadra de jogo. Para simplificar, supõe-se que o projétil é lançado de maneira que a sua direção de movimento horizontal seja perpendicular a uma das paredes.")

# Entrando com os valores
v0 = float(input("Digite um valor para a velocidade inicial do projétil (em m/s): "))
while (v0 < 0):  # Impondo as condições
    v0 = float(input("A velocidade deve ser positiva. Tente novamente: "))
th = radians(float(input("Digite um valor para o angulo de lançamento (em graus): ")))
while (th < 0 or th > pi / 2):
    th = radians(float(input("O valor deve estar entre 0 e 90 graus. Tente novamente: ")))
l = float(input("Digite um valor para a distância até a parede: "))
while (l < 0):
    l = float(input("O parede não pode estar atrás de você. Tente novamente: "))
dt = float(input("Digite o intervalo para a discretização do tempo (em segundos): "))
while (dt < 0):
    dt = float(input("O intervalo não pode ser negativo. Tente novamente: "))
    
t = 0.
x0, y0 = (0., 0.) # coordenadas iniciais

print("t (s)\tx (m)\ty (m)") # Imprime os títulos das colunas
while True:
    # Calcula as coordenadas no tempo t
    x = x0 + v0 * cos(th) * t
    y = y0 + v0 * sin(th) * t - 0.5 * 9.8 * t ** 2
    
    # Verifica se não ultrapassou alguma das barreiras (chão ou parede)
    if x > l:
        print("O projétil atingiu a parede!")
        break
        
    if y < 0:
        print("O projetil atingiu o chão!")
        break

    # imprime o tempo e as coordenadas uma vez que as condições (de quebra) não tenham sido satisfeitas
    print("{:.3g}\t{:.3g}\t{:.3g}".format(t, x, y))

    # incrementa o tempo
    t = t + dt

print("end") 
