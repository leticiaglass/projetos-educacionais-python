from tkinter import * # importando o módulo tkinter
from math import sqrt, sin, cos, radians # importando as funções matemáticas necessárias

# Define as variaveis do sistema
S = 10  # dimensão canvas -> objeto
h = 400
w = 600

mass = 1.0 
r = S * .66
t = 0.

x0 = w / 2
y0 = h / 2
running = False

# Define a função que redesenha a partícula em cada nova posição
def redraw(x, y):
    canvas.coords(part, x-r, y-r, x+r, y+r)

# Define a função que anima o sistema
def animate():
    global t, running
    global x, y
    
    if running is not True:
        return
    
    dt = 50     # Define um dt para os frames da animação 
    t += dt * 1e-3

    x = x0 + float(v0Value.get()) * cos(radians(float(thValue.get()))) * t + float(FxValue.get()) / mass * 0.5 * t ** 2
    y = y0 - float(v0Value.get()) * sin(radians(float(thValue.get()))) * t + float(FyValue.get()) / mass * 0.5 * t ** 2

    redraw(x, y)
    window.after(dt, animate)

# Define a função que inicia/pausa o sistema (botão)   
def start():
    global running
    
    if running == True:
        running = False
    else:
        running = True
        animate()

# Define a função que para o sistema e volta a posição inicial (botão)
def stop():
    global running, t, x0, y0
    running = False
    t = 0
    redraw(x0, y0)

# Define a função que para o sistema e mostra passo a passo (botão)
def step():
    global running
    running = True
    animate()
    running = False

# Criar e nomear a janela
window =  Tk()
window.title("Leticia Glass")

# Criar e adicionar o canvas
canvas = Canvas(window, width=w, height=h, bg="white")
# Cria e adiciona textos informativos na tela
canvas.create_text(10,10,text="-Digite a velocidades inicial e forças no SI.",anchor=W)
canvas.create_text(10, 46, text="A particula possui 1 kg.", anchor=W)
canvas.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# Cria os espaços para digitação
Label(window, text='Velocidade inicial (m/s)').grid(row=4,column=1,sticky=E)
Label(window, text='Ângulo do lançamento (graus)').grid(row=5,column=1,sticky=E)
Label(window, text='Força no eixo x (N)').grid(row=4,column=3,sticky=E)
Label(window, text='Força no eixo y (N)').grid(row=5,column=3,sticky=E)

# Captura os valores
v0Value = StringVar()
thValue = StringVar()
FxValue = StringVar()
FyValue = StringVar()

# Propõe valores iniciais para o sistema
v0Value.set(60.)
thValue.set(90.)
FxValue.set(0.0)
FyValue.set(9.8)

v0Entr = Entry(window, textvariable=v0Value)
thEntr = Entry(window, textvariable=thValue)
FxEntr = Entry(window, textvariable=FxValue)
FyEntr = Entry(window, textvariable=FyValue)

# Coloca as posições dos campos de digitação
v0Entr.grid(row=4,column=2,sticky=E)
thEntr.grid(row=5,column=2,sticky=E)
FxEntr.grid(row=4,column=4,sticky=E)
FyEntr.grid(row=5,column=4,sticky=E)

# Cria, adiciona e posiciona os botões
Button(window, text='Start/Pause', command=start).grid(row=6, column=1, sticky=W+N)
Button(window, text='Stop', command=stop).grid(row=6, column=2, sticky=W+N)
Button(window, text='Step', command=step).grid(row=6, column=3, sticky=W+N)
Button(window, text='Sair', command=window.destroy).grid(row=6, column=4, sticky=W+N)


# Desenhando
x = x0
y = y0
part = canvas.create_oval(x-r,y-r,x+r,y+r, outline="pink", fill="pink")

window.mainloop()
