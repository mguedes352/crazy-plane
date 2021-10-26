import pygame
from pygame.locals import *
from sys import exit
import random


pygame.init()

#SETTINGS
largura = 900
altura = 500
screen = pygame.display.set_mode((largura, altura), 0, 32)
AZULCLARO = ((173, 216, 230))
ROXO = ((48, 23, 45))
VERMELHO = ((255, 0, 0))
VERDE = ((0, 255, 0))
FPS = 120
clock = pygame.time.Clock()

#LOADING IMAGES
predios1_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
predios2_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
aviao_surface = pygame.image.load("crazy-plane/avioes/aviao-charles.png").convert_alpha()

#GAME NAME
pygame.display.set_caption('Crazy Plane')


#CLASS AVIAO
class Aviao:
    def __init__(self, vida, gasolina,  x, y):
        self.vida = vida
        self.gasolina = gasolina
        self.x = x
        self.y = y


#GAME SETTINGS
aviao = Aviao(3, 100, 30, 120)

x_obstaculo = 900
y_obstaculo = random.randint(20, 480)

x_predios1 = 0
y_predios1 = 0

x_predios2 = 1800
y_predios2 = 0

gravidade = 0.1
movimento_aviao = 0


#LOOP GAME
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                movimento_aviao = 0
                movimento_aviao -= 5

    
    background = screen.fill(ROXO)
    
    #MOVIMENTO PREDIOS
    x_predios1 -= 3
    if x_predios1 <= -1800:
        x_predios1 = 1800
    
    x_predios2 -= 3
    if x_predios2 <= -1800:
        x_predios2 = 1800

    #MOVIMENTO AVIAO
    movimento_aviao += gravidade
    aviao.y += movimento_aviao 


    screen.blit(predios1_surface,(x_predios1, y_predios1))
    screen.blit(predios2_surface,(x_predios2, y_predios2))


    if x_obstaculo <= 900:
        pygame.draw.circle(screen, VERDE, (x_obstaculo, y_obstaculo), 10)
        x_obstaculo -= 7
        if x_obstaculo <= 0:
            y_obstaculo = random.randint(20, 480)
            x_obstaculo = 900

    screen.blit(aviao_surface, (aviao.x, aviao.y))


    pygame.display.update()
    clock.tick(FPS)