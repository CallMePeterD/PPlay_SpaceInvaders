import random
import pygame
import jogo
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from PPlay.sprite import *
from PPlay.window import *

janela = Window(800,600)

def win():
    global matrix_x
    global matrix_y
    global GAME_STATE

    won = True

    
    if won: 
        GAME_STATE = 2 


def adjust_bullet(actor, bullet):
   
    x_fire = actor.x + (actor.width / 2) - (bullet.width / 2)

    if actor.direction == -1:
        y_fire = actor.y
    elif actor.direction == 1:
        y_fire = actor.y + actor.height - bullet.height

    bullet.x = x_fire
    bullet.y = y_fire

    bullet.direction = actor.direction

def shoot(shooter):
    
    shooter.shoot_tick = 0
 

    if shooter.direction == -1:
        b = Sprite("assets/Bullet.png", 1)
    elif shooter.direction == 1:
        b = Sprite("assets/Bullet.png", 1)
         

    adjust_bullet(shooter, b)
 
    bullets.append(b)


    
def scrolling(fundo1, fundo2, roll_speed):
    fundo1.y += roll_speed * janela.delta_time()
    fundo2.y += roll_speed * janela.delta_time()

    if fundo2.y >= 0:
        fundo1.y = 0
        fundo2.y = -fundo2.height

    fundo1.draw()
    fundo2.draw()

def update_counters():

    nave.shoot_tick += janela.delta_time()

def player_shoot():
    if teclado.key_pressed("SPACE"):
        if nave.shoot_tick > nave.shoot_delay:
            shoot(nave)

def bullet_movement():

    for b in bullets:
        b.move_y(200 * b.direction * janela.delta_time() * GAME_SPEED)
        if b.y < -b.height or b.y > janela.height + b.height:
            bullets.remove(b)




def bullet_ship_collision():
    global GAME_STATE

    for b in bullets:
        if b.direction == 1:
            if b.collided(alien_group):
                alien_group.remove(alien)

        elif b.direction ==1:
            if b.collided(player):
                GAME_STATE = 2



def bullet_bullet_collision():
    for b1 in bullets:
        if b1.direction == -1:
            for b2 in bullets:
                if b2.direction == 1:
                    if b1.collided(b2):
                        bullet.remove(b1)
                        bullet.remove(b2)
                        break

     

def draw():

    for b in bullets:
        b.draw()

   
    nave.draw()