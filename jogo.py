import random
import pygame
import alienigenas
import dificul
import time
import mainmenu
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from PPlay.sprite import *
from PPlay.window import *


janela = Window(800, 600)
janela.set_title("Space Invaders")

screen = pygame.display.set_mode((800, 600),0,32)

teclado = Window.get_keyboard()
GAME_SPEED = dificul.GAME_SPEED

fundo1 = GameImage("imagens/space.png")
fundo2 = GameImage("imagens/space.png")
fundo1.y = 0
fundo2.y = -fundo2.height
roll_speed = 50

nave = Sprite("assets/ship.png", 1)
nave.set_position((janela.width - nave.width)/2, (janela.height - nave.height))
nave_vidas = mainmenu.vidas_nave

velNave = 300
nave.direction = -1

bullets = [] 
nave.shoot_delay = 1/GAME_SPEED * 0.5

nave.shoot_tick = nave.shoot_delay

alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
enemy = Sprite("assets/RedInvader.png", 1)
enemy_speed = 200
enemy_direction = 1


enemy.shoot_delay = 1/GAME_SPEED
enemy.shoot_tick = enemy.shoot_delay
alien = 0

#Lista
rows = 4
cols = 7
alien_cooldown = 1000
last_alien_shoot = pygame.time.get_ticks()

GAME_STATE = 1
countdown = 3
last_count = pygame.time.get_ticks()

Pontu = 0


def create_aliens(rows, cols):
    for row in range(rows):
        for item in range(cols):
            alien = alienigenas.Aliens(150 + item * 75, 50 + row * 70)
            alien_group.add(alien)

            

def win():
    global matrix_x
    global matrix_y
    global GAME_STATE

    won = True

    
    if won: 
        GAME_STATE = 2 

def pontuacao():
    global Pontu
    while True:
        fundo1.draw()
        janela.draw_text("SUA PONTUAÇÃO FOI:", janela.width/2 - 70, janela.height/2, size=40, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
        janela.draw_text(str(Pontu), janela.width/2, janela.height/2 + 50, size=30, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
    



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



linhas = []
def bullet_ship_collision():
    global GAME_STATE
    global nave_vidas
    global countdown
    global Pontu
    global linhas
    for b in bullets:
        if b.direction == -1:
                check_enemy_collision(b)
    if pygame.sprite.spritecollide(nave, alien_bullet_group, True):
        nave_vidas -= 1
    if nave_vidas <= 0:
        nome = input("Digite seu nome: ")
        linhas.append(str(Pontu) + " - " + nome)
        linhas.sort()
        linhas.reverse()
        if len(linhas) > 5:
            linhas.pop()
        f = open("score.txt", "a")
        for linha in linhas:
            f.write(linha + "\n")
        f.close()
        print(linhas)
        nave_vidas = 3
        
        mainmenu.main_menu()



def check_enemy_collision(b):
    global alien_group
    global Pontu
    global rows
    global cols
    for row in range(rows):
        for column in range(cols):
            if pygame.sprite.spritecollide(b, alien_group, True):
                bullets.remove(b)
                alien_group.remove(alien)
                Pontu += 50
                if len(alien_group) == 0:
                    cols = cols + 1
                    create_aliens(4, cols)
                return


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
    global alien_bullet_group
    global countdown
    for b in bullets:
        b.draw()

    for row in range(rows):
        for column in range(cols):
            if enemy != 0:
                alien_group.draw(screen)
    if countdown == 0:           
        alien_group.update()
        alien_bullet_group.update()
    nave.draw()
    alien_bullet_group.draw(screen)
clock = pygame.time.Clock()



if GAME_STATE == 1:
    def game():
        global cols
        global rows
        create_aliens(rows, cols)
        running = True
        start_time = time.time()
        x = 1
        counter = 0
        global Pontu
        global alien_cooldown
        global last_alien_shoot
        global nave_vidas
        global countdown
        global last_count

        while running:
            time_now = pygame.time.get_ticks()
            Pontua = str(Pontu)
            counter+=1    

            if (time.time() - start_time) > x :
                counter = 0
                start_time = time.time()

            nave.move_key_x(velNave * janela.delta_time() * dificul.GAME_SPEED)

            if countdown == 0:
                if (time_now - 1000) > alien_cooldown and len(alien_bullet_group)< 5 and len(alien_group) >0:
                    attacking_alien = random.choice(alien_group.sprites())
                    alien_bullet = alienigenas.Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
                    alien_bullet_group.add(alien_bullet)
                    last_alien_shot = time_now

            if nave.x <= 0:           
                nave.x = janela.width - nave.width
            elif nave.x >= janela.width:
                nave.x = 0
            

            if teclado.key_pressed("A"):
                nave.x = nave.x - velNave*janela.delta_time()

            if teclado.key_pressed("D"):
                nave.x = nave.x + velNave*janela.delta_time() 

            scrolling(fundo1, fundo2, 100)
            clock.tick(60)
            win()
            update_counters()
            if countdown == 0:
                player_shoot()
                bullet_movement()
            bullet_ship_collision()
            bullet_bullet_collision()
            draw()
            janela.draw_text(Pontua, janela.width - 100, janela.height/10, size=30, color=(255,255,255), font_name="Arial", bold=False, italic=False)
            janela.draw_text(str(nave_vidas)+ " vidas", janela.width - 200, janela.height/10, size=30, color=(255,255,255), font_name="Arial", bold=False, italic=False)
            janela.draw_text("FPS: " + str(round(counter / (time.time() - start_time))), 50, janela.height/11, size=30, color=(255,255,255), font_name="Arial", bold=False, italic=False)
            if countdown > 0:
                janela.draw_text("SE PREPARE", janela.width/2 - 50, janela.height/2, size=30, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
                janela.draw_text(str(countdown), janela.width/2, janela.height/2 + 50, size=30, color=(255,255,255), font_name="Space_Invaders", bold=False, italic=False)
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -=1
                    last_count = count_timer

            janela.update()


