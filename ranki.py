import pygame

from PPlay.window import *
from PPlay.gameimage import *



janela = Window(800, 600)

fundo1 = GameImage("imagens\space.png")


running= True

def rank():
    running = True

    
    while running:
        fundo1.draw()
        n = 200
        janela.draw_text("RANKING", janela.width/2 - 100, janela.height/ 2 - 200, size=30, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
        with open("score.txt", "r") as file:
            for line in file:
                janela.draw_text(line, 300, n, size=30, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
                n += 50
        janela.update()