import sys, pygame, os
from pygame.locals import *
import pygame_menu
import menu
import game
import random
import numpy as np
from array import *

class Game:
    def __init__(self):
        self.timer = 0
        self.screen = "pseudo_menu"
        self.map = "route01"
        self.pseudo = ""

newGame = Game()

pygame.init()

programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)

# Params du plateau
size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255


# Menu
while True:
    if newGame.screen == "pseudo_menu":
        menuScreen = pygame.display.set_mode([600, 600])
        pygame.mixer.music.load('songs/main-menu.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        menu.pseudo_menu(menuScreen, 600, newGame)
    elif newGame.screen == "main_menu":
        menuScreen = pygame.display.set_mode([600, 600])
        menu.main_menu(menuScreen, 600, newGame)
    elif newGame.screen == "list_map_menu":
        menuScreen = pygame.display.set_mode([600, 600])
        menu.list_map_menu(menuScreen, 600, newGame)
    elif newGame.screen == "stats_menu":
        menuScreen = pygame.display.set_mode([600, 600])
        menu.stats_menu(menuScreen, 600, newGame)
    elif newGame.screen ==  "game":
        gameScreen = pygame.display.set_mode([1125, 825])
        if newGame.map == "route01":
            pygame.mixer.music.load('songs/routes/route1.wav')
        elif newGame.map == "route101":
            pygame.mixer.music.load('songs/routes/route101.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        game.game(newGame, gameScreen)