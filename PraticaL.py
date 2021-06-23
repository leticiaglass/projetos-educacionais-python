# Importando as funções
from visual import *  
from visual.controls import *
from visual.graph import * 

# Definindo a função do botão play/pause
def alavanca():
    global ini,anda,omega
    if ini==False:
        omega=(k/m)**(1/2)
        ini=True
    anda=not anda
    
# Definindo a função do botão restart    
def reiniciar():
    global ini,anda,th
    if not ini:
        return
    ini,anda=False,False
    bot.value=0
    th=0
    configurar()
    mol.axis=(0, l0, 0)            # Modificar o eixo da mola
    bol.pos.y = y0 + dy            # Mover a bolinha
    v_seta.axis.y=fr/(2*k)         # Tamanho e orientação do vetor
    v_seta.pos.y= y0 + dy          # Mover o  vetor
    reiniciargraph()               # reinicia também o gráfico

#Defindindo a função que reinicia o gráfico
def reiniciargraph():
    global x_curva,z_curva  # aqui usamos z porque y já está sendo usado 
    x_curva.gcurve.visible=False
    z_curva.gcurve.visible=False
    x_curva=gcurve(gdisplay=grafpos,color=cor_curva[0])
    z_curva=gcurve(gdisplay=grafpos,color=cor_curva[1])
    

# Definindo a função do botão que ajusta k
def ajustk():
    global k
    if ini==False:
        k=kSlid.value
        kLb.text=kStr.format(k)
        configurar()
    else:
        kSlid.value=k

# Definindo a função que reconthgura o sistema 
def configurar():
    global y0, l0, fr
    y0 = 25 - rr - rb - lm - (m*g/k)
    l0 = - lm / 4 - (m*g/k)
    fr = 0
    
def mover():
    global th, t
    th+=omega*dt                        # Ângulo de oscilação
    A = dy                              # Amplitude do movimento, entre y0 e 0
    y = A * cos(th)                     # Novos valores de y
    mol.axis=(x,l0-A+y,z)               # Modificar o eixo da mola
    fr = - m * g - k * (y0 + m*g/k + y) # Calcula a força resultante para o novo y
    bol.pos.y = y0 + y                  # Mover a bolinha
    v_seta.axis.y=fr/(2*k)              # Tamanho e orientação do vetor
    v_seta.pos.y= y0 + y                # Mover o  vetor
    t+=dt
    x_curva.plot(pos=(t,y))
    z_curva.plot(pos=(t,fr))

# Dados
g = 9.81  # m/s²
m = 1     # kg
k = 100.0 # N/m
lm = 20   # Comprimento da mola, em cm
dy = 0.75 * lm
th = 0
dt = 0.01 # Intervalo de tempo
rr = 1.5  # Raio da Rótula, em cm
rb = 3    # Raio da bolinha em cm
t = 0     # tempo


# Criando a janela de exibição
larg,alt=500,500  # dimensões da janela
# configuração da janela que mostrará a cena
scene=display(title='Sistema Massa-Mola',x=0,y=0,width=larg,height=alt,  
     center=(0,0,0), range=40, background=(0,0,0))

# Rótulo indicando o valor de k (adimensional)
kStr='Constante elástica={0:.4}' # Cadeia a ser formada
kLb=label(pos=(5,30,0), color=(0,2,0), text=kStr.format(k),
          opacity=0, box=0, line=0) # Rótulo

f=frame() # conjunto do pêndulo


# Janela de painel de controle
largc=150
contr=controls(title='Controls', x=larg, y=0, width=largc, height=alt,
               background=(0.,0.,0.), range=100)
ini,anda=False,False

# Botão play/pause
bot=toggle(pos=(0,-20), width=16, text1='Play', text0='Pause',
           action=lambda: alavanca())

# Botão restart
button(pos=(0,-70), width=30, height=16, text='Restart',
       color=(0.7,0.9,0.7),action=lambda: reiniciar())

# Slider 
kSlid=slider(pos=(0,+20), width=10, height=60, axis=(0,50,2.5), lenght=100,
             color=(0.,1.,0.), min=1.0, max=10.0, action=lambda: ajustk())
kSlid.value=k

# Gráficos
largg=500                            # largura da janela de gráfico
altg=300                             # altura da janela do gráfico
cor_curva=[color.white,color.orange] # cores
tmx = 15                             # tempo máximo do gráfico
pmx = 150                            # valor máximo das posições

# criar as janelas de gráficos
grafpos=gdisplay(title='Coords', x=0,y=alt,width=largg,height=altg,
                 xtitle="t", ytitle="y,F", xmin=0,xmax=tmx,ymin=-pmx,ymax=pmx)
grafpos.display.visible=True

# criar as curvas do gráfico
x_curva=gcurve(gdisplay=grafpos,color=cor_curva[0])
z_curva=gcurve(gdisplay=grafpos,color=cor_curva[1])


# objetos da animação
# Esfera no teto, a rótula, onde a mola é pendurada 
rot=sphere(frame=f,pos=(0,25,0),radius=rr,color=color.gray(0.8))

# Mola
x = 0
l0 = - lm / 4 - (m*g/k)
z = 0
mol=helix(frame=f,pos=(0,25-rr,0),axis=(0,l0,0),radius=0.8, 
          thickness=0.4,coils=15,color=color.yellow)
# Bolinha
y0 = 25 - rr - rb - lm - (m*g/k)
bol=sphere(frame=f,pos=(x,y0+dy,z),radius=rb,color=color.blue, opacity=0.5)

# Vetor força
fr=0
v_seta=arrow(pos=(x,y0+dy,z),axis=(0,fr/5,0),color=color.orange)

# Laço principal
while True:   # pêndulo oscila enquanto a janela estiver aberta
    rate(100) # não mais de 100 passos/segundo
    contr.interact()
    if anda:
        mover()
    
