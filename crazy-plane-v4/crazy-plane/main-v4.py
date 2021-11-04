
# IMPORTANDO BIBLIOTECAS UTILIZADAS
import pygame
from pygame.locals import *
from sys import exit
import random

# INICIALIZANDO PYGAME
pygame.init()

# -------------- SETTINGS ------------------

# -- CRIANDO SURFACE
largura = 900
altura = 500
screen = pygame.display.set_mode((largura, altura), 0, 32)

# -- CORES
AZULCLARO = ((173, 216, 230))
ROXO = ((48, 23, 45))
VERMELHO = ((255, 0, 0))
VERDE = ((0, 255, 0))
AMARELO = ((255, 255, 0))
BRANCO = ((255, 255, 255))

# -- FRAMES POR SEGUNDO
FPS = 120
clock = pygame.time.Clock()

# DECLARANDO A FONTE DO SCORE E A PONTUAÇÃO
font = pygame.font.SysFont('segoeuiblack', 32)
score = 0

# ---------- CARREGANDO IMAGENS -----------
# -- FASE 1

# -- CENÁRIO --
predios1_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
predios2_surface = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
predios_fundo_surface1 = pygame.image.load('crazy-plane/background/background-fundo.png').convert_alpha()
predios_fundo_surface2 = pygame.image.load('crazy-plane/background/background-fundo.png').convert_alpha()

# -- AVIÃO
aviao_surface = pygame.image.load("crazy-plane/avioes/aviao-charles.png").convert_alpha()
# -- NUVEM
nuvem_surface = pygame.image.load("crazy-plane/background/cloud.png")
nuvem_surface_1 = pygame.image.load("crazy-plane/background/cloud_2.png")
nuvem_surface_2 = pygame.image.load("crazy-plane/background/cloud_3.png")
# -- LUA
lua_surface = pygame.image.load("crazy-plane/background/moon.png")
lua = pygame.transform.scale(lua_surface, (32*2, 32*2))

# -- FASE 2
agua1_surface = pygame.image.load('crazy-plane/background/praia-agua.png').convert_alpha()
agua2_surface = pygame.image.load('crazy-plane/background/praia-agua.png').convert_alpha()
areia1_surface = pygame.image.load('crazy-plane/background/praia-areia.png').convert_alpha()
areia2_surface = pygame.image.load('crazy-plane/background/praia-areia.png').convert_alpha()

# -- NUVEM
nuvem_surface_3 = pygame.image.load("crazy-plane/background/2-cloud.png")
nuvem_surface_4 = pygame.image.load("crazy-plane/background/2-cloud_2.png")
nuvem_surface_5 = pygame.image.load("crazy-plane/background/2-cloud_3.png")

# -- NOME DO JOGO
pygame.display.set_caption('Crazy Plane')

# -- CLASSE AVIAO
class Aviao:
    def __init__(self, pontos, vida, gasolina,  x, y):
        self.pontos = pontos
        self.vida = vida
        self.gasolina = gasolina
        self.x = x
        self.y = y

# -- CLASSE PEDRA
class Pedra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pedras = []
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_1.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_1.5.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_2.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_2.5.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_3.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_3.5.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_4.png'))
        self.pedras.append(pygame.image.load('crazy-plane/obstaculos/stone/stone_4.5.png'))
        self.atual = 0
        self.image = self.pedras[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.pedras):
            self.atual = 0
        self.image = self.pedras[int(self.atual)]

# -- CLASSE FOGUETE
class Foguete(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.foguetes = []
        self.foguetes.append(pygame.image.load('crazy-plane/obstaculos/rocket/rocket_1.png'))
        self.foguetes.append(pygame.image.load('crazy-plane/obstaculos/rocket/rocket_2.png'))
        self.foguetes.append(pygame.image.load('crazy-plane/obstaculos/rocket/rocket_3.png'))
        self.foguetes.append(pygame.image.load('crazy-plane/obstaculos/rocket/rocket_4.png'))
        self.foguetes.append(pygame.image.load('crazy-plane/obstaculos/rocket/rocket_5.png'))
        self.atual = 0
        self.image = self.foguetes[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual = self.atual + 0.05
        if self.atual >= len(self.foguetes):
            self.atual = 0
        self.image = self.foguetes[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (54*2, 21*2))

class Bola(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bolas = []
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola0.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola1.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola2.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola3.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola4.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola5.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola6.png'))
        self.bolas.append(pygame.image.load('crazy-plane/obstaculos/bola/sprite_bola7.png'))
        self.atual = 0
        self.image = self.bolas[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.bolas):
            self.atual = 0
        self.image = self.bolas[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

# ---------------- GAME SETTINGS -------------------
# -- AVIÃO
aviao = Aviao(score, 3, 100, 30, 120)
gravidade = 0.1
movimento_aviao = 0

# -- OBSTÁCULOS 
obstaculo1 = True
obstaculo2 = True
obstaculo3 = True

x_obstaculo = 900 
y_obstaculo = random.randint(50, 450) # y aleatório para o obstáculo variar a posição verticalmente
x_obstaculo2 = 1350 
y_obstaculo2 = random.randint(50, 450)
x_obstaculo3 = 900
y_obstaculo3 = random.randint(50, 450)

# -- CENÁRIO FASE 1
x_predios1 = 0 # x do 1º blit da imagem
y_predios1 = 0
x_predios2 = 1800 # x do 2º blit da imagem
y_predios2 = 0

x_predios_fundo = 0
y_predios_fundo = 0
x_predios_fundo2 = 1800
y_predios_fundo2 = 0

x_nuvem = 900
y_nuvem = random.randint(10, 250)
x_nuvem1 = 300
y_nuvem1 = random.randint(10, 250)
x_nuvem2 = 600
y_nuvem2 = random.randint(10, 250)

x_lua = 1100
y_lua = 50

# -- CENÁRIO FASE 2
x_agua1 = 0
y_agua1 = 0
x_agua2 = 1252
y_agua2 = 0

x_areia1 = 0
y_areia1 = 0
x_areia2 = 1252
y_areia2 = 0

# -- SPRITES
all_sprites = pygame.sprite.Group()
all_sprites_level_2 = pygame.sprite.Group()

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
    if score <= 1000:
        background = screen.fill(ROXO)

        # MOVIMENTO PREDIOS
        x_predios1 -= 3
        if x_predios1 <= -1800:
            x_predios1 = 1800
        x_predios2 -= 3
        if x_predios2 <= -1800:
            x_predios2 = 1800

        # MOVIMENTO AVIAO
        movimento_aviao += gravidade
        aviao.y += movimento_aviao 

        # LUA
        x_lua -= 0.5
        if x_lua <= -250:
            x_lua = 1000
        screen.blit(lua,(x_lua, y_lua))

        # NUVENS
        x_nuvem -=1.5
        if x_nuvem <= -180:
            x_nuvem = 900
            y_nuvem = random.randint(10, 250)
        screen.blit(nuvem_surface, (x_nuvem, y_nuvem))
        x_nuvem1 -=1.5
        if x_nuvem1 <= -180:
            x_nuvem1 = 900
            y_nuvem1 = random.randint(10, 250)
        screen.blit(nuvem_surface_1,(x_nuvem1, y_nuvem1))
        x_nuvem2 -=1.5
        if x_nuvem2 <= -180:
            x_nuvem2 = 900
            y_nuvem2 = random.randint(10, 250)
        screen.blit(nuvem_surface_2, (x_nuvem2, y_nuvem2))

        x_predios_fundo -= 2
        if x_predios_fundo <= -1800:
            x_predios_fundo = 1800
        screen.blit(predios_fundo_surface1, (x_predios_fundo, y_predios_fundo))
        x_predios_fundo2 -= 2
        if x_predios_fundo2 <= -1800:
            x_predios_fundo2 = 1800
        screen.blit(predios_fundo_surface2, (x_predios_fundo2, y_predios_fundo2))


        # ATUALIZANDO MOVIMENTO DOS PREDIOS
        screen.blit(predios1_surface,(x_predios1, y_predios1))
        screen.blit(predios2_surface,(x_predios2, y_predios2))

        # ------- MOVIMENTO DOS OBSTACULOS -----------
        if obstaculo1 == True:
            new_foguete = Foguete(x_obstaculo, y_obstaculo)
            all_sprites.add(new_foguete)
            obstaculo1 = False
        if x_obstaculo <= -60*2:
            obstaculo1 = True
            all_sprites.remove(new_foguete)
            y_obstaculo = random.randint(50, 450)
            x_obstaculo = 900
        x_obstaculo -= 4
        new_foguete.rect.topleft = x_obstaculo, y_obstaculo
        all_sprites.draw(screen)

        if obstaculo2 == True:
            new_pedra = Pedra(x_obstaculo2, y_obstaculo2)
            all_sprites.add(new_pedra)
            obstaculo2 = False
        if x_obstaculo2 <= -100:
            obstaculo2 = True
            all_sprites.remove(new_pedra)
            y_obstaculo2 = random.randint(50, 450)
            x_obstaculo2 = 950
        x_obstaculo2 -= 3
        new_pedra.rect.topleft = x_obstaculo2, y_obstaculo2
        all_sprites.draw(screen)
        # ---------------------------------------

        # Renderizando as fontes do placar na tela
        pontuacao = font.render('Score '+ str(score), True, (BRANCO))
        screen.blit(pontuacao, (700, 10))
        score += 1

        # Renderizando o aviao
        screen.blit(aviao_surface, (aviao.x, aviao.y))

    if score >= 1000:
        background = screen.fill(AZULCLARO)

        # NUVENS
        x_nuvem -=1.5
        if x_nuvem <= -180:
            x_nuvem = 900
            y_nuvem = random.randint(10, 250)
        screen.blit(nuvem_surface_3, (x_nuvem, y_nuvem))
        x_nuvem1 -=1.5
        if x_nuvem1 <= -180:
            x_nuvem1 = 900
            y_nuvem1 = random.randint(10, 250)
        screen.blit(nuvem_surface_4,(x_nuvem1, y_nuvem1))
        x_nuvem2 -=1.5
        if x_nuvem2 <= -180:
            x_nuvem2 = 900
            y_nuvem2 = random.randint(10, 250)
        screen.blit(nuvem_surface_5, (x_nuvem2, y_nuvem2))

        # MOVIMENTO PRAIA
        x_agua1 -= 2
        if x_agua1 <= -1252:
            x_agua1 = 1252
        x_agua2 -= 2
        if x_agua2 <= -1252:
            x_agua2 = 1252

        x_areia1 -= 3
        if x_areia1 <= -1252:
            x_areia1 = 1252
        x_areia2 -= 3
        if x_areia2 <= -1252:
            x_areia2 = 1252

        # MOVIMENTO AVIAO
        movimento_aviao += gravidade
        aviao.y += movimento_aviao

        # ATUALIZANDO MOVIMENTO DA PRAIA
        screen.blit(agua1_surface,(x_agua1, y_agua1))
        screen.blit(agua2_surface,(x_agua2, y_agua2))
        screen.blit(areia1_surface,(x_areia1, y_areia1))
        screen.blit(areia2_surface, (x_areia2, y_areia2))

        if obstaculo3 == True:
            new_bola = Bola(x_obstaculo3, y_obstaculo3)
            all_sprites_level_2.add(new_bola)
            obstaculo3 = False
        if x_obstaculo3 <= -60*2:
            obstaculo3 = True
            all_sprites_level_2.remove(new_bola)
            y_obstaculo3 = random.randint(50, 450)
            x_obstaculo3 = 900
        x_obstaculo3 -= 4
        new_bola.rect.topleft = x_obstaculo3, y_obstaculo3
        all_sprites_level_2.draw(screen)

        # Renderizando as fontes do placar na tela
        pontuacao = font.render('Score '+ str(score), True, (BRANCO))
        screen.blit(pontuacao, (700, 10))
        score += 1

        # Renderizando o aviao
        screen.blit(aviao_surface, (aviao.x, aviao.y))

    all_sprites.update()
    all_sprites_level_2.update()
    pygame.display.flip()
    clock.tick(FPS)