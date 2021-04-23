import pygame, pygame_menu
from pygame_menu.examples import create_example_window
import mysql.connector

def pseudo_menu(screen, width, newGame):

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "pokoban"
    )
    
    pygame.init()
    center_x, center_y = 240, 240
    
    font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    prompt = font.render('Entrez votre pseudo : ', True, "blue")
    prompt_rect = prompt.get_rect(center=(center_x, center_y))
    
    user_input_value = ""
    user_input = font.render(user_input_value, True, "yellow")
    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
    
    continuer = True
    
    while continuer:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 13 or event.key == 1073741912:
                    mycursor = mydb.cursor()

                    mycursor.execute("SELECT * FROM users WHERE pseudo = '"+user_input_value+"'")

                    myresult = mycursor.fetchall()
                    
                    if len(myresult) == 0:
                        sql = "INSERT INTO users (pseudo, route01, route101) VALUES (%s, %s, %s)"
                        val = (user_input_value, 0, 0)
                        mycursor.execute(sql, val)

                        mydb.commit()
                    newGame.pseudo = user_input_value
                    newGame.screen = "main_menu"
                    continuer = False

                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    if event.key != 13 and event.key != 32 and event.key != 1073741912:
                        user_input_value += event.unicode
                user_input = font.render(user_input_value, True, "yellow")
                user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
    
    
        mainMenuImage = pygame.image.load("main-menu.png").convert_alpha()
        screen.blit(mainMenuImage, (0, 0))
        screen.blit(prompt, prompt_rect)
        screen.blit(user_input, user_input_rect)
        pygame.display.set_caption("Pokoban - Choisissez votre pseudo")
        pygame.display.flip()
    
def main_menu(screen, width, newGame):

    mainMenuImage = pygame.image.load("main-menu.png").convert_alpha()
    screen.blit(mainMenuImage, (0, 0))

    # Ma police d'écriture
    titleFont = "PokemonSolidNormal-xyWR.ttf"
    def title_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        titleText=newFont.render(message, 0, textColor)
 
        return titleText
    
    subtitleFont = "PokemonGb-RAeo.ttf"
    def subtitle_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        subtitleText=newFont.render(message, 0, textColor)
 
        return subtitleText

    menu=True
    selected = "level"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN	:
                # down
                if event.key == 1073741905:
                    if selected == "level":
                        selected = "stats"
                    elif selected == "stats":
                        selected = "quit"
                # up
                if event.key == 1073741906:
                    if selected == "stats":
                        selected = "level"
                    elif selected == "quit":
                        selected = "stats"
                # enter
                if event.key == 13:
                    if selected == "level":
                        newGame.mode = "level"
                        newGame.screen = "list_map_menu"
                        menu = False
                    if selected == "stats":
                        newGame.mode = "stats"
                        newGame.screen = "stats_menu"
                        menu = False
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        title=title_format("Pokoban", titleFont, 90, 'yellow')
        titleBlue=title_format("Pokoban", titleFont, 90, 'blue')
        text_level_black = subtitle_format("Liste des niveaux", subtitleFont, 28, 'black')
        if selected=="level":
            text_level=subtitle_format("Liste des niveaux", subtitleFont, 28, 'yellow')
        else:
            text_level = subtitle_format("Liste des niveaux", subtitleFont, 28, 'whitesmoke')
        if selected=="stats":
            text_stats=subtitle_format("Mes stats", subtitleFont, 40, 'yellow')
        else:
            text_stats = subtitle_format("Mes stats", subtitleFont, 40, 'whitesmoke')
            text_stats_black = subtitle_format("Mes stats", subtitleFont, 40, 'black')
        if selected=="quit":
            text_quit=subtitle_format("Quitter", subtitleFont, 40, 'yellow')
        else:
            text_quit = subtitle_format("Quitter", subtitleFont, 40, 'whitesmoke')
            text_quit_black = subtitle_format("Quitter", subtitleFont, 40, 'black')
 
        title_rect=title.get_rect()
        level_rect=text_level.get_rect()
        stats_rect=text_stats.get_rect()
        quit_rect=text_quit.get_rect()              
 
        # Main Menu Text Placement
        screen.blit(titleBlue, (width/2 - (title_rect[2]/2), 58))
        screen.blit(titleBlue, (width/2 - (title_rect[2]/2), 44))
        screen.blit(titleBlue, (width/2+4 - (title_rect[2]/2), 58))
        screen.blit(titleBlue, (width/2-4 - (title_rect[2]/2), 58))
        screen.blit(titleBlue, (width/2+4 - (title_rect[2]/2), 44))
        screen.blit(titleBlue, (width/2-4 - (title_rect[2]/2), 44))
        screen.blit(title, (width/2 - (title_rect[2]/2), 50))
        screen.blit(text_level_black, (width/2 - (level_rect[2]/2), 225))
        screen.blit(text_level, (width/2 - (level_rect[2]/2), 220))
        screen.blit(text_stats_black, (width/2 - (stats_rect[2]/2), 305))
        screen.blit(text_stats, (width/2 - (stats_rect[2]/2), 300))
        screen.blit(text_quit_black, (width/2 - (quit_rect[2]/2), 425))
        screen.blit(text_quit, (width/2 - (quit_rect[2]/2), 420))
        pygame.display.set_caption("Pokoban - Menu principal")
        pygame.display.update()


def list_map_menu(screen, width, newGame):

    listMapMenuImage = pygame.image.load("main-menu.png").convert_alpha()
    screen.blit(listMapMenuImage, (0, 0))

    # Ma police d'écriture
    titleFont = "PokemonSolidNormal-xyWR.ttf"
    def title_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        titleText=newFont.render(message, 0, textColor)
 
        return titleText
    
    subtitleFont = "PokemonGb-RAeo.ttf"
    def subtitle_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        subtitleText=newFont.render(message, 0, textColor)
 
        return subtitleText

    menu=True
    selected = "route01"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == pygame.KEYDOWN	:
                # down
                if event.key == 1073741905:
                    if selected == "route01":
                        selected = "route101"
                    elif selected == "route101":
                        selected = "route104"
                # up
                if event.key == 1073741906:
                    if selected == "route101":
                        selected = "route01"
                    elif selected == "route104":
                        selected = "route101"
                # enter
                if event.key == 13:
                    if selected == "route01":
                        newGame.map = "route01"
                        newGame.screen = "game"
                        menu = False
                    if selected == "route101":
                        newGame.map = "route101"
                        newGame.screen = "game"
                        menu = False
                    if selected == "route104":
                        newGame.map = "route104"
                        newGame.screen = "game"
                        menu = False
                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key == 27:
                    newGame.screen = "main_menu"
                    menu = False
 
        title=title_format("Levels", titleFont, 50, 'yellow')
        titleBlue=title_format("Levels", titleFont, 50, 'blue')
        text_route01_black = subtitle_format("Route 01", subtitleFont, 27, 'black')
        text_route101_black = subtitle_format("Route 101", subtitleFont, 27, 'black')
        text_route104_black = subtitle_format("Route 104", subtitleFont, 27, 'black')
        text_easy = subtitle_format("Easy", subtitleFont, 27, 'green')
        text_medium = subtitle_format("Medium", subtitleFont, 27, 'orange')
        text_hard = subtitle_format("Hard", subtitleFont, 27, 'red')

        if selected=="route01":
            text_route01=subtitle_format("Route 01", subtitleFont, 27, 'yellow')
        else:
            text_route01 = subtitle_format("Route 01", subtitleFont, 27, 'whitesmoke')
        if selected=="route101":
            text_route101=subtitle_format("Route 101", subtitleFont, 27, 'yellow')
        else:
            text_route101 = subtitle_format("Route 101", subtitleFont, 27, 'whitesmoke')
        if selected=="route104":
            text_route104=subtitle_format("Route 104", subtitleFont, 27, 'yellow')
        else:
            text_route104 = subtitle_format("Route 104", subtitleFont, 27, 'whitesmoke')

        text_escape = subtitle_format("Retour -> ECHAP", subtitleFont, 27, 'whitesmoke')
 
        title_rect=title.get_rect()
        level_rect=text_route01.get_rect()
 
        # Main Menu Text Placement
        screen.blit(titleBlue, (width/2 - (title_rect[2]/2), 58))
        screen.blit(title, (width/2 - (title_rect[2]/2), 50))
        screen.blit(text_route01_black, (110, 145))
        screen.blit(text_route01, (110, 140))
        screen.blit(text_route101_black, (110, 185))
        screen.blit(text_route101, (110, 180))
        screen.blit(text_route104_black, (110, 225))
        screen.blit(text_route104, (110, 220))
        screen.blit(text_easy, (370, 140))
        screen.blit(text_medium, (370, 180))
        screen.blit(text_hard, (370, 220))
        screen.blit(text_escape, (width/2-90 - (level_rect[2]/2), 550))
        pygame.display.set_caption("Pokoban - Liste des niveaux")
        pygame.display.update()

def stats_menu(screen, width, newGame):

    listMapMenuImage = pygame.image.load("main-menu.png").convert_alpha()
    screen.blit(listMapMenuImage, (0, 0))

    # Ma police d'écriture
    titleFont = "PokemonSolidNormal-xyWR.ttf"
    def title_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        titleText=newFont.render(message, 0, textColor)
 
        return titleText
    
    subtitleFont = "PokemonGb-RAeo.ttf"
    def subtitle_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        subtitleText=newFont.render(message, 0, textColor)
 
        return subtitleText

    menu=True
    selected = "route01"

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "pokoban"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM users WHERE pseudo = '"+newGame.pseudo+"'")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == pygame.KEYDOWN	:
                print(event.key)
                # down
                if event.key == 1073741905:
                    if selected == "route01":
                        selected = "route101"
                    elif selected == "route101":
                        selected = "route104"
                # up
                if event.key == 1073741906:
                    if selected == "route101":
                        selected = "route01"
                    elif selected == "route104":
                        selected = "route101"
                # enter
                if event.key == 27:
                    newGame.screen = "main_menu"
                    menu = False

 
        title=title_format("Mes stats", titleFont, 50, 'yellow')
        titleBlue=title_format("Mes stats", titleFont, 50, 'blue')
        text_route01_black = subtitle_format("Route 01", subtitleFont, 27, 'black')
        text_route101_black = subtitle_format("Route 101", subtitleFont, 27, 'black')
        text_route104_black = subtitle_format("Route 104", subtitleFont, 27, 'black')
        if selected=="route01":
            text_route01 = subtitle_format(("Route 01: "+str(myresult[0][2])), subtitleFont, 27, 'yellow')
        else:
            text_route01 = subtitle_format(("Route 01: "+str(myresult[0][2])), subtitleFont, 27, 'whitesmoke')
        if selected=="route101":
            text_route101 = subtitle_format(("Route 101: "+str(myresult[0][3])), subtitleFont, 27, 'yellow')
        else:
            text_route101 = subtitle_format(("Route 101: "+str(myresult[0][3])), subtitleFont, 27, 'whitesmoke')
        if selected=="route104":
            text_route104 = subtitle_format(("Route 104: "+str(myresult[0][4])), subtitleFont, 27, 'yellow')
        else:
            text_route104 = subtitle_format(("Route 104: "+str(myresult[0][4])), subtitleFont, 27, 'whitesmoke')
        
        text_escape = subtitle_format("Retour -> ECHAP", subtitleFont, 27, 'whitesmoke')
 
        title_rect=title.get_rect()
        level_rect=text_route01.get_rect()
 
        # Main Menu Text Placement
        screen.blit(titleBlue, (width/2 - (title_rect[2]/2), 58))
        screen.blit(title, (width/2 - (title_rect[2]/2), 50))
        screen.blit(text_route01_black, (width/2 - (level_rect[2]/2), 145))
        screen.blit(text_route01, (width/2 - (level_rect[2]/2), 140))
        screen.blit(text_route101_black, (width/2 - (level_rect[2]/2), 185))
        screen.blit(text_route101, (width/2 - (level_rect[2]/2), 180))
        screen.blit(text_route104_black, (width/2 - (level_rect[2]/2), 225))
        screen.blit(text_route104, (width/2 - (level_rect[2]/2), 220))
        screen.blit(text_escape, (width/2-35 - (level_rect[2]/2), 550))
        pygame.display.set_caption("Pokoban - Mes stats")
        pygame.display.update()
