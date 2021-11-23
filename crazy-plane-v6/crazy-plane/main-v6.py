
# IMPORTANDO BIBLIOTECAS UTILIZADAS
from typing import overload
import pygame
import constantes
from pygame.locals import *
from sys import exit
import random

class Game:
    def __init__(self):
        # INICIALIZANDO PYGAME
        pygame.init()

        # MUSICA
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.01)

        # CRIANDO TELA
        self.screen = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA), 0, 32)
        self.tela_start = pygame.image.load('crazy-plane/background/tela_inicio.png').convert_alpha()
        self.tela_game_over = pygame.image.load('crazy-plane/background/game_over.png').convert_alpha()

        # NOME DO JOGO
        pygame.display.set_caption('CRAZY PLANE')

        # FRAMES POR SEGUNDO
        self.clock = pygame.time.Clock()

        # FONTE
        self.fonte = pygame.font.match_font(constantes.FONTE1)

    def atualizar_pontuacao(self):
        self.pontuacao = constantes.FONTE.render('Score '+ str(score), True, (constantes.BRANCO))

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.screen.blit(texto, texto_rect)

        pygame.display.flip()

# -- FASE 1
class Campo:
    def __init__(self):
        # -- CENÁRIO --
        self.grama = pygame.image.load('crazy-plane/background/chao-campo.png').convert_alpha()
        self.arvores = pygame.image.load('crazy-plane/background/arvores.png').convert_alpha()
        self.farm = pygame.image.load('crazy-plane/background/farm.png').convert_alpha()
        self.sun = pygame.image.load('crazy-plane/background/sun.png').convert_alpha()
        self.sun = pygame.transform.scale(self.sun, (128, 121))

# -- FASE 2
class Praia:
    def __init__(self):
        # -- CENÁRIO --
        self.agua = pygame.image.load('crazy-plane/background/praia-agua.png').convert_alpha()
        self.areia = pygame.image.load('crazy-plane/background/praia-areia.png').convert_alpha()


# -- FASE 3
class Cidade:
    def __init__(self):
        # -- CENÁRIO --
        self.predios_frente = pygame.image.load('crazy-plane/background/background.png').convert_alpha()
        self.predios_frente_rect = self.predios_frente.get_rect()
        self.predios_fundo = pygame.image.load('crazy-plane/background/background-fundo.png').convert_alpha()

        self.nuvem_1 = pygame.image.load("crazy-plane/background/cloud.png")
        self.nuvem_2 = pygame.image.load("crazy-plane/background/cloud_2.png")
        self.nuvem_3 = pygame.image.load("crazy-plane/background/cloud_3.png")

        self.lua_namefile = pygame.image.load("crazy-plane/background/moon.png")
        self.lua = pygame.transform.scale(self.lua_namefile, (32*2, 32*2))

game = Game()
cidade = Cidade()
praia = Praia()
campo = Campo()


class Aviao(pygame.sprite.Sprite):
    def __init__(self, pontos, vida,  x, y):
        pygame.sprite.Sprite.__init__(self)
        self.aviao = []
        self.aviao.append(pygame.image.load("crazy-plane/avioes/aviao-john.png"))
        self.aviao.append(pygame.image.load("crazy-plane/avioes/aviao-charles.png"))
        self.atual = random.randint(0,1)
        self.image = self.aviao[self.atual]
        self.rect = self.image.get_rect()

        self.pontos = pontos
        self.vida = vida
        self.x = x
        self.y = y
    
    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            print('colidiu')


class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("crazy-plane/background/2-cloud.png")

        self.rect = self.image.get_rect()
        self.rect.y = random.randint(10, 250)
        self.rect.x = 900
    
    def update(self):
        self.rect.x -= 1
        if self.rect.x < -200:
            self.rect.x = 900
            self.rect.y = random.randint(10, 250)

class NuvemMedia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("crazy-plane/background/2-cloud_2.png")

        self.rect = self.image.get_rect()
        self.rect.y = random.randint(10, 250)
        self.rect.x = 300
    
    def update(self):
        self.rect.x -= 1
        if self.rect.x < -200:
            self.rect.x = 900
            self.rect.y = random.randint(10, 250)

class NuvemPequena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("crazy-plane/background/2-cloud_3.png")

        self.rect = self.image.get_rect()
        self.rect.y = random.randint(10, 250)
        self.rect.x = 600
    
    def update(self):
        self.rect.x -= 1
        if self.rect.x < -200:
            self.rect.x = 900
            self.rect.y = random.randint(10, 250)
        

class Passaro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.passaros = []
        self.passaros.append(pygame.image.load('crazy-plane/obstaculos/bird/bird_1.png'))
        self.passaros.append(pygame.image.load('crazy-plane/obstaculos/bird/bird_2.png'))
        self.atual = 0
        self.image = self.passaros[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual += 0.1
        if self.atual >= len(self.passaros):
            self.atual = 0
        self.image = self.passaros[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

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

class Coconut(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.coconuts = []
        self.coconuts.append(pygame.image.load('crazy-plane\obstaculos\coconut\coconut_1.png'))
        self.coconuts.append(pygame.image.load('crazy-plane\obstaculos\coconut\coconut_2.png'))
        self.coconuts.append(pygame.image.load('crazy-plane\obstaculos\coconut\coconut_3.png'))
        self.coconuts.append(pygame.image.load('crazy-plane\obstaculos\coconut\coconut_4.png'))
        self.atual = 0
        self.image = self.coconuts[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.coconuts):
            self.atual = 0
        self.image = self.coconuts[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))

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

# ---------------- GAME SETTINGS -------------------
# DECLARANDO SCORE
score = 0

# -- AVIÃO
x = 30
y = 120
aviao = Aviao(score, 3, x, y)
gravidade = 0.1
movimento_aviao = 0

# -- OBSTÁCULOS
obstaculo_passaro = True
obstaculo_passaro_1 = True
obstaculo_foguete = True
obstaculo_pedra = True
obstaculo_bola = True
obstaculo_coconut = True

x_obstaculo_passaro = 900
y_obstaculo_passaro = random.randint(50, 450) # y aleatório para o obstáculo variar a posição verticalmente
x_obstaculo_passaro_1 = 1350
y_obstaculo_passaro_1 = random.randint(50, 450) 
x_obstaculo_foguete = 900 
y_obstaculo_foguete = random.randint(50, 450) 
x_obstaculo_pedra = 1350 
y_obstaculo_pedra = random.randint(50, 450)
x_obstaculo_bola = 900
y_obstaculo_bola = random.randint(50, 450)
x_obstaculo_coconut = 1350
y_obstaculo_coconut = random.randint(50, 450) 

# -- CENÁRIO FASE 1
x_grama1 = 0
y_grama1 = 0
x_grama2 = 1920
y_grama2 = 0

x_arvores1 = 0
y_arvores1 = 0
x_arvores2 = 1920
y_arvores2 = 0

x_farm = 0
y_farm = 0

x_sun = 1100
y_sun = 50

# -- CENÁRIO FASE 2
x_agua1 = 0
y_agua1 = 0
x_agua2 = 1252
y_agua2 = 0

x_areia1 = 0
y_areia1 = 0
x_areia2 = 1252
y_areia2 = 0

# -- CENÁRIO FASE 3
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

# -- SPRITES
sprites_obstaculos = pygame.sprite.Group()
sprites_cenario = pygame.sprite.Group()
nuvem = Nuvem()
nuvem_media = NuvemMedia()
nuvem_pequena = NuvemPequena()
sprites_cenario.add(nuvem)
sprites_cenario.add(nuvem_media)
sprites_cenario.add(nuvem_pequena)

start = True
jogo = True
game_over = False

while start:
    game.clock.tick(constantes.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            jogo = False
        if event.type == pygame.KEYUP:
            if event.key == K_SPACE:
                start = False
    
    game.mostrar_texto('Pressione START para iniciar', 32, constantes.BRANCO, constantes.LARGURA / 2, constantes.ALTURA / 2)
    game.screen.blit(game.tela_start, (0, 0))
       
if jogo == True:
    music = pygame.mixer.music.load('crazy-plane\sounds/background-music\Blazer Rail 2.wav')
    pygame.mixer.music.play(-1)

#LOOP GAME
while jogo:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                movimento_aviao = 0
                movimento_aviao -= 4
        
    if aviao.y <= 0:
        movimento_aviao = 0
        movimento_aviao += 3

    if aviao.y >= 500:
        game_over = True
        jogo = False

    '''
    # COLISÕES
    colisoes = pygame.sprite.spritecollide(aviao.rect, sprites_obstaculos, True)
    if colisoes:
        print('colidiu')
        
    print(aviao.y)
    for obstaculo in sprites_obstaculos:
        sprites_obstaculos.remove(obstaculo)
        aviao.collide(sprites_obstaculos)
        sprites_obstaculos.add(obstaculo)
        '''
    if score < 2000:
        background = game.screen.fill(constantes.AZULCLARO)
        # SOL
        x_sun -= 0.4
        if x_sun <= -250:
            x_sun = 1000
        game.screen.blit(campo.sun,(x_sun, y_sun))

        sprites_cenario.draw(game.screen)

        x_farm -= 1.5
        if x_farm <= -1920:
            x_farm = 300
        game.screen.blit(campo.farm, (x_farm, y_farm))

        x_arvores1 -= 2
        if x_arvores1 <= -1920:
            x_arvores1 = 1920
        x_arvores2 -= 2
        if x_arvores2 <= -1920:
            x_arvores2 = 1920
        game.screen.blit(campo.arvores, (x_arvores1, y_arvores2))
        game.screen.blit(campo.arvores, (x_arvores2, y_arvores2))

        x_grama1 -= 2.5
        if x_grama1 <= -1920:
            x_grama1 = 1920
        x_grama2 -= 2.5
        if x_grama2 <= -1920:
            x_grama2 = 1920
        game.screen.blit(campo.grama, (x_grama1, y_grama1))
        game.screen.blit(campo.grama, (x_grama2, y_grama2))

        if obstaculo_passaro == True:
            new_passaro = Passaro(x_obstaculo_passaro, y_obstaculo_passaro)
            sprites_obstaculos.add(new_passaro)
            obstaculo_passaro = False
        if x_obstaculo_passaro <= -64:
            obstaculo_passaro = True
            sprites_obstaculos.remove(new_passaro)
            y_obstaculo_passaro= random.randint(50, 450)
            x_obstaculo_passaro = 900
        x_obstaculo_passaro -= 3
        new_passaro.rect.topleft = x_obstaculo_passaro, y_obstaculo_passaro
        

        if obstaculo_passaro_1 == True:
            new_passaro_1 = Passaro(x_obstaculo_passaro_1, y_obstaculo_passaro_1)
            sprites_obstaculos.add(new_passaro_1)
            obstaculo_passaro_1 = False
        if x_obstaculo_passaro_1 <= -64:
            obstaculo_passaro_1 = True
            sprites_obstaculos.remove(new_passaro_1)
            y_obstaculo_passaro_1 = random.randint(50, 450)
            x_obstaculo_passaro_1 = 900
        x_obstaculo_passaro_1 -= 3
        new_passaro_1.rect.topleft = x_obstaculo_passaro_1, y_obstaculo_passaro_1
        sprites_obstaculos.draw(game.screen)

        # Renderizando as fontes do placar na tela
        game.atualizar_pontuacao()
        game.screen.blit(game.pontuacao, (700, 10))
        score += 1

        # MOVIMENTO AVIAO
        movimento_aviao += gravidade
        aviao.y += movimento_aviao

        # Renderizando o aviao
        game.screen.blit(aviao.image, (aviao.x, aviao.y))
        
        
    if score >= 2000 and score < 4000:
        sprites_obstaculos.remove(new_passaro)
        sprites_obstaculos.remove(new_passaro_1)
        background = game.screen.fill(constantes.AZULCLARO)

        sprites_cenario.draw(game.screen)

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
        game.screen.blit(praia.agua,(x_agua1, y_agua1))
        game.screen.blit(praia.agua,(x_agua2, y_agua2))
        game.screen.blit(praia.areia,(x_areia1, y_areia1))
        game.screen.blit(praia.areia, (x_areia2, y_areia2))

        if obstaculo_bola == True:
            new_bola = Bola(x_obstaculo_bola, y_obstaculo_bola)
            sprites_obstaculos.add(new_bola)
            obstaculo_bola = False
        if x_obstaculo_bola <= -64:
            obstaculo_bola = True
            sprites_obstaculos.remove(new_bola)
            y_obstaculo_bola = random.randint(50, 450)
            x_obstaculo_bola = 900
        x_obstaculo_bola -= 4
        new_bola.rect.topleft = x_obstaculo_bola, y_obstaculo_bola

        if obstaculo_coconut == True:
            new_coconut = Coconut(x_obstaculo_coconut, y_obstaculo_coconut)
            sprites_obstaculos.add(new_coconut)
            obstaculo_coconut = False
        if x_obstaculo_coconut <= -64:
            obstaculo_coconut = True
            sprites_obstaculos.remove(new_coconut)
            y_obstaculo_coconut = random.randint(50, 450)
            x_obstaculo_coconut = 900
        x_obstaculo_coconut -= 4
        new_coconut.rect.topleft = x_obstaculo_coconut, y_obstaculo_coconut
        sprites_obstaculos.draw(game.screen)


        # Renderizando as fontes do placar na tela
        game.atualizar_pontuacao()
        game.screen.blit(game.pontuacao, (700, 10))
        score += 1

        # Renderizando o aviao
        game.screen.blit(aviao.image, (aviao.x, aviao.y))
        
    if score >= 4000:
        sprites_obstaculos.remove(new_bola)
        sprites_obstaculos.remove(new_coconut)
        background = game.screen.fill(constantes.ROXO)

        sprites_cenario.remove(nuvem)
        sprites_cenario.remove(nuvem_media)
        sprites_cenario.remove(nuvem_pequena)
        sprites_cenario.draw(game.screen)

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
        # TAVA_AQUI
        
        # LUA
        x_lua -= 0.5
        if x_lua <= -250:
            x_lua = 1000
        game.screen.blit(cidade.lua,(x_lua, y_lua))

        # NUVENS
        x_nuvem -=1.5
        if x_nuvem <= -180:
            x_nuvem = 900
            y_nuvem = random.randint(10, 250)
        game.screen.blit(cidade.nuvem_1, (x_nuvem, y_nuvem))
        x_nuvem1 -=1.5
        if x_nuvem1 <= -180:
            x_nuvem1 = 900
            y_nuvem1 = random.randint(10, 250)
        game.screen.blit(cidade.nuvem_2,(x_nuvem1, y_nuvem1))
        x_nuvem2 -=1.5
        if x_nuvem2 <= -180:
            x_nuvem2 = 900
            y_nuvem2 = random.randint(10, 250)
        game.screen.blit(cidade.nuvem_3, (x_nuvem2, y_nuvem2))

        x_predios_fundo -= 2
        if x_predios_fundo <= -1800:
            x_predios_fundo = 1800
        game.screen.blit(cidade.predios_fundo, (x_predios_fundo, y_predios_fundo))
        x_predios_fundo2 -= 2
        if x_predios_fundo2 <= -1800:
            x_predios_fundo2 = 1800
        game.screen.blit(cidade.predios_fundo, (x_predios_fundo2, y_predios_fundo2))


        # ATUALIZANDO MOVIMENTO DOS PREDIOS
        game.screen.blit(cidade.predios_frente,(x_predios1, y_predios1))
        game.screen.blit(cidade.predios_frente,(x_predios2, y_predios2))

        # ------- MOVIMENTO DOS OBSTACULOS -----------
        if obstaculo_foguete == True:
            new_foguete = Foguete(x_obstaculo_foguete, y_obstaculo_foguete)
            sprites_obstaculos.add(new_foguete)
            obstaculo_foguete = False
        if x_obstaculo_foguete <= -60*2:
            obstaculo_foguete = True
            sprites_obstaculos.remove(new_foguete)
            y_obstaculo_foguete = random.randint(50, 450)
            x_obstaculo_foguete = 900
        x_obstaculo_foguete -= 6
        new_foguete.rect.topleft = x_obstaculo_foguete, y_obstaculo_foguete
        sprites_obstaculos.draw(game.screen)

        if obstaculo_pedra == True:
            new_pedra = Pedra(x_obstaculo_pedra, y_obstaculo_pedra)
            sprites_obstaculos.add(new_pedra)
            obstaculo_pedra = False
        if x_obstaculo_pedra <= -130:
            obstaculo_pedra = True
            sprites_obstaculos.remove(new_pedra)
            y_obstaculo_pedra = random.randint(50, 450)
            x_obstaculo_pedra = 950
        x_obstaculo_pedra -= 5
        new_pedra.rect.topleft = x_obstaculo_pedra, y_obstaculo_pedra
        sprites_obstaculos.draw(game.screen)
        # ---------------------------------------

        # Renderizando as fontes do placar na tela
        game.atualizar_pontuacao()
        game.screen.blit(game.pontuacao, (700, 10))
        score += 1

        # Renderizando o aviao
        game.screen.blit(aviao.image, (aviao.x, aviao.y))

    
    sprites_cenario.update()
    sprites_obstaculos.update()
    pygame.display.flip()
    game.clock.tick(constantes.FPS)

if game_over == True:
    pygame.mixer.music.stop()
    
while game_over == True:
    game.clock.tick(constantes.FPS)
    game.mostrar_texto('Grupo: Felipe de Carvalho, Matheus Guedes, Matheus Stefano e Vitor Olivetti', 20, constantes.BRANCO, constantes.LARGURA / 2, constantes.ALTURA - 30)
    game.mostrar_texto('SCORE', 24, constantes.BRANCO, constantes.LARGURA / 2, constantes.ALTURA / 2 - 30)
    game.mostrar_texto(str(score), 24, constantes.BRANCO, constantes.LARGURA / 2, constantes.ALTURA / 2)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    game.screen.blit(game.tela_game_over, (0, 0))
    game.screen.blit(aviao.image, (constantes.LARGURA / 2 + 70, constantes.ALTURA - 290))
