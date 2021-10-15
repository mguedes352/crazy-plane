import pygame
from pygame.locals import *
from sys import exit

pygame.init()

azul_claro = ((173, 216, 230))

largura = 800
altura = 600
screen = pygame.display.set_mode((largura, altura), 0, 32)

nuvens1_filename = 'nuvem1.png'
nuvens1 = pygame.image.load(nuvens1_filename).convert_alpha()
nuvens2_filename = 'nuvem2.png'
nuvens2 = pygame.image.load(nuvens2_filename).convert_alpha()

FPS = 60
clock = pygame.time.Clock()

x1 = -40
x2 = 100
x3 = 550
width_rect = 70
height_rect = 15

x_nuvens1 = 0
y_nuvens1 = 0

x_nuvens2 = 0
y_nuvens2 = -600


direction1 = 'right'
direction2 = 'right'
direction3 = 'right'
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if direction1 == 'right':
        x1 += 3
        if x1 >= largura-width_rect:
            direction1 = 'left'
    elif direction1 == 'left':
        x1 -= 3
        if x1 <= 0:
            direction1 = 'right'
    if direction2 == 'right':
        x2 += 5
        if x2 >= largura-width_rect:
            direction2 = 'left'
    elif direction2 == 'left':
        x2 -= 5
        if x2 <= 0:
            direction2 = 'right'
    if direction3 == 'right':
        x3 += 4
        if x3 >= largura-width_rect:
            direction3 = 'left'
    elif direction3 == 'left':
        x3 -= 4
        if x3 <= 0:
            direction3 = 'right'
    if y_nuvens1 >= altura:
        y_nuvens1 = -600
    y_nuvens1 += 1
    if y_nuvens2 >= altura:
        y_nuvens2 = -600
    y_nuvens2 += 1

    screen.fill(azul_claro)
    screen.blit(nuvens1, (x_nuvens1, y_nuvens1))
    screen.blit(nuvens2, (x_nuvens2, y_nuvens2))

    pygame.draw.rect(screen, (255,0,0), (x1, 500, width_rect, height_rect))
    pygame.draw.rect(screen, (255,0,0), (x2, 350, width_rect, height_rect))
    pygame.draw.rect(screen, (255,0,0), (x3, 200, width_rect, height_rect))



    pygame.display.update()
    clock.tick(FPS)