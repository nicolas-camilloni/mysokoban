import sys, pygame, os
import pygame_menu
import random

from array import *

# next fix : quand tu pousse un pokemon hors de la pokeball en étant sur une pokeball ouverte

class Game:
    def __init__(self, isStarted, pround):
        self.isStarted = isStarted
        self.pround = pround
        self.round = 0
        self.mode = "pvp"

    def startGame(self):
        if self.isStarted == False:
            self.isStarted = True

newGame = Game(False, 1)
pygame.init()
pygame.font.init()
pokegbfont = pygame.font.Font(os.path.join('PokemonGb-RAeo.ttf'), 24)
pokegbfontmini = pygame.font.Font(os.path.join('PokemonGb-RAeo.ttf'), 16)
pokefont = pygame.font.Font(os.path.join('PokemonSolidNormal-xyWR.ttf'), 24)


# Params du plateau
size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255

map = [
    [51, 0, 0, 4, 1, 1, 0, 0],
    [0, 0, 0, 4, 1, 0, 101, 0],
    [0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 101, 101, 101, 0, 0, 1],
    [4, 4, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 101, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

lastTry = [
    [51, 0, 0, 4, 1, 1, 0, 0],
    [0, 0, 0, 4, 1, 0, 101, 0],
    [0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 101, 101, 101, 0, 0, 1],
    [4, 4, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 101, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

resultMap = [
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

screen = pygame.display.set_mode(size)

rCount = True
lCount = True
dCount = True
uCount = True

def displayMap():
    i = 0
    j = 0
    for j in range (0, 8):
        for i in range (0, 8):
            if map[j][i] == 0:
                screen.blit(grassImage, (75*i, 75*j))
            elif map[j][i] == 1:
                screen.blit(wallImage, (75*i, 75*j))
            elif map[j][i] == 3:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseurImage, (75*i, 75*j))
            elif map[j][i] == 51:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1R1Image, (75*i, 75*j))
            elif map[j][i] == 52:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1R2Image, (75*i, 75*j))
            elif map[j][i] == 53:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1L1Image, (75*i, 75*j))
            elif map[j][i] == 54:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1L2Image, (75*i, 75*j))
            elif map[j][i] == 55:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1D1Image, (75*i, 75*j))
            elif map[j][i] == 56:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1D2Image, (75*i, 75*j))
            elif map[j][i] == 57:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1U1Image, (75*i, 75*j))
            elif map[j][i] == 58:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(dresseur1U2Image, (75*i, 75*j))
            elif map[j][i] == 4:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(openedPokeballImage, (75*i, 75*j))
            elif map[j][i] == 5:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(pokeballImage, (75*i, 75*j))
            elif map[j][i] == 101:
                screen.blit(grassImage, (75*i, 75*j))
                screen.blit(psyduckImage, (75*i, 75*j))
            i += 1
        i = 0
        j += 1

def checkWin():
    i = 0
    j = 0
    stop = True
    for j in range (0, 8):
        for i in range (0, 8):
            if map[j][i] > 100:
                # Pokémon détecté : partie pas fini
                stop = False
            i += 1
        i = 0
        j += 1
    if stop == True:
        textsurfaceggbig = pokefont.render('Vous avez gagné !', False, (51, 91, 255))
        textsurfacegg = pokefont.render('Vous avez gagné !', False, (255, 209, 51))
        textsurfacereset = pokegbfontmini.render('Appuie sur R pour restart', False, (51, 91, 255))
        screen.blit(textsurfaceggbig,(188,260))
        screen.blit(textsurfacegg,(190,260))
        screen.blit(textsurfacereset,(100,300))


# Mes images (point et croix)
dotImage = pygame.image.load("dot.png").convert_alpha()
crossImage = pygame.image.load("cross.png").convert_alpha()
grassImage = pygame.image.load("grass.png").convert_alpha()
wallImage = pygame.image.load("wall.png").convert_alpha()
psyduckImage = pygame.image.load("psyduck.png").convert_alpha()
dresseurImage = pygame.image.load("dresseur.png").convert_alpha()
openedPokeballImage = pygame.image.load("pokeball-open.png").convert_alpha()
pokeballImage = pygame.image.load("pokeball.png").convert_alpha()

# Player sprites
dresseur1R1Image = pygame.image.load("chars/dresseur1-r1.png").convert_alpha()
dresseur1R2Image = pygame.image.load("chars/dresseur1-r2.png").convert_alpha()
dresseur1L1Image = pygame.image.load("chars/dresseur1-l1.png").convert_alpha()
dresseur1L2Image = pygame.image.load("chars/dresseur1-l2.png").convert_alpha()
dresseur1D1Image = pygame.image.load("chars/dresseur1-d1.png").convert_alpha()
dresseur1D2Image = pygame.image.load("chars/dresseur1-d2.png").convert_alpha()
dresseur1U1Image = pygame.image.load("chars/dresseur1-u1.png").convert_alpha()
dresseur1U2Image = pygame.image.load("chars/dresseur1-u2.png").convert_alpha()


playerPosX = 0
playerPosY = 0


while True:

    mapSave = [
        [51, 0, 0, 4, 1, 1, 0, 0],
        [0, 0, 0, 4, 1, 0, 101, 0],
        [0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 101, 101, 101, 0, 0, 1],
        [4, 4, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1],
        [1, 4, 0, 0, 0, 101, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

    displayMap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN	:
            if event.key == 114:
                # Touche : R
                map = mapSave
                playerPosX = 0
                playerPosY = 0
                rCount = True
                lCount = True
                dCount = True
                uCount = True
                # pygame.display.flip()
            if event.key == 1073741906:
                # Touche : up
                print("up")
                if playerPosY > 0:
                    nextPlayerPosY = playerPosY-1
                    if map[nextPlayerPosY][playerPosX] == 5:
                        pokeballPosY = nextPlayerPosY
                        pokeballPosX = playerPosX
                        nextPokeballPosY = nextPlayerPosY-1
                        if pokeballPosY > 0:
                            # faire condition si deux pokeballs à côté
                            if map[nextPokeballPosY][pokeballPosX] == 0:
                                map[nextPokeballPosY][pokeballPosX] = 101
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if uCount:
                                    map[nextPlayerPosY][playerPosX] = 57
                                    uCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 58
                                    uCount = True
                                print(1)
                                playerPosY -= 1
                                print(map)
                            if map[nextPokeballPosY][pokeballPosX] == 4:
                                map[nextPokeballPosY][pokeballPosX] = 5
                                resultMap[nextPokeballPosY][pokeballPosX] = 2
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if uCount:
                                    map[nextPlayerPosY][playerPosX] = 57
                                    uCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 58
                                    uCount = True
                                print(1)
                                playerPosY -= 1
                    elif map[nextPlayerPosY][playerPosX] != 1 and map[nextPlayerPosY][playerPosX] != 3 and map[nextPlayerPosY][playerPosX] != 5 and map[nextPlayerPosY][playerPosX] < 101:
                        print(lastTry[playerPosY][playerPosX])
                        if mapSave[playerPosY][playerPosX] == 4:
                            if resultMap[playerPosY][playerPosX] == 2:
                                map[playerPosY][playerPosX] = 5
                            else:
                                map[playerPosY][playerPosX] = mapSave[playerPosY][playerPosX]
                        else:
                            map[playerPosY][playerPosX] = 0
                        if uCount:
                            map[nextPlayerPosY][playerPosX] = 57
                            uCount = False
                        else:
                            map[nextPlayerPosY][playerPosX] = 58
                            uCount = True
                        playerPosY -= 1
                    if map[nextPlayerPosY][playerPosX] > 100:
                        pokemonPosX = playerPosX
                        pokemonPosY = nextPlayerPosY
                        nextPokemonPosY = nextPlayerPosY-1
                        if pokemonPosY > 0:
                            if map[nextPokemonPosY][pokemonPosX] != 1 and map[nextPokemonPosY][pokemonPosX] != 3 and map[nextPokemonPosY][pokemonPosX] != 5 and map[nextPokemonPosY][pokemonPosX] < 101:
                                if map[nextPokemonPosY][pokemonPosX] == 4:
                                    map[nextPokemonPosY][pokemonPosX] = 5
                                    resultMap[nextPokemonPosY][pokemonPosX] = 2
                                else:
                                    map[nextPokemonPosY][pokemonPosX] = 101
                                if resultMap[playerPosY][playerPosX] == 1:
                                    map[playerPosY][playerPosX] = 4
                                else:
                                    map[playerPosY][playerPosX] = 0
                                if uCount:
                                    map[nextPlayerPosY][playerPosX] = 57
                                    uCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 58
                                    uCount = True
                                playerPosY -= 1
                lastTry = map
            if event.key == 1073741903:
                # Touche : right
                print("right")
                if playerPosX < 7:
                    nextPlayerPosX = playerPosX+1
                    if map[playerPosY][nextPlayerPosX] == 5:
                        pokeballPosX = nextPlayerPosX
                        pokeballPosY = playerPosY
                        nextPokeballPosX = nextPlayerPosX+1
                        if pokeballPosX < 7:
                            if map[pokeballPosY][nextPokeballPosX] == 0:
                                map[pokeballPosY][nextPokeballPosX] = 101
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if rCount:
                                    map[playerPosY][nextPlayerPosX] = 51
                                    rCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 52
                                    rCount = True
                                print(1)
                                playerPosX += 1
                                print(map)
                            if map[pokeballPosY][nextPokeballPosX] == 4:
                                map[pokeballPosY][nextPokeballPosX] = 5
                                resultMap[pokeballPosY][nextPokeballPosX] = 2
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if rCount:
                                    map[playerPosY][nextPlayerPosX] = 51
                                    rCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 52
                                    rCount = True
                                print(1)
                                playerPosX += 1
                    elif map[playerPosY][nextPlayerPosX] != 1 and map[playerPosY][nextPlayerPosX] != 3 and map[playerPosY][nextPlayerPosX] != 5 and map[playerPosY][nextPlayerPosX] < 101:
                        if mapSave[playerPosY][playerPosX] == 4:
                            if resultMap[playerPosY][playerPosX] == 2:
                                map[playerPosY][playerPosX] = 5
                            else:
                                map[playerPosY][playerPosX] = mapSave[playerPosY][playerPosX]
                        else:
                            map[playerPosY][playerPosX] = 0
                        if rCount:
                            map[playerPosY][nextPlayerPosX] = 51
                            rCount = False
                        else:
                            map[playerPosY][nextPlayerPosX] = 52
                            rCount = True
                        print(map[playerPosY][nextPlayerPosX])
                        print(2)
                        playerPosX += 1
                    if map[playerPosY][nextPlayerPosX] > 100:
                        pokemonPosX = nextPlayerPosX
                        pokemonPosY = playerPosY
                        nextPokemonPosX = nextPlayerPosX+1
                        if pokemonPosX < 7:
                            if map[pokemonPosY][nextPokemonPosX] != 1 and map[pokemonPosY][nextPokemonPosX] != 3 and map[pokemonPosY][nextPokemonPosX] != 5 and map[pokemonPosY][nextPokemonPosX] < 101:
                                if map[pokemonPosY][nextPokemonPosX] == 4:
                                    map[pokemonPosY][nextPokemonPosX] = 5
                                    resultMap[pokemonPosY][nextPokemonPosX] = 2
                                else:
                                    map[pokemonPosY][nextPokemonPosX] = 101
                                if resultMap[playerPosY][playerPosX] == 1:
                                    map[playerPosY][playerPosX] = 4
                                else:
                                    map[playerPosY][playerPosX] = 0
                                if rCount:
                                    map[playerPosY][nextPlayerPosX] = 51
                                    rCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 52
                                    rCount = True
                                print(3)
                                playerPosX += 1
                lastTry = map
            if event.key == 1073741905:
                # Touche : down
                print("down")
                if playerPosY < 7:
                    nextPlayerPosY = playerPosY+1
                    if map[nextPlayerPosY][playerPosX] == 5:
                        pokeballPosY = nextPlayerPosY
                        pokeballPosX = playerPosX
                        nextPokeballPosY = nextPlayerPosY+1
                        if pokeballPosY < 7:
                            if map[nextPokeballPosY][pokeballPosX] == 0:
                                map[nextPokeballPosY][pokeballPosX] = 101
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if dCount:
                                    map[nextPlayerPosY][playerPosX] = 55
                                    dCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 56
                                    dCount = True
                                print(1)
                                playerPosY += 1
                                print(map)
                            if map[nextPokeballPosY][pokeballPosX] == 4:
                                map[nextPokeballPosY][pokeballPosX] = 5
                                resultMap[nextPokeballPosY][pokeballPosX] = 2
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if dCount:
                                    map[nextPlayerPosY][playerPosX] = 55
                                    dCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 56
                                    dCount = True
                                print(1)
                                playerPosY += 1
                    elif map[nextPlayerPosY][playerPosX] != 1 and map[nextPlayerPosY][playerPosX] != 3 and map[nextPlayerPosY][playerPosX] != 5 and map[nextPlayerPosY][playerPosX] < 101:
                        print(lastTry[playerPosY][playerPosX])
                        if mapSave[playerPosY][playerPosX] == 4:
                            if resultMap[playerPosY][playerPosX] == 2:
                                map[playerPosY][playerPosX] = 5
                            else:
                                map[playerPosY][playerPosX] = mapSave[playerPosY][playerPosX]
                        else:
                            map[playerPosY][playerPosX] = 0
                        if dCount:
                            map[nextPlayerPosY][playerPosX] = 55
                            dCount = False
                        else:
                            map[nextPlayerPosY][playerPosX] = 56
                            dCount = True
                        playerPosY += 1
                    if map[nextPlayerPosY][playerPosX] > 100:
                        pokemonPosX = playerPosX
                        pokemonPosY = nextPlayerPosY
                        nextPokemonPosY = nextPlayerPosY+1
                        if pokemonPosY < 7:
                            if map[nextPokemonPosY][pokemonPosX] != 1 and map[nextPokemonPosY][pokemonPosX] != 3 and map[nextPokemonPosY][pokemonPosX] != 5 and map[nextPokemonPosY][pokemonPosX] < 101:
                                if map[nextPokemonPosY][pokemonPosX] == 4:
                                    map[nextPokemonPosY][pokemonPosX] = 5
                                    resultMap[nextPokemonPosY][pokemonPosX] = 2
                                else:
                                    map[nextPokemonPosY][pokemonPosX] = 101
                                if resultMap[playerPosY][playerPosX] == 1:
                                    map[playerPosY][playerPosX] = 4
                                else:
                                    map[playerPosY][playerPosX] = 0
                                if dCount:
                                    map[nextPlayerPosY][playerPosX] = 55
                                    dCount = False
                                else:
                                    map[nextPlayerPosY][playerPosX] = 56
                                    dCount = True
                                playerPosY += 1
                lastTry = map
            if event.key == 1073741904:
                # Touche : left
                print("left")
                if playerPosX > 0:
                    nextPlayerPosX = playerPosX-1
                    if map[playerPosY][nextPlayerPosX] == 5:
                        pokeballPosX = nextPlayerPosX
                        pokeballPosY = playerPosY
                        nextPokeballPosX = nextPlayerPosX-1
                        if pokeballPosX > 0:
                            if map[pokeballPosY][nextPokeballPosX] == 0:
                                map[pokeballPosY][nextPokeballPosX] = 101
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if lCount:
                                    map[playerPosY][nextPlayerPosX] = 53
                                    lCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 54
                                    lCount = True
                                print(1)
                                playerPosX -= 1
                                print(map)
                            if map[pokeballPosY][nextPokeballPosX] == 4:
                                map[pokeballPosY][nextPokeballPosX] = 5
                                resultMap[pokeballPosY][nextPokeballPosX] = 2
                                resultMap[pokeballPosY][pokeballPosX] = 1
                                map[playerPosY][playerPosX] = 0
                                if lCount:
                                    map[playerPosY][nextPlayerPosX] = 53
                                    lCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 54
                                    lCount = True
                                print(1)
                                playerPosX -= 1
                    elif map[playerPosY][nextPlayerPosX] != 1 and map[playerPosY][nextPlayerPosX] != 3 and map[playerPosY][nextPlayerPosX] != 5 and map[playerPosY][nextPlayerPosX] < 101:
                        print(resultMap[playerPosY][playerPosX])
                        if mapSave[playerPosY][playerPosX] == 4:
                            if resultMap[playerPosY][playerPosX] == 2:
                                map[playerPosY][playerPosX] = 5
                            else:
                                map[playerPosY][playerPosX] = mapSave[playerPosY][playerPosX]
                        else:
                            map[playerPosY][playerPosX] = 0
                        if lCount:
                            map[playerPosY][nextPlayerPosX] = 53
                            lCount = False
                        else:
                            map[playerPosY][nextPlayerPosX] = 54
                            lCount = True
                        playerPosX -= 1
                    if map[playerPosY][nextPlayerPosX] > 100:
                        pokemonPosX = nextPlayerPosX
                        pokemonPosY = playerPosY
                        nextPokemonPosX = nextPlayerPosX-1
                        if pokemonPosX > 0:
                            if map[pokemonPosY][nextPokemonPosX] != 1 and map[pokemonPosY][nextPokemonPosX] != 3 and map[pokemonPosY][nextPokemonPosX] != 5 and map[pokemonPosY][nextPokemonPosX] < 101:
                                if map[pokemonPosY][nextPokemonPosX] == 4:
                                    map[pokemonPosY][nextPokemonPosX] = 5
                                    resultMap[pokemonPosY][nextPokemonPosX] = 2
                                else:
                                    map[pokemonPosY][nextPokemonPosX] = 101
                                if lCount:
                                    map[playerPosY][nextPlayerPosX] = 53
                                    lCount = False
                                else:
                                    map[playerPosY][nextPlayerPosX] = 54
                                    lCount = True
                                if resultMap[playerPosY][playerPosX] == 1:
                                    map[playerPosY][playerPosX] = 4
                                else:
                                    map[playerPosY][playerPosX] = 0
                                playerPosX -= 1
                lastTry = map
    
    checkWin()
    pygame.display.set_caption("Sokoban")
    pygame.display.flip()