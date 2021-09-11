import pygame, time
import random
import jogo
import dificul
import ranki
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from PPlay.sprite import *
from PPlay.window import *

#Janela
janela = Window(800, 600)
janela.set_title("Space Invaders")

#inputs
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
click = False
#fundo
fundo1 = GameImage("imagens/space.png")
fundo2 = GameImage("imagens/space.png")
fundo1.y = 0
fundo2.y = -fundo1.height
roll_speed = 50
random.seed()

fps = 60




screen = pygame.display.set_mode((800, 600),0,32)

titulo = GameImage("imagens/titulo.png")
titulo.x = janela.width/2 - titulo.width/2

jogar = Sprite("imagens/jogar.png")
dificuldade = Sprite("imagens/dificuldade.png")
ranking = Sprite("imagens/ranking.png")
sair = Sprite("imagens/sair.png")

jogar.x = janela.width/2 - jogar.width/2
jogar.y = janela.height/2 + 2

dificuldade.x = janela.width/2 - dificuldade.width/2
dificuldade.y = janela.height/2 + 60

ranking.x = janela.width/2 - ranking.width/2
ranking.y = janela.height/2 + 120

sair.x = janela.width/2 - sair.width/2
sair.y = janela.height/2 + 180

clock = pygame.time.Clock()

GAME_STATE = 0
vidas_nave = 3

def main_menu():
    running = True
    start_time = time.time()
    x = 1
    counter = 0
    while running:
        counter += 1
        if (time.time() - start_time) > x :
            counter = 0
            start_time = time.time()
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(janela.width/2 - jogar.width/2, janela.height/2 + 2, 200, 50)
        if button1.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                jogo.game()
        button2 = pygame.Rect(janela.width/2 - dificuldade.width/2, janela.height/2 + 60, 400, 50)
        if button2.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                dificul.difi()
        button3 = pygame.Rect(janela.width/2 - ranking.width/2, janela.height/2 + 120, 200, 50)
        if button3.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                ranki.rank()
        button4 = pygame.Rect(janela.width/2 - sair.width/2, janela.height/2 + 180, 200, 50)
        if button4.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

 
        pygame.display.update()
        clock.tick(60)
        fundo1.draw()
        titulo.draw()
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()
        janela.draw_text("FPS: " + str(round(counter / (time.time() - start_time))), 50, janela.height/11, size=30, color=(255,255,255), font_name="Arial", bold=False, italic=False)
        janela.update()