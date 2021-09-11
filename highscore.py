import pygame
import sys
from PPlay.window import *
from PPlay.gameimage import *



pygame.init()
  
clock = pygame.time.Clock()
  
janela = Window(800,600)
screen = pygame.display.set_mode([800, 600])
fundo = GameImage("imagens/space.png")

base_font = pygame.font.Font(None, 38)
user_text = ''
  
input_rect = pygame.Rect(janela.width/2 - 100, janela.height/2 - 100, 200, 50)
mouse = Window.get_mouse()

color_active = pygame.Color('darkgrey')

color_passive = pygame.Color('grey')
color = color_passive

active = False
  
while True:
    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(janela.width/2 - 100, janela.height/2 + 100, 200, 50)
        if button1.collidepoint((mx, my)):
            if (mouse.is_button_pressed(1)):
                print("apertado")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:  
           
            if event.key == pygame.K_BACKSPACE:
  
                user_text = user_text[:-1]
  
            
            else:
                user_text += event.unicode
      

    
  
    if active:
        color = color_active
    else:
        color = color_passive

    fundo.draw()
    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      

    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      

    input_rect.w = max(200, text_surface.get_width()+10)
    janela.draw_text("SALVAR", janela.width/2 - 50, janela.height/2, size=40, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)

    janela.update()