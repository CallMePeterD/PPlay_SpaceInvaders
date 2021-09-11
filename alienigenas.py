import pygame
import jogo
from PPlay.window import *
from PPlay.sprite import *

vel = 5
velIni = 50 / vel
janela = Window(800, 600)

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/RedInvader.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        all_aliens = jogo.alien_group.sprites()
        for alien in all_aliens:
            if alien.rect.right >= janela.width:
                self.move_direction = -1
                self.rect.y += 5
            elif alien.rect.left <= 0:
                self.move_direction = 1
                self.rect.y += 5
                
        
class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("assets/Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2
        if self.rect.top > 600:
            self.kill()