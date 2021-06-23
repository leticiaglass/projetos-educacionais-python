from tkinter import *  # Importando o módulo tk
from math import * 


# Definindo a função que age quando o botão do mouse é pressionado
def mouse_apertado(evento):
    global dmke,booSelec,carSelec,xa,ya # variáveis globais
    
    xa,ya=evento.x,evento.y
    encl=anim.find_enclosed(xa-40,ya-40,xa+40,ya+40)
    
    for e in encl:
        if e in dmke:
            booSelec=True 
            carSelec=anim.gettags(e)[0]


# Definindo a função que age quando o botão é solto
def mouse_solto(evento):
    global booSelec
    booSelec=False

# Definindo a função que age quando o cursor do mouse é movido enquanto pressionado
def mouse_movido(evento):
    global booSelec,carSelec,xa,ya 

    if booSelec:
        xe,ye=evento.x,evento.y
        dx,dy=xe-xa,ye-ya
        pm[int(carSelec)][1]+=dy
        desenhar()
        xa,ya=xe,ye

# Definindo a função que cria os objetos
def desenhar():
    global pm,r,mke,dmke
    anim.delete(ALL)
    m,ke,xf,yf=float(mke[0]),float(mke[1]),float(pm[1][0]),float(pm[1][1])

    if m<9 or m>12: # Definindo limites
        err=Tk()
        err.title("Erro")
        er=Canvas(err, width=400, height=70, bg='white')
        er.pack(side=TOP, padx=3, pady=3)
        er.create_text(20, 35, text="Por favor digite um valor entre 9 e 12kg para a massa.", anchor=W)
        
    elif ke<0.3 or ke>0.6:
        err=Tk()
        err.title("Erro")
        er=Canvas(err, width=400, height=70, bg='white')
        er.pack(side=TOP, padx=3, pady=3)
        er.create_text(20, 35, text="Por favor digite um valor entre 0.3 e 0.6 N/m para a constante elástica", anchor=W)

    else:
        yeq=((m*g)/ke)
        A=yeq-yf
        fa=(ke/m)**1/2
        fr=(m*g)-((ke*(yf)))
        Ue=0.5*ke*((yf-yeq)**(1/2))
        h=(Ue)/(m*g)
        Ug=m*g*h
        E=Ug-Ue
        if yf>=0 and yf<100: # para o elastico não ficar frouxo
            booSelec=False
            elastico=anim.create_line(200,1,200,yf,width=2,fill='yellow')
            dmke[0]=anim.create_oval(xf-r,yf-r,xf+r,yf+r,tags=str(1),fill="darkblue") 
            text=anim.create_text(280,20,text="O elástico não pode ficar frouxo.",anchor=W)
            booSelec=False
            
        elif yf>=(yeq-100) and yf<yeq: # intervalo em que os referenciais trocaram, então as equações não servem
            elastico=anim.create_line(200,1,200,yf,width=2,fill='yellow')
            dmke[0]=anim.create_oval(xf-r,yf-r,xf+r,yf+r,tags=str(1),fill="darkblue")
            setinha=anim.create_line(200,yf, 200,yf+fr,fill='red',arrow = LAST)
            text=anim.create_text(280,20,text="A Amplitude é {0:3g}m".format(fr),anchor=W)
            
        elif yf>=yeq and yf<=380: # intervalo válido para as equações anteiores
            elastico=anim.create_line(200,1,200,yf,width=2,fill='yellow')
            dmke[0]=anim.create_oval(xf-r,yf-r,xf+r,yf+r,tags=str(1),fill="darkblue")
            setinha=anim.create_line(200,yf, 200,yf+fr,fill='red',arrow = LAST)
            text=anim.create_text(280,20,text="A Amplitude em relação ao ponto de equilíbrio é {0:3g}m".format(fr),anchor=W)
            text=anim.create_text(280,40,text="A Energia Potencial Gravitacional é {0:3g}J".format(Ug),anchor=W)
            text=anim.create_text(280,60,text="A Energia Potencial Elástica é {0:3g}J".format(Ue),anchor=W)
            text=anim.create_text(280,80,text="A Energia Potencial Total é {0:3g}J".format(E),anchor=W)
        else: # fora da visualização
            booSelec=False
            elastico=anim.create_line(200,1,200,yf,width=2,fill='yellow')
            dmke[0]=anim.create_oval(xf-r,yf-r,xf+r,yf+r,tags=str(1),fill="darkblue") 

# Função para quando novos dados são digitados
def novosdados (evento):
    global mke
    for i in range (0,2):
        mke[i]= float (mkeEntr[i].get())
        desenhar ()

# Valores usados no programa
g=9.8
esc=0.05
pm=[[200.,200.],[200.,200.]]
m=10
ke=0.49
r=20
rc=5
mke=[10,0.49] # valores das  constantes m= mke[0] ke=mke[1]
dmke=[0,0]
booSelec=False

# Criando e nomenando a janela
jan=Tk()
jan.title("Energias potenciais de uma massa pendurada por um elástico - Leticia Glass.")
anim=Canvas(jan,width=600,height=400,bg="white")
anim.grid(column=1,row=1,columnspan=4)
anim.bind("<Button-1>",mouse_apertado)
anim.bind("<Button1-Motion>",mouse_movido)
anim.bind("<Button1-ButtonRelease>",mouse_solto)
mkeRot = []
mkeEntr = []
mkeVar = []
nomevar=["Massa (entre 9kg e 12kg):","Constante elástica (entre 0.3N/m e 0.6N/m ):"]
for i in range (0,2):
    mkeRot.append (Label(jan, text=nomevar[i]))
    mkeRot [i].grid (column=1+i, row=2, sticky=E)
    mkeVar.append (StringVar ())
    mkeVar [i].set (str (mke[i]))
    mkeEntr.append (Entry(jan, textvariable=mkeVar [i]))
    mkeEntr [i] . grid (column=2*(1+i), row=2, sticky=W)
    mkeEntr [i] . bind ("<Return>", novosdados)
desenhar()
jan.mainloop()
