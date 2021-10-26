import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 900
altura = 500
screen = pygame.display.set_mode((largura, altura), 0, 32)

ceu_azul_claro = ((173, 216, 230))
ceu_roxo = ((48, 23, 45))


predios1_surface = pygame.image.load('background.png').convert_alpha()
predios2_surface = pygame.image.load('background.png').convert_alpha()
aviao_surface = pygame.image.load("aviao.png").convert_alpha()


FPS = 120
clock = pygame.time.Clock()

pygame.display.set_caption('Game')


x_aviao = 30
y_aviao = 120

x_predios1 = 0
y_predios1 = 0

x_predios2 = 1800
y_predios2 = 0

#Variaveis de jogo
gravidade = 0.1
movimento_aviao = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                movimento_aviao = 0
                movimento_aviao -= 5

    x_predios1 -= 3
    if x_predios1 <= -1800:
        x_predios1 = 1800
    
    x_predios2 -= 3
    if x_predios2 <= -1800:
        x_predios2 = 1800

    movimento_aviao += gravidade
    y_aviao += movimento_aviao 

    background = screen.fill(ceu_roxo)
    
    screen.blit(predios1_surface,(x_predios1, y_predios1))
    screen.blit(predios2_surface,(x_predios2, y_predios2))
    screen.blit(aviao_surface, (x_aviao, y_aviao))


    pygame.display.update()
    clock.tick(FPS)