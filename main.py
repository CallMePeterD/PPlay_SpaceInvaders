import pygame, time
import random
import jogo
import dificul
import ranki
import mainmenu
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sound import *
from PPlay.sprite import *
from PPlay.window import *

GAME_STATE = 0

while True:
    if GAME_STATE == 0:
        mainmenu.main_menu()
    janela.update()