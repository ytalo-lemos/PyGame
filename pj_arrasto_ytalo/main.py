import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Bibliotecas Utilizadas!

g=9.81  # Aceleração da Gravidade
m=1.0   # Massa da partícula (kg)
K=0.1   # Constante de resistência
n_v=[1,2,3]  # Diferentes valores de n
dt=0.01 # Passo de tempo
t_t=10  # Duração da simulação em segundos

def aceleracao(v,n): # Função para calcular a aceleração
    return g-(K/m)*v**n

def simulacao(n): # Função para realizar a simulação
    tempo=np.arange(0,t_t,dt)
    posicoes=np.zeros_like(tempo)
    velocidades = np.zeros_like(tempo)
    velocidade_i = 0.0  # Velocidade inicial

    for i in range(1,len(tempo)):
        velocidade_i += aceleracao(velocidade_i, n) * dt
        posicoes[i] = posicoes[i-1] + velocidade_i * dt
        velocidades[i] = velocidade_i  # Atualiza a lista de velocidades
    
    return tempo,posicoes,velocidade_i

fig,ax = plt.subplots() # Criação da figura para a animação
ax.set_xlim(0,t_t)
ax.set_ylim(0,100)
ax.grid(True)  # Ativa o grid no gráfico
line,=ax.plot([],[],lw=2)

def init(): # Função de inicialização da animação
    line.set_data([],[])
    return line,

def update(frame): # Função de atualização da animação
    n=n_v[frame%len(n_v)]  # Alterar o valor de n a cada iteração
    tempo,posicoes,_=simulacao(n)
    line.set_data(tempo,posicoes)
    ax.set_title(f"Animação com n = {n}")
    return line,

# Criação da animação
ani=FuncAnimation(fig,update,frames=len(n_v),init_func=init,blit=True,repeat=True,interval=1000)

# Exibe a animação
plt.show()