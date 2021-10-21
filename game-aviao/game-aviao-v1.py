import pygame
from pygame.draw import ellipse
from pygame.locals import *
from sys import exit

pygame.init()

largura = 900
altura = 500
screen = pygame.display.set_mode((largura, altura), 0, 32)

azul_claro = ((173, 216, 230))
cor_diferente = ((48, 23, 45))


predios1_image_filename = 'background.png'
predios1 = pygame.image.load(predios1_image_filename).convert_alpha()
predios2_image_filename = 'background.png'
predios2 = pygame.image.load(predios2_image_filename).convert_alpha()

aviao_filename = "aviao.png"
aviao = pygame.image.load(aviao_filename).convert_alpha()


FPS = 60
clock = pygame.time.Clock()

pygame.display.set_caption('Fase 1')


x_aviao = 100
y_aviao = 100

x_predios1 = 0
y_predios1 = 0

x_predios2 = 1800
y_predios2 = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    x_predios1 -= 5
    if x_predios1 <= -1800:
        x_predios1 = 1800
    
    x_predios2 -= 5
    if x_predios2 <= -1800:
        x_predios2 = 1800

    
    background = screen.fill(cor_diferente)

    screen.blit(predios1,(x_predios1, y_predios1))
    screen.blit(predios2,(x_predios2, y_predios2))
    screen.blit(aviao, (x_aviao, y_aviao))



    pygame.display.update()
    clock.tick(FPS)