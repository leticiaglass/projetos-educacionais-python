# Voce deve fazer um programa que pergunte ao usuario o alcance, a altura e a aceleração gravitacional
# e então retornar a velocidade inicial (em x e y) e o tempo de voo.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

print("Olá, esse programa calculará o alcance e a altura e o tempo de vooo para um lançamento obliquo a partir de uma dada velocidade.")

v0x = float(input("Por favor, entre com o valor para a velocidade inicial em x: "))
v0y = float(input("Por favor, entre com o valor para a velocidade inicial em y: "))

g = 9.8

# calculo do tempo de voo
t = 2 * v0y / g

# calculo do alcance
alc = v0x * t

# calculo da altura
alt = v0y ** 2 / (2 * g)

print("Os resultados são:")
print(alt, "é a altura máxima atingida")
print(alc, "é o alcance")


# ANIMAÇÂO

if "y" != input("Pressione y para ver a animação: "):
    exit()

Max = alt if alt > alc else alc
Max += Max * 0.1

# cria a figura necesária para exibir a animação
figure = plt.figure()
ax = figure.add_subplot(111, autoscale_on=False, xlim=(-Max/11, Max), ylim=(-Max/11, Max))
ax.grid() # exibe o grid 

# Cria um vetor de tempos entre 0 e t
tt = np.linspace(0, t, t * 10 + 1)
xx = np.zeros(len(tt))
yy = np.zeros(len(tt))

dt = t / len(tt)

# Cria a linha que servira para plotar os dados
line, = ax.plot([], [], "--")
head, = ax.plot([], [], "o")
labl = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# função responsavel por criar cada frame (frame de indice i) da animação
def animate(i):
    xx[i] = v0x * tt[i]
    yy[i] = v0y * tt[i] - (g / 2) * tt[i] ** 2
    
    line.set_data(xx[:i], yy[:i])
    head.set_data(xx[i], yy[i])
    labl.set_text('time = %.1fs' % tt[i])
    return line, head, labl
    
# apenas necessario    
def init():
    line.set_data([], [])
    head.set_data([], [])
    labl.set_text('')
    return line, head, labl

# cria a animação
anim = animation.FuncAnimation(figure, animate, len(tt),
                              interval=dt*1000, blit=True, init_func=init, repeat=True)

# exibe
plt.show()
