from math import sin, cos, radians
from tkinter import * # importando módulo tkinter

# cria um triangulo equilátero a partir do ponto fixo superior (x1, y1), e o comprimento do lado do triangulo
def create_triangle(canvas, x1, y1, length): 

# triangulo = um poligono com três vertices)
# Pontos dos vértices inferiores do triângulo a partir do ponto inicial (x1,y1)
    x2 = x1 + length * sin(radians(-30))  
    y2 = y1 + length * cos(radians(-30))
    
    x3 = x1 + length * sin(radians(30))
    y3 = y1 + length * cos(radians(30))
    
    return canvas.create_polygon(x1, y1, x2, y2, x3, y3) 
    

# Definindo a função que cria os textos com as informações dos dados do problema
def show_info(length): 
    global h, w
    global canvas

    x0 = (w / 2) + 15   
    y0 = 50 - (length / 2) * 0.4
    y1 = 50 + (length / 2) * 0.4
    
    canvas.create_line(x0, y0, x0, y1, arrow=FIRST)
    canvas.create_text(x0 + 15, 50, text="T = {0:.3f} N".format((length * 1e-2) ** 2 / 2 * 5e-3 * 7900), anchor=W)
    canvas.create_text(10, h - 20, text="Espessura = 5 mm", anchor=W)
    canvas.create_text(10, h - 40, text="Placa triangular de ferro, com lado = {0:.2f} cm".format(length), anchor=W)
    
# Definindo as funções que aumentam e diminuem o triângulo
def inc():
    global length
    
    if length > 200:  # Colocando um valor máximo para o aumento 
        return

    length *= 1.05   # Aumento de 5%
    canvas.delete(ALL)
    draw(length)

def dec():
    global length
    
    if length < 50: # Colocando um valor mínimo para a diminuição
        return
        
    length *= 0.95    # Diminuindo 5%
    canvas.delete(ALL)
    draw(length)


# Função que desenha na tela os objetos
def draw(length):
    global w, h
    
    # cria a linha
    x0, y0 = (w / 2, 0)
    x1, y1 = (w / 2, 100)
    canvas.create_line(x0, y0, x1, y1, fill="black", width=1)
    
    # cria o triangulo, com o ponto fixo no final da linha
    create_triangle(canvas, x1, y1, length)
    show_info(length)
    
# Criando a janela
# cria e nomeia a janela
window = Tk()
window.title("Placa triangular suspenso por um fio - Leticia Glass.")

# cria e adiciona um canvas a janela
h = 400
w = 400
canvas = Canvas(window, width=w, height=h, bg='white')
canvas.pack(side=TOP, padx=5, pady=5) 

# adiciona botões para aumentar ou diminuir o triangulo
Button(window, text="+ zoom", command=inc).pack(side=LEFT, padx=5, pady=5)
Button(window, text="- zoom", command=dec).pack(side=LEFT, padx=5, pady=5)

length = 100

draw(length)
window.mainloop()
