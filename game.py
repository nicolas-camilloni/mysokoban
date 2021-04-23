from copy import copy, deepcopy
import pygame, os
import mysql.connector

def game(newGame, screen):

    pokegbfont = pygame.font.Font(os.path.join('PokemonGb-RAeo.ttf'), 24)
    pokegbfontmini = pygame.font.Font(os.path.join('PokemonGb-RAeo.ttf'), 16)
    pokegbfontchrono = pygame.font.Font(os.path.join('PokemonGb-RAeo.ttf'), 20)
    pokefont = pygame.font.Font(os.path.join('PokemonSolidNormal-xyWR.ttf'), 24)

    # Mes textures
    grassImage = pygame.image.load("tiles/grass.png").convert_alpha()
    wallImage = pygame.image.load("tiles/wall.png").convert_alpha()
    dresseurImage = pygame.image.load("tiles/dresseur.png").convert_alpha()
    openedPokeballImage = pygame.image.load("tiles/pokeball-open.png").convert_alpha()
    pokeballImage = pygame.image.load("tiles/pokeball.png").convert_alpha()
    waterUpImage = pygame.image.load("tiles/water-up.png").convert_alpha()
    waterDownImage = pygame.image.load("tiles/water-down.png").convert_alpha()
    waterLeftImage = pygame.image.load("tiles/water-left.png").convert_alpha()
    waterRightImage = pygame.image.load("tiles/water-right.png").convert_alpha()
    waterHorizonImage = pygame.image.load("tiles/water-horizon.png").convert_alpha()
    waterVerticalImage = pygame.image.load("tiles/water-vertical.png").convert_alpha()

    # Pokemons
    psyduckImage = pygame.image.load("pokemons/psyduck.png").convert_alpha()
    pikachuImage = pygame.image.load("pokemons/pikachu.png").convert_alpha()
    arcaninImage = pygame.image.load("pokemons/arcanin.png").convert_alpha()
    arckoImage = pygame.image.load("pokemons/arcko.png").convert_alpha()
    dracaufeuImage = pygame.image.load("pokemons/dracaufeu.png").convert_alpha()

    # Sprites joueur
    dresseur1R1Image = pygame.image.load("chars/dresseur1-r1.png").convert_alpha()
    dresseur1R2Image = pygame.image.load("chars/dresseur1-r2.png").convert_alpha()
    dresseur1L1Image = pygame.image.load("chars/dresseur1-l1.png").convert_alpha()
    dresseur1L2Image = pygame.image.load("chars/dresseur1-l2.png").convert_alpha()
    dresseur1D1Image = pygame.image.load("chars/dresseur1-d1.png").convert_alpha()
    dresseur1D2Image = pygame.image.load("chars/dresseur1-d2.png").convert_alpha()
    dresseur1U1Image = pygame.image.load("chars/dresseur1-u1.png").convert_alpha()
    dresseur1U2Image = pygame.image.load("chars/dresseur1-u2.png").convert_alpha()

    if newGame.map == "route01":
        from maps import route01
        map = route01.map()
        mapSave = route01.mapInit()
        resultMap = route01.mapResult()
        resultMapSave = deepcopy(resultMap)
        playerPosX = route01.startX()
        playerPosY = route01.startY()
        savePlayerPosX = playerPosX
        savePlayerPosY = playerPosY

    if newGame.map == "route101":
        from maps import route101
        map = route101.map()
        mapSave = route101.mapInit()
        resultMap = route101.mapResult()
        resultMapSave = deepcopy(resultMap)
        playerPosX = route101.startX()
        playerPosY = route101.startY()
        savePlayerPosX = playerPosX
        savePlayerPosY = playerPosY

    if newGame.map == "route104":
        from maps import route104
        map = route104.map()
        mapSave = route104.mapInit()
        resultMap = route104.mapResult()
        resultMapSave = deepcopy(resultMap)
        playerPosX = route104.startX()
        playerPosY = route104.startY()
        savePlayerPosX = playerPosX
        savePlayerPosY = playerPosY

    lastTry = deepcopy(map)
    lastKey = 0
    resetPossible = False

    rCount = True
    lCount = True
    dCount = True
    uCount = True

    catchEffect = pygame.mixer.Sound("songs/catch.wav")
    catchEffect.set_volume(0.2)

    pygame.display.set_caption("Chrono")
    fpsClock = pygame.time.Clock()
    
    TpsZero = pygame.time.get_ticks() ## Départ
    def temps():
        seconds = (pygame.time.get_ticks() - TpsZero) / 1000
        return seconds

    def displayMap():
        i = 0
        j = 0
        for j in range (0, 11):
            for i in range (0, 15):
                if map[j][i] == 0:
                    screen.blit(grassImage, (75*i, 75*j))
                elif map[j][i] == 1:
                    screen.blit(wallImage, (75*i, 75*j))
                elif map[j][i] == 3:
                    screen.blit(grassImage, (75*i, 75*j))
                    screen.blit(dresseurImage, (75*i, 75*j))
                elif map[j][i] == 6:
                    screen.blit(waterUpImage, (75*i, 75*j))
                elif map[j][i] == 7:
                    screen.blit(waterDownImage, (75*i, 75*j))
                elif map[j][i] == 8:
                    screen.blit(waterLeftImage, (75*i, 75*j))
                elif map[j][i] == 9:
                    screen.blit(waterRightImage, (75*i, 75*j))
                elif map[j][i] == 10:
                    screen.blit(waterHorizonImage, (75*i, 75*j))
                elif map[j][i] == 11:
                    screen.blit(waterVerticalImage, (75*i, 75*j))
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
                elif map[j][i] == 102:
                    screen.blit(grassImage, (75*i, 75*j))
                    screen.blit(pikachuImage, (75*i, 75*j))
                elif map[j][i] == 103:
                    screen.blit(grassImage, (75*i, 75*j))
                    screen.blit(arcaninImage, (75*i, 75*j))
                elif map[j][i] == 104:
                    screen.blit(grassImage, (75*i, 75*j))
                    screen.blit(arckoImage, (75*i, 75*j))
                elif map[j][i] == 105:
                    screen.blit(grassImage, (75*i, 75*j))
                    screen.blit(dracaufeuImage, (75*i, 75*j))
                i += 1
            i = 0
            j += 1

    def checkWin():
        i = 0
        j = 0
        stop = True
        for j in range (0, 11):
            for i in range (0, 15):
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
            textsurfacemenu = pokegbfontmini.render('Appuie sur M pour retourner au menu', False, (51, 91, 255))
            screen.blit(textsurfaceggbig,(458,360))
            screen.blit(textsurfacegg,(460,360))
            screen.blit(textsurfacereset,(370,400))
            screen.blit(textsurfacemenu,(284,440))

            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "pokoban"
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT "+newGame.map+" FROM users WHERE pseudo = '"+newGame.pseudo+"'")

            myresult = mycursor.fetchall()
            
            for x in myresult:
                print("hello", x)
                for y in x:
                    if float(y) > float(temps()) or float(y) == 0:

                        sql = "UPDATE users SET "+newGame.map+" = "+str(temps())+" WHERE pseudo = '"+newGame.pseudo+"'"

                        mycursor.execute(sql)

                        mydb.commit()

    returnToMenu = False

    while True:

        if returnToMenu == True:
            break

        displayMap()

        textsurfacechrono = pokegbfontchrono.render(str(temps()), False, "black")
        screen.blit(textsurfacechrono,(43,23))
        textsurfacechrono = pokegbfontchrono.render(str(temps()), False, (51, 91, 255))
        screen.blit(textsurfacechrono,(44,24))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN	:
                print(event.key)
                if event.key == 109:
                    newGame.screen = "main_menu"
                    returnToMenu = True
                if event.key == 49:
                    pygame.mixer.music.pause()
                if event.key == 50:
                    pygame.mixer.music.unpause()
                if event.key == 51:
                    actuamVolume = pygame.mixer.music.get_volume()
                    if actuamVolume <= 1:
                        pygame.mixer.music.set_volume(actuamVolume-0.1)
                if event.key == 52:
                    actuamVolume = pygame.mixer.music.get_volume()
                    if actuamVolume >= 0:
                        pygame.mixer.music.set_volume(actuamVolume+0.1)
                if event.key != 114 and event.key != 122 and event.key != 49 and event.key != 50 and event.key != 51 and event.key != 52:
                    lastTry = deepcopy(map)
                    lastKey = event.key
                    resetPossible = True
                if event.key == 114:
                    # Touche : R
                    map = deepcopy(mapSave)
                    playerPosX = savePlayerPosX
                    playerPosY = savePlayerPosY
                    rCount = True
                    lCount = True
                    dCount = True
                    uCount = True
                    resultMap = deepcopy(resultMapSave)
                    resetPossible = False
                if event.key == 122 and resetPossible == True:
                    # Touche : Z
                    if lastKey != 0:
                        map = deepcopy(lastTry)
                        # last move : up
                        if lastKey == 1073741906:
                            if resultMap[playerPosY-1][playerPosX] == 2:
                                resultMap[playerPosY-1][playerPosX] = 1
                            playerPosY += 1
                        # last move : right
                        if lastKey == 1073741903:
                            if resultMap[playerPosY][playerPosX+1] == 2:
                                resultMap[playerPosY][playerPosX+1] = 1
                            playerPosX -= 1
                        # last move : down
                        if lastKey == 1073741905:
                            if resultMap[playerPosY+1][playerPosX] == 2:
                                resultMap[playerPosY+1][playerPosX] = 1
                            playerPosY -= 1
                        # last move : left
                        if lastKey == 1073741904:
                            if resultMap[playerPosY][playerPosX-1] == 2:
                                resultMap[playerPosY][playerPosX-1] = 1
                            playerPosX += 1
                    resetPossible = False
                if event.key == 1073741906:
                    # Touche : up
                    print("up")
                    if playerPosY > 0:
                        nextPlayerPosY = playerPosY-1
                        # Si le joueur avance sur une pokéball remplie
                        if map[nextPlayerPosY][playerPosX] == 5:
                            pokeballPosY = nextPlayerPosY
                            pokeballPosX = playerPosX
                            nextPokeballPosY = nextPlayerPosY-1
                            if pokeballPosY > 0:
                                # faire condition si deux pokeballs à côté
                                if map[nextPokeballPosY][pokeballPosX] == 0:
                                    map[nextPokeballPosY][pokeballPosX] = pokemonCaptured
                                    resultMap[pokeballPosY][pokeballPosX] = 1
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
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
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
                                        map[playerPosY][playerPosX] = 0
                                    if uCount:
                                        map[nextPlayerPosY][playerPosX] = 57
                                        uCount = False
                                    else:
                                        map[nextPlayerPosY][playerPosX] = 58
                                        uCount = True
                                    print(1)
                                    playerPosY -= 1
                        # Si le joueur avance sur une pokéball vide ou de la terre
                        elif map[nextPlayerPosY][playerPosX] != 1 and map[nextPlayerPosY][playerPosX] != 3 and map[nextPlayerPosY][playerPosX] != 5 and map[nextPlayerPosY][playerPosX] < 101:
                            if mapSave[playerPosY][playerPosX] == 4:
                                if resultMap[playerPosY][playerPosX] == 2:
                                    map[playerPosY][playerPosX] = 5
                                else:
                                    map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                            else:
                                map[playerPosY][playerPosX] = 0
                            if uCount:
                                map[nextPlayerPosY][playerPosX] = 57
                                uCount = False
                            else:
                                map[nextPlayerPosY][playerPosX] = 58
                                uCount = True
                            playerPosY -= 1
                        # Si le joueur avance sur un pokémon
                        if map[nextPlayerPosY][playerPosX] > 100:
                            pokemonPosX = playerPosX
                            pokemonPosY = nextPlayerPosY
                            nextPokemonPosY = nextPlayerPosY-1
                            if pokemonPosY > 0:
                                if map[nextPokemonPosY][pokemonPosX] != 1 and map[nextPokemonPosY][pokemonPosX] != 3 and map[nextPokemonPosY][pokemonPosX] != 5 and map[nextPokemonPosY][pokemonPosX] < 101:
                                    if map[nextPokemonPosY][pokemonPosX] == 4:
                                        map[nextPokemonPosY][pokemonPosX] = 5
                                        pokemonCaptured = map[pokemonPosY][pokemonPosX]
                                        catchEffect.stop()
                                        catchEffect.play()
                                        resultMap[nextPokemonPosY][pokemonPosX] = 2
                                    else:
                                        print(map[pokemonPosY][pokemonPosX])
                                        map[nextPokemonPosY][pokemonPosX] = map[pokemonPosY][pokemonPosX]
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
                if event.key == 1073741903:
                    # Touche : right
                    print("right")
                    if playerPosX < 15:
                        nextPlayerPosX = playerPosX+1
                        # Si le joueur avance sur une pokéball remplie
                        if map[playerPosY][nextPlayerPosX] == 5:
                            pokeballPosX = nextPlayerPosX
                            pokeballPosY = playerPosY
                            nextPokeballPosX = nextPlayerPosX+1
                            if pokeballPosX < 15:
                                if map[pokeballPosY][nextPokeballPosX] == 0:
                                    map[pokeballPosY][nextPokeballPosX] = pokemonCaptured
                                    resultMap[pokeballPosY][pokeballPosX] = 1
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
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
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
                                        map[playerPosY][playerPosX] = 0
                                    if rCount:
                                        map[playerPosY][nextPlayerPosX] = 51
                                        rCount = False
                                    else:
                                        map[playerPosY][nextPlayerPosX] = 52
                                        rCount = True
                                    print(1)
                                    playerPosX += 1
                        # Si le joueur avance sur une pokéball vide ou de la terre
                        elif map[playerPosY][nextPlayerPosX] != 1 and map[playerPosY][nextPlayerPosX] != 3 and map[playerPosY][nextPlayerPosX] != 5 and map[playerPosY][nextPlayerPosX] < 101:
                            if mapSave[playerPosY][playerPosX] == 4:
                                if resultMap[playerPosY][playerPosX] == 2:
                                    map[playerPosY][playerPosX] = 5
                                else:
                                    map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
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
                        # Si le joueur avance sur un pokémon
                        if map[playerPosY][nextPlayerPosX] > 100:
                            pokemonPosX = nextPlayerPosX
                            pokemonPosY = playerPosY
                            nextPokemonPosX = nextPlayerPosX+1
                            if pokemonPosX < 15:
                                if map[pokemonPosY][nextPokemonPosX] != 1 and map[pokemonPosY][nextPokemonPosX] != 3 and map[pokemonPosY][nextPokemonPosX] != 5 and map[pokemonPosY][nextPokemonPosX] < 101:
                                    if map[pokemonPosY][nextPokemonPosX] == 4:
                                        map[pokemonPosY][nextPokemonPosX] = 5
                                        pokemonCaptured = map[pokemonPosY][pokemonPosX]
                                        catchEffect.stop()
                                        catchEffect.play()
                                        resultMap[pokemonPosY][nextPokemonPosX] = 2
                                    else:
                                        map[pokemonPosY][nextPokemonPosX] = map[pokemonPosY][pokemonPosX]
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
                if event.key == 1073741905:
                    # Touche : down
                    print("down")
                    if playerPosY < 11:
                        nextPlayerPosY = playerPosY+1
                        # Si le joueur avance sur une pokéball remplie
                        if map[nextPlayerPosY][playerPosX] == 5:
                            pokeballPosY = nextPlayerPosY
                            pokeballPosX = playerPosX
                            nextPokeballPosY = nextPlayerPosY+1
                            if pokeballPosY < 11:
                                if map[nextPokeballPosY][pokeballPosX] == 0:
                                    map[nextPokeballPosY][pokeballPosX] = pokemonCaptured
                                    resultMap[pokeballPosY][pokeballPosX] = 1
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
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
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
                                        map[playerPosY][playerPosX] = 0
                                    if dCount:
                                        map[nextPlayerPosY][playerPosX] = 55
                                        dCount = False
                                    else:
                                        map[nextPlayerPosY][playerPosX] = 56
                                        dCount = True
                                    print(1)
                                    playerPosY += 1
                        # Si le joueur avance sur une pokéball vide ou de la terre
                        elif map[nextPlayerPosY][playerPosX] != 1 and map[nextPlayerPosY][playerPosX] != 3 and map[nextPlayerPosY][playerPosX] != 5 and map[nextPlayerPosY][playerPosX] < 101:
                            if mapSave[playerPosY][playerPosX] == 4:
                                if resultMap[playerPosY][playerPosX] == 2:
                                    map[playerPosY][playerPosX] = 5
                                else:
                                    map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                            else:
                                map[playerPosY][playerPosX] = 0
                            if dCount:
                                map[nextPlayerPosY][playerPosX] = 55
                                dCount = False
                            else:
                                map[nextPlayerPosY][playerPosX] = 56
                                dCount = True
                            playerPosY += 1
                        # Si le joueur avance sur un pokémon
                        if map[nextPlayerPosY][playerPosX] > 100:
                            pokemonPosX = playerPosX
                            pokemonPosY = nextPlayerPosY
                            nextPokemonPosY = nextPlayerPosY+1
                            if pokemonPosY < 11:
                                if map[nextPokemonPosY][pokemonPosX] != 1 and map[nextPokemonPosY][pokemonPosX] != 3 and map[nextPokemonPosY][pokemonPosX] != 5 and map[nextPokemonPosY][pokemonPosX] < 101:
                                    if map[nextPokemonPosY][pokemonPosX] == 4:
                                        pokemonCaptured = map[pokemonPosY][pokemonPosX]
                                        map[nextPokemonPosY][pokemonPosX] = 5
                                        catchEffect.stop()
                                        catchEffect.play()
                                        resultMap[nextPokemonPosY][pokemonPosX] = 2
                                    else:
                                        map[nextPokemonPosY][pokemonPosX] = map[pokemonPosY][pokemonPosX]
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
                if event.key == 1073741904:
                    # Touche : left
                    print("left")
                    if playerPosX > 0:
                        nextPlayerPosX = playerPosX-1
                        # Si le joueur avance sur une pokéball remplie
                        if map[playerPosY][nextPlayerPosX] == 5:
                            pokeballPosX = nextPlayerPosX
                            pokeballPosY = playerPosY
                            nextPokeballPosX = nextPlayerPosX-1
                            if pokeballPosX > 0:
                                if map[pokeballPosY][nextPokeballPosX] == 0:
                                    map[pokeballPosY][nextPokeballPosX] = pokemonCaptured
                                    resultMap[pokeballPosY][pokeballPosX] = 1
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
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
                                    if mapSave[playerPosY][playerPosX] == 4:
                                        if resultMap[playerPosY][playerPosX] == 2:
                                            map[playerPosY][playerPosX] = 5
                                        else:
                                            map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                                    else:
                                        map[playerPosY][playerPosX] = 0
                                    if lCount:
                                        map[playerPosY][nextPlayerPosX] = 53
                                        lCount = False
                                    else:
                                        map[playerPosY][nextPlayerPosX] = 54
                                        lCount = True
                                    print(1)
                                    playerPosX -= 1
                        # Si le joueur avance sur une pokéball vide ou de la terre
                        elif map[playerPosY][nextPlayerPosX] != 1 and map[playerPosY][nextPlayerPosX] != 3 and map[playerPosY][nextPlayerPosX] != 5 and map[playerPosY][nextPlayerPosX] < 101:
                            print(resultMap[playerPosY][playerPosX])
                            if mapSave[playerPosY][playerPosX] == 4:
                                if resultMap[playerPosY][playerPosX] == 2:
                                    map[playerPosY][playerPosX] = 5
                                else:
                                    map[playerPosY][playerPosX] = deepcopy(mapSave[playerPosY][playerPosX])
                            else:
                                map[playerPosY][playerPosX] = 0
                            if lCount:
                                map[playerPosY][nextPlayerPosX] = 53
                                lCount = False
                            else:
                                map[playerPosY][nextPlayerPosX] = 54
                                lCount = True
                            playerPosX -= 1
                        # Si le joueur avance sur un pokémon
                        if map[playerPosY][nextPlayerPosX] > 100:
                            pokemonPosX = nextPlayerPosX
                            pokemonPosY = playerPosY
                            nextPokemonPosX = nextPlayerPosX-1
                            if pokemonPosX > 0:
                                if map[pokemonPosY][nextPokemonPosX] != 1 and map[pokemonPosY][nextPokemonPosX] != 3 and map[pokemonPosY][nextPokemonPosX] != 5 and map[pokemonPosY][nextPokemonPosX] < 101:
                                    if map[pokemonPosY][nextPokemonPosX] == 4:
                                        pokemonCaptured = map[pokemonPosY][pokemonPosX]
                                        map[pokemonPosY][nextPokemonPosX] = 5
                                        catchEffect.stop()
                                        catchEffect.play()
                                        resultMap[pokemonPosY][nextPokemonPosX] = 2
                                    else:
                                        map[pokemonPosY][nextPokemonPosX] = map[pokemonPosY][pokemonPosX]
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
        
        checkWin()
        temps()
        fpsClock.tick(60)
        pygame.display.set_caption(str("Sokoban - "+newGame.map))
        pygame.display.flip()