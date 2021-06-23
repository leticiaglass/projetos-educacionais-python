from math import sin, cos, radians
from tkinter import *

# Defindindo a função que cria um triangulo equilatero a partir do ponto fixo superior (x1, y1),
# e o comprimento do lado do triangulo
def create_triangle(canvas, x1, y1, length):
# triangulo = um poligono com três vértices)
    x2 = x1 + length * sin(radians(-30))
    y2 = y1 + length * cos(radians(-30))
    x3 = x1 + length * sin(radians(30))
    y3 = y1 + length * cos(radians(30))
    return canvas.create_polygon(x1, y1, x2, y2, x3, y3)
    
# Definindo uma função que cria o texto com as informações a partir das variáveis globais
def show_info(length):
    global h, w
    global canvas

    x0 = (w / 2) + 15                  # Seta do vetor "tensão"
    y0 = 50 - (length / 2) * 0.4   #  centraliza e diminui seu valor em 60% apenas pra ficar melhor a visualização
    y1 = 50 + (length / 2) * 0.4
    
    canvas.create_line(x0, y0, x0, y1, arrow=FIRST)
    canvas.create_text(x0 + 15, 50, text="T = {0:.3f} N".format((length * 1e-2) ** 2 / 2 * 5e-3 * 7900), anchor=W)
    canvas.create_text(10, h - 20, text="Espessura = 5 mm", anchor=W)
    canvas.create_text(10, h - 40, text="Placa triangular de ferro, com lado = {0:.2f} cm".format(length), anchor=W)
    
# Definindo a função que muda o comprimento do lado do triângulo a partir do valor digitado pelo usuário
def change_length(event):
    global length
    global value
    
    length = float(value.get()) # Transorma o valor digitado em uma variável do tipo float
    
    if (length > 200):
        length = 200
        value.set(length)  # Define um limite para o valor digitado, nesse caso 200 cm para máximo
    elif (length < 50):     # e 50 para mínimo
        length = 50
        value.set(length)

    draw(length)

# Definindo a função que desenha os objetos na tela
def draw(length):
    global w
    global h
    global canvas
    
    canvas.delete(ALL)
    
    # cria a linha
    x0, y0 = (w / 2, 0)
    x1, y1 = (w / 2, 100)
    canvas.create_line(x0, y0, x1, y1, fill="black", width=1)

    # cria o triangulo, com o ponto fixo no final da linha
    create_triangle(canvas, x1, y1, length)
    show_info(length)
    

# cria e nomeia a janela
window = Tk()
window.title("Placa triangular suspenso por um fio ")

# cria e adiciona um canvas a janela
h = 400
w = 400
canvas = Canvas(window, width=w, height=h, bg='white')
canvas.pack(side=TOP, padx=5, pady=5) 
length = 100

Label(window, text="Comprimento do lado do triangulo:").pack(side=LEFT, padx=5, pady=5)
value = StringVar()
value.set(length)
entrada = Entry(window, textvariable=value)
entrada.pack(side=LEFT, padx=5, pady=5)
entrada.bind("<Return>", change_length)

draw(length)
window.mainloop()
