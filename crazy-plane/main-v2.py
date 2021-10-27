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
AMARELO = ((255,255,0))
FPS = 120
clock = pygame.time.Clock()

#LOADING IMAGES
predios1_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
predios2_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
aviao_surface = pygame.image.load("crazy-plane/avioes/aviao-charles.png").convert_alpha()
stone_surface = pygame.image.load("crazy-plane/obstaculos/stone.png").convert_alpha()

#GAME NAME
pygame.display.set_caption('Crazy Plane')


#CLASS AVIAO
class Aviao:
    def __init__(self, vida, gasolina,  x, y):
        self.vida = vida
        self.gasolina = gasolina
        self.x = x
        self.y = y

class Foguete(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('crazy-plane/obstaculos/rocket_1.png'))
        self.sprites.append(pygame.image.load('crazy-plane/obstaculos/rocket_2.png'))
        self.sprites.append(pygame.image.load('crazy-plane/obstaculos/rocket_3.png'))
        self.sprites.append(pygame.image.load('crazy-plane/obstaculos/rocket_4.png'))
        self.sprites.append(pygame.image.load('crazy-plane/obstaculos/rocket_5.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual = self.atual + 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (54*2, 21*2))


#GAME SETTINGS
aviao = Aviao(3, 100, 30, 120)

x_obstaculo = 900
y_obstaculo = random.randint(50, 450)

x_obstaculo2 = 1350
y_obstaculo2 = random.randint(50, 450)

x_predios1 = 0
y_predios1 = 0

x_predios2 = 1800
y_predios2 = 0

gravidade = 0.1
movimento_aviao = 0

obstaculo1 = True
obstaculo2 = True

all_sprites = pygame.sprite.Group()
#INSTANCIANDO OBJETO
#foguete = Foguete(x_obstaculo, y_obstaculo)
#all_sprites.add(foguete)

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

    #ATUALIZANDO MOVIMENTO DOS PREDIOS
    screen.blit(predios1_surface,(x_predios1, y_predios1))
    screen.blit(predios2_surface,(x_predios2, y_predios2))

    #MOVIMENTO DOS OBSTACULOS
    if obstaculo1 == True:
        new_foguete = Foguete(x_obstaculo, y_obstaculo)
        all_sprites.add(new_foguete)
        obstaculo1 = False
    if x_obstaculo <= -60*2:
        obstaculo1 = True
        all_sprites.remove(new_foguete)
        y_obstaculo = random.randint(50, 450)
        x_obstaculo = 900
    x_obstaculo -= 5
    new_foguete.rect.topleft = x_obstaculo, y_obstaculo
    all_sprites.draw(screen)

    if obstaculo2 == True:
        screen.blit(stone_surface, (x_obstaculo2, y_obstaculo2))
        x_obstaculo2 -= 4
        if x_obstaculo2 <= -100:
            y_obstaculo2 = random.randint(50, 450)
            x_obstaculo2 = 950

    screen.blit(aviao_surface, (aviao.x, aviao.y))

    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)