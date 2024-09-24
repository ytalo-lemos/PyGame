# Importar Bibliotecas
import pygame
from pygame.locals import *
from sys import exit

# Tamanho da janela
largura = 840
altura = 840

# Função para receber input com valor padrão
def get_input(message, default_value):
    try:
        value = float(input(message))
    except ValueError:
        value = default_value
    return value

# +++++++++++++++++++++++++++++++++++++++++++++
# Controle de posição
x1, x2, x3 = 160,320,480
y1, y2, y3 = 0.0, 0.0, 0.0
#a = float(input('Insira Valor de A: '))
g = 9.8  # Aceleração gravitacional
m = get_input("Digite o valor da massa (padrão: 1.0): ", 1.0)  # Massa das partículas
# Constante de Arrasto:
c1 = get_input("Digite o valor de arrasto para o círculo 1 (padrão: 0.01): ", 0.01)
c2 = get_input("Digite o valor de arrasto para o círculo 2 (padrão: 0.02): ", 0.02)
c3 = get_input("Digite o valor de arrasto para o círculo 3 (padrão: 0.03): ", 0.03)
# Velocidade Inicial:
v1 = 0
v2 = 0
v3 = 0
# Cor
cor1 = (0, 0, 255)
cor2 = (0, 255, 0)  
cor3 = (255, 0, 0)

texto_legenda = [
    ("Partícula 1", cor1),
    ("Partícula 2", cor2),
    ("Partícula 3", cor3)
]
# Posições da legenda
legenda_x = largura - 200
legenda_y = 20

# +++++++++++++++++++++++++++++++++++++++++++++

clock = pygame.time.Clock() # Frames

pygame.init() # Inicia janela
pygame.font.init() # Inicia o Sistema de Fontes

# Configuração da fonte para os números do eixo
fonte = pygame.font.SysFont('Arial', 20)

# Tamanho do grid
grid_size = 40  # Espaçamento entre linhas e colunas do grid

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Programa')
while True: # Programa fecha e o codigo para
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    dt = clock.tick(60) / 1000.0  # Delta de tempo no SI
    a1 = g - c1 * v1**2 / m  # Aceleração do círculo 1
    v1 += a1 * dt  # Atualiza a velocidade
    y1 += v1 * dt  # Atualiza a posição

    a2 = g - c2 * v2**2 / m  # Aceleração do círculo 2
    v2 += a2 * dt
    y2 += v2 * dt

    a3 = g - c3 * v3**2 / m  # Aceleração do círculo 3
    v3 += a3 * dt
    y3 += v3 * dt
    #pygame.draw.rect(tela,(255,0,0), (300,300,50,50))
    pygame.draw.circle(tela,(cor1),(int(x1),y1),20)
    pygame.draw.circle(tela,(cor2),(int(x2),y2),20)
    pygame.draw.circle(tela,(cor3),(int(x3),y3),20)
    #pygame.draw.line(tela,(0,255,0),(390,0),(390,600))
    if y1 and y2 and y3 >= altura:
        y1 = 0
        v1 = 0
    if y2 and y3 >= altura:
        y2 = 0
        v2 = 0
    if y3 >= altura:
        y3 = 0
        v3 = 0
    
     # Desenhar o grid
    for x in range(0, largura, grid_size):
        pygame.draw.line(tela, (115, 115, 115), (x, 0), (x, altura))  # Linhas verticais
    for y in range(0, altura, grid_size):
        pygame.draw.line(tela, (115, 115, 115), (0, y), (largura, y))  # Linhas horizontais

    pygame.draw.line(tela, (255, 255, 255), (50, 0), (50, altura), 2)

    # Desenhar os números do eixo
    num_divisoes = 10  # Quantidade de divisões no eixo
    step = altura / num_divisoes  # Espaçamento entre os números

    for i in range(num_divisoes + 1):
        pos_y = i * (altura / num_divisoes)  # Posição Y para cada número
        valor_altura = -int(i * step)  # Valor da altura (negativo conforme desce)
        texto = fonte.render(str(valor_altura), True, (255, 255, 255))
        tela.blit(texto, (10, pos_y - 10))  # Posição do número (espaçado à esquerda)

    # Desenhar a legenda no canto superior direito
    for i, (nome, cor) in enumerate(texto_legenda):
        pygame.draw.rect(tela, cor, (legenda_x, legenda_y + i * 30, 20, 20))  # Retângulo colorido
        texto = fonte.render(nome, True, (255, 255, 255))
        tela.blit(texto, (legenda_x + 30, legenda_y + i * 30))  # Texto ao lado do retângulo

    #y = y+1

    pygame.display.update() # Reinicia a janela sem parar