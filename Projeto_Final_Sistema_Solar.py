""" Simulador do Sistema Solar
"""
# Importando funções necessárias para o programa
from visual import *
from visual.controls import *

# ***** Constantes usadas nos cálculos *****
G = 6.67408e-11
UA = 150e9
mT = 5.972e24
rT = 1e9
sc = 20
length = 31*UA
x1 = length * 0.9
y1 = length / 8 * 2
y2 = length / 8 * 4
y3 = length / 8 * 6

# Dicionário de informações
info = {"Sun":      "Sol\nmassa = 332900.MT kg \n raio = 695700 km.",
        "Mercury":  "Mercúrio\nmassa = 0,55.MT \n raio = 2440 km \n distância ao Sol = 0.307.UA",
        "Venus":    "Vênus\nmassa = 0,95.MT \n raio = 6052 km \n distância ao Sol = 0,718.UA",
        "Earth":    "Terra\nmassa = 6X10^24 \n raio = 6371 km \n distância ao Sol = 1,5X10^9",
        "Mars":     "Marte \n massa = 0,53.MT \n raio = 3390 km \n distância ao Sol = 1,381.UA",
        "Jupiter":  "Jupiter \n massa = 11,2.MT \n raio = 69911 km \n distância ao Sol = 4,95.UA",
        "Saturn":   "Saturno \n massa = 9,5.MT \n raio = 58232 km \n distância ao Sol = 9,024.UA",
        "Uranus":   "Urano \n massa = 4,1.MT \n raio = 25362 km \n distância ao Sol = 18,33.UA",
        "Neptune":  "Netuno \n massa = 3,9.MT \n raio = 24622 km \n distância ao Sol = 29,81.UA"
    }

# ***** Funções *****
# Criamos uma classe, uma classe herda funcionalidades. Nesse caso, da esfera.
class Celestial(sphere):
# Definimos uma função que cria o objeto, chamada quando chamamos a classe
    def __init__(self, name, radius, mass, position, velocity, color):
        self.name = name
        self.vel = velocity
        self.acc = vector(0., 0., 0.)
        sphere.__init__(self, radius=radius, mass=mass, pos=position, color=color, make_trail=True, interval=10)


# Definimos uma função para ajustar as velocidades centrípetas de cada planeta
    def centripetalvelocity(self,target):
        e = {"Mercury": 2.105, # Esses valores foram ajustados de modo que a excentricidade de cada planeta fosse a real
             "Venus": 1.838,   # Eles foram ajustados rodando o programa várias vezes e conferindo os valores
             "Earth": 1.852,             
             "Mars": 1.9585,
             "Jupiter": 1.895,
             "Saturn": 1.9,
             "Uranus": 1.889,
             "Neptune": 1.837
            }
        v = sqrt(G * target.mass / mag(self.pos-target.pos))
        uv = norm(self.pos-target.pos)
        d = rotate(uv,angle=pi/2,axis=(0,1,0))
        return v * d * (1 + e[self.name])

# Por último funções que controlam os botões
def play():
    global running, m1
    running = not running
    
def changedt(value):
    global dt
    dt = dt + value
    if dt > 1000: dt = 1000
    if dt < 10: dt = 10

def activ_menu(i):
    global planet, a, b
    planet = i
    a = b = mag(bodies[i].pos - bodies[0].pos)
    length = int(mag(bodies[i].pos) + UA)  # ajusta a tela para a orbita do planeta
    scene.range = length
    x1 = length * 0.9      # ajusta a posição das informações com as orbitas selecionadas
    y1 = length / 8 * 2
    y2 = length / 8 * 4
    y3 = length / 8 * 6
    exc.pos=(x1,0,y2)
    time.pos=(x1,0,y3)

    
    
planet=1 # Definindo um planeta inicial

# ***** Objetos de cena *****
# Criando a janela onde a animação é exibida        
scene = display(width=600, height=600, center=(0,0,0), forward=(0,-1,0), range=length, autoscale=False, ambient=0)
# Criando a janela complementar
c = controls(title='Escolha um planeta!', x=600, y=0, width=300, height=600, range=50)
# Criando os botões da janela auxiliar
pp = toggle(pos=(0,40,0), width=15, height=7, text1='Para', text0='Inicia', action=lambda: play())
bp = button(pos=(5,25,0), width=14, height=7, text='rápido', action=lambda: changedt(50))
bm = button(pos=(-10,25,0), width=14, height=7, text='devagar', action=lambda: changedt(-50))
m1 = menu(pos=(0,15,0), width=25, height=5, text='Planeta')
# Adicionando cada item ao menu
m1.items.append(('Mercúrio', lambda: activ_menu(1))) 
m1.items.append(('Venus',    lambda: activ_menu(2)))
m1.items.append(('Terra',    lambda: activ_menu(3))) 
m1.items.append(('Marte',    lambda: activ_menu(4)))
m1.items.append(('Jupiter',  lambda: activ_menu(5)))
m1.items.append(('Saturno',  lambda: activ_menu(6)))
m1.items.append(('Urano',    lambda: activ_menu(7)))
m1.items.append(('Netuno',   lambda: activ_menu(8)))

# Criando os labels onde aparecem os cálculos em tempo real
exc  = label(pos=(x1,0,y2), color=(1,1,0), text="e = NaN", opacity=0, box=0, xoffset=-1, line=0)
time = label(pos=(x1,0,y3), color=(1,1,0), text="t = 0.0", opacity=0, box=0, xoffset=-1, line=0)


# ***** Criando os corpos do sistema solar *****
bodies = []
bodies.append(Celestial("Sun",     rT,         332900*mT, (0., 0., 0.), vector(0., 0., 0.), color.yellow))
bodies.append(Celestial("Mercury", 0.38*rT*sc, 0.055*mT,  (0.307*UA , 0.), vector(0., 0., 0.), color.orange))
bodies.append(Celestial("Venus",   0.95*rT*sc, 0.815*mT,  (0.718*UA, 0.), vector(0., 0., 0.), color.white))
bodies.append(Celestial("Earth",   rT*sc,      mT,        (0.983*UA , 0., 0.), vector(0., 0., 0.), color.white))
bodies.append(Celestial("Mars",    0.53*rT*sc, 0.107*mT,  (1.381*UA , 0., 0.), vector(0., 0., 0.), color.red))
bodies.append(Celestial("Jupiter", 11.2*rT*sc, 317.8*mT,  (4.95*UA  , 0., 0.), vector(0., 0., 0.), color.orange))
bodies.append(Celestial("Saturn",  9.5*rT*sc,  95.16*mT,  (9.024*UA  , 0., 0.), vector(0., 0., 0.), color.white))
bodies.append(Celestial("Uranus",  4.1*rT*sc,  14.54*mT,  (18.33*UA  , 0., 0.), vector(0., 0., 0.), color.green))
bodies.append(Celestial("Neptune", 3.9*rT*sc,  17.15*mT,  (29.81*UA  , 0., 0.), vector(0., 0., 0.), color.blue))
# Adicionando velocidade aos corpos a partir da função de velocidade centrípeta
bodies[1].vel = bodies[1].centripetalvelocity(bodies[0])
bodies[2].vel = bodies[2].centripetalvelocity(bodies[0])
bodies[3].vel = bodies[3].centripetalvelocity(bodies[0])
bodies[4].vel = bodies[4].centripetalvelocity(bodies[0])
bodies[5].vel = bodies[5].centripetalvelocity(bodies[0])
bodies[6].vel = bodies[6].centripetalvelocity(bodies[0])
bodies[7].vel = bodies[7].centripetalvelocity(bodies[0])
bodies[8].vel = bodies[8].centripetalvelocity(bodies[0])
# Adicionando texturas a alguns planetas para diferenciá-los
bodies[3].trail_object.color=color.blue
bodies[3].material = materials.BlueMarble
bodies[8].material = materials.wood
bodies[4].material = materials.blazed
# Adicionando a luz do Sol que reflete nos planetas
light=local_light(pos=(0,0,0),color=color.white)


# ***** Laço principal *****
b = a = mag(bodies[planet].pos)  # Posição dos eixos da elipse da órbita de cada planeta
dt = 500      # dt não pode ser muito grande pois torna o método de Euler-Cromer impreciso
tt = 0
running = True
showing = False  # Quando o programa é aberto as informações ficam ocultas
objInfo = None
# Laço que faz o programa rodar
while True:
    if running:
        for i in range(len(bodies)):
            for j in range(i+1, len(bodies)):              
                dx = bodies[i].pos.x - bodies[j].pos.x                              # Calcula a nova posição em x, y e z de cada planeta
                dy = bodies[i].pos.y - bodies[j].pos.y                              # pelo método de Euler-Cromer
                dz = bodies[i].pos.z - bodies[j].pos.z
                dr = sqrt(dx*dx + dy*dy + dz*dz)                                    # Calcula o módulo da distância entre o Sol e o planeta
                bodies[i].acc += G * bodies[j].mass * vector(dx, dy, dz) / dr**3    # Calcula a nova aceleração de cada planeta 
                bodies[j].acc += G * bodies[i].mass * vector(dx, dy, dz) / dr**3    # pelo método de Euler-Cromer 
                bodies[i].vel += bodies[i].acc * dt
                bodies[j].vel += bodies[j].acc * dt
        # Calcula o período em dias de cada planeta
        tt += dt 
        time.text = "Tempo = %d dias. \n" % int(tt * 2.76 / 86400)  # Exibe na tela, com uma casa decimal
                                                                    # valor foi ajutado para mais próximo do real.
        for body in bodies:
            body.pos += body.vel * dt
            body.rotate(angle=dt*pi/7500, axis=(0,1,0))  # Roda cada planeta em torno de si
            body.acc = vector(0., 0., 0.)

        d = mag(bodies[planet].pos - bodies[0].pos)
        if d > a: a = d
        if d < b: b = d
        # Calcula e imprime na tela o valor da excentricidade de cada planeta.
        exc.text = "Excentricidade = %.4f  \nDistância ao Sol = %.2f UA" % (1 - 2 / (a/b + 1), d / UA)
    else:
        rate(50)
    # Se houve um clique do mouse    
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.click == 'left':
            if showing == True:    # mostra a informação do planeta clicado
                if scene.mouse.pick == objInfo:
                    continue
                else:
                    infolbl.visible = False
                    showing = False
            if scene.mouse.pick != None:
                objInfo = scene.mouse.pick
                infolbl = label(pos=objInfo.pos, text=info[objInfo.name])
                showing = True



    
    
    
