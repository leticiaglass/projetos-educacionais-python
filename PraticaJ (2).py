from visual import * # importando funções

w = 500
h = 500    # dimensões da janela
g = 9.81   # gravidade em m/s²
m=2.0      # massa da bola 
k= 0.5     # constante elástica da mola

# configuração da janela que mostrará a cena
scene=display(title='Sistema Massa-Mola', x=0, y=0, width=w, height=h, 
     center=(0,0,0), range=40, background=(0,0,0))

f=frame() # conjunto do pêndulo


# Esfera no teto, a rótula, onde a mola é pendurada ***
rr=1.5 
rot=sphere(frame=f,pos=(0,25,0),radius=rr,color=color.gray(0.8))
lm=20 # Comprimento da mola, em cm
fi=0


# Mola 
x,y,z=0,lm/2,0
mol=helix(frame=f,pos=(0,25-rr,0),axis=(0,y,0),radius=0.8, 
          thickness=0.4,coils=15,color=color.blue)

# Criação da bolinha
rb=3 # Raio da bolinha, em cm
y0=25-rb-rr
yequi=m*g/k
bol=sphere(frame=f,pos=(x,y0,z),radius=rb,color=color.green, opacity=0.5)

# Força Resultante
fr=-m*g-k*y
v_seta=arrow(pos=(x,y,z),axis=(0,fr/5,0),color=color.orange)

# Oscilação 
omega=(m/k)**(1/2)
dt=0.01 # intervalo de tempo

while True: 
    rate(100) 
    fi+=omega*dt        # Ângulo de oscilação
    A=y0                # Amplitude do movimento, entre y0 e 0
    y=A*cos(fi)         # Novos valores de y
    mol.axis=(x,y-y0,z) # Modificar o eixo da mola
    fr=-m*g-k*(y-yequi) # Calcula a força resultante para o novo y
    bol.pos.y=y         # Mover a bolinha
    v_seta.axis.y=fr    # Tamanho e orientação do vetor
    v_seta.pos.y=y      # Mover o  vetor
