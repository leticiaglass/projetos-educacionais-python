from tkinter import * # importando o módulo tkinter
from math import sqrt, sin

# define as variaveis globais
S = 10      # escala sistema <-> canvas
h = 400     # altura do canvas
w = 500     # comprimento do canvas

t = 0.      # variavel para controlar o tempo na animação
m = 50.     # massa da bola
k = 50.     # constante elástica inicial
l0 = 5 + 9.8 * m / k      # comprimento inicial do elástico
A = 0.      # Amplitude de deslocamento inicial
r = 3.      # raio da bola
x = w/2     # posição do sistema
def y(l):   # posiçao y da bola como funçao do comprimento do elástico
    return l + r

running = False

# Define a função que redesenha as informações conforme a animação ocorre
def redraw(l):
    global info, txForce
    can.coords(ela, x, 0, x, S*l)
    can.coords(circ, x-S*r, S*y(l)-S*r, x+S*r, S*y(l)+S*r)
    yi = h/2 + (l0-l) * S * 0.5
    yf = h/2 + (l-l0) * S * 0.5
    can.coords(lnForce, x + 45, yi, x + 45, yf)
    can.delete(txForce)
    txForce = can.create_text(x + 60, h/2, text="F = {0:.3} N".format(k*(l-l0)), anchor=W)
    can.delete(info)
    info = can.create_text(10, h-20, text="posição atual: y = -{0:.2f} m".format(l), anchor=W)
 
# Define a função que faz a animação
def animate():
    global t, running, info
    global A
    
    if running is not True:
        return
    
    dt = 50 # Define um dt para os frames da animação 
    t += dt

    dl = A * sin(sqrt(k / m) * t)

    redraw(l0+dl)
    jan.after(dt, animate)

# Função que inicia/continua a animação
def start():
    global running
    
    if running == True:
        running = False
        btInc.configure(state=NORMAL)
        btDec.configure(state=NORMAL)
    else:
        running = True
        btInc.configure(state=DISABLED)
        btDec.configure(state=DISABLED)
        animate()

# Funçao que pára a animação e retorna ao estado inicial
def stop():
    global running, t, A
    running = False
    btInc.configure(state=NORMAL)
    btDec.configure(state=NORMAL)
    t = 0
    A = 0
    redraw(l0)

# Funções para "puxar" a bolinha e fazer o movimento acontecer
def inc():
    global A
    if A > 0.6 * l0:
        return
    A += l0 * 0.05
    redraw(l0 + A)
def dec():
    global A
    if A < -0.6 * l0:
        return
    A -= l0 * 0.05
    redraw(l0 + A)

# Função que aceita como entrada um novo valor de k e muda o movimento    
def change_k(event):
    global k
    global value

    nk = float(value.get())
    if nk > 100:        # Impondo um limite superior
        value.set(100)
    elif nk < 25:       # Impondo um limite inferior
        value.set(25)
        
    k = float(value.get()) # Tranforma o valor digitado numa variável do tipo float
    

# Criar e nomear a janela
jan =  Tk()
jan.title("Massa pendurada por um elástico - Leticia Glass")

# Criar e adicionar o canvas
can = Canvas(jan, width=w, height=h, bg="white")
can.pack(side=TOP, padx=5, pady=5)

# Cria e adiciona o espaço para digitação do valor de k
value = StringVar()
value.set(k)
Label(jan, text="Constante elástica do elástico:").pack(side=LEFT, padx=5, pady=5)
entrada = Entry(jan, textvariable=value)
entrada.pack(side=LEFT, padx=5, pady=5)
entrada.bind("<Return>", change_k)

# Cria os demais botões
Button(jan, text="Start/Pause", command=start).pack(side=LEFT, padx=5, pady=5)
Button(jan, text="Stop", command=stop).pack(side=LEFT, padx=5, pady=5)
btInc = Button(jan, text="+", command=inc)
btDec = Button(jan, text="-", command=dec)
btInc.pack(side=LEFT, padx=5, pady=5)
btDec.pack(side=LEFT, padx=5, pady=5)

# Coloca informações na tela sobre a posição da bolinha
can.create_text(10, h-40, text="posição de equilíbrio: y = -{0:.2f} m".format(l0), anchor=W)
info = can.create_text(10, h-20, text="posição atual: y = -{0:.2f} m".format(l0), anchor=W)

# cria os objetos na tela
ela = can.create_line(x, 0, x, S*(l0+A)) # cria a linha representando o elástico
circ = can.create_oval(x-S*r, S*y(l0+A)-S*r, x+S*r, S*y(l0+A)+S*r, outline="pink", fill="pink") # cria a esfera

# cria o vetor da força resultante
yi = l0 - k*A/2
yf = l0 + k*A/2
lnForce = can.create_line(x + 45, yi, x + 45, yf, arrow=FIRST)
txForce = can.create_text(x + 60, h/2, text="F = {0:.3} N".format(0.), anchor=W)
                
jan.after(1000, animate) # começa a animação
jan.mainloop() # entra no laço principal e aguarda os eventos
