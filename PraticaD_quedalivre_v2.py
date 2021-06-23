assunto = "Queda livre sem arraste do ar."
print(assunto)

g = 9.8 # Defindindo um valor para a aceleração da gravidade, que será necessário mais tarde

# Valores de entrada 
alt = float(input("Por favor entre com o valor da altura do ponto onde solta-se o objeto (em metros): "))
npts  = int(input("Por favor entre com um valor (INTEIRO) para o núemro de pontos que deseja na discretização vertical: ")) # Pega o valor de entrada e tranforma em uma variável inteira

# Calcular o intervalo de posição entre pontos sucessivos de maneira que os pontos esteam igualmente separados no espaço
dy = alt / (npts - 1)

# Primeiro precisamos criar listas vazias para depois incrementá-las com os dados
ll = []

# Calculando a posição, tempo e velocidade para cada npts 
for i in range(0, npts):
    y = alt - i * dy   
    t = (2 * (alt - y) / g)**0.5
    v = g * t

    # Adicionando os valores as listas criadas
    ll.append([y, t, v])

# Por último, imprimimos os valores obtidos na devida formatação
for i in range(0, npts): 
    print("t: {:.3} s\t y: {:.3} m\t v: {:.3} m/s".format(ll[i][1], ll[i][0], ll[i][2]))

print("end")
