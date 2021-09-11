import pygame
import jogo
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from PPlay.sprite import *
from PPlay.window import *

janela = Window(800, 600)
janela.set_title("Space Invaders")

screen = pygame.display.set_mode((800, 600),0,32)

mouse = Window.get_mouse()

fundo1 = GameImage("imagens/space.png")
fundo2 = GameImage("imagens/space.png")

dificuldade = Sprite("imagens/dificuldade.png")

GAME_SPEED = 1


def difi():
    running = True
    while running:
        dificuldade.x = janela.width/2 - dificuldade.width/2
        dificuldade.y = 50
        facil = Sprite("imagens/facil.png")
        medio = Sprite("imagens/medio.png")
        dificil = Sprite("imagens/dificil.png")

        facil.x = janela.width/2 - facil.width/2
        facil.y = 170

        medio.x = janela.width/2 - medio.width/2
        medio.y = 300

        dificil.x = janela.width/2 - dificil.width/2
        dificil.y = 420


        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(janela.width/2 - facil.width/2, 170, 200, 50)
        if button1.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                jogo.game()
        button2 = pygame.Rect(janela.width/2 - medio.width/2, 300, 400, 50)
        if button2.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                GAME_SPEED = 3
                jogo.game()
        button3 = pygame.Rect(janela.width/2 - dificil.width/2, 420, 200, 50)
        if button3.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                jogo.game()
        fundo1.draw()
        dificuldade.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        janela.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
            
        pygame.display.update()
