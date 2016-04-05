# -*- coding: utf-8 -*-
import pygame
import string
import os.path
import sys
import codecs
from time import *
import pickle
# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')
clickcounter = 0
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15, True)
 

def main():

    # Initialisieren aller Pygame-Module und    

    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).

    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    screen = pygame.display.set_mode((800, 600))
    pygame.init()
    playing = False
    
    ####################
    alreadygot = {"bild0.jpg" : ["cursor.jpg"]}
    alreadytook = {"bild0.jpg" : ["cursor.jpg"]}
    slots = ["","","",""]
    holding = ""
    raum = "fertig/bild0.jpg"
    ####################

    try:
        f = open("inventory.dat")
        slots = pickle.load(f)
        f.close()
        f = open("holding.dat")
        holding = pickle.load(f)
        f.close()
        f = open("position.dat")
        raum = pickle.load(f)
        f.close()
        f = open("alreadygot.dat")
        alreadygot = pickle.load(f)
        f.close()
    except IOError:
        output = open('inventory.dat', 'w')
        pickle.dump(slots, output)
        output.close()
        output = open('holding.dat', 'w')
        pickle.dump(holding, output)
        output.close()
        output = open('position.dat', 'w')
        pickle.dump(raum, output)
        output.close()
        output = open('alreadygot.dat', 'w')
        pickle.dump(alreadygot, output)
        output.close()
        output = open('alreadytook.dat', 'w')
        pickle.dump(alreadytook, output)
        output.close()
    if(not holding == ""):
        holdingsurface = pygame.image.load(holding)
    dummysurface = pygame.image.load("cursor.jpg")
    slotsurfaces=[dummysurface, dummysurface, dummysurface, dummysurface]
    j = 0
    for i in slots:
        if(not i == ""):
            slotsurfaces[j] = pygame.image.load(i)
            
        j = j + 1

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

    pygame.display.set_caption("TEACHERS")

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 30)

    
 

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

    clock = pygame.time.Clock()
    labeltime = 0
    labeltext = ["Herzlich Willkommen!"]
    del(labeltext[0])

    # Die Schleife, und damit unser Spiel, läuft solange running == True.

    running = True

    while running:

        # Framerate auf 30 Frames pro Sekunde beschränken.

        # Pygame wartet, falls das Programm schneller läuft.
        
        clock.tick(30)
        #print(labeltime)
        #print(time())
        successfull = True
        x, y = pygame.mouse.get_pos()
        logik = string.replace(raum, '.jpg', '.txt')
        image = pygame.image.load(raum)
        inventar = pygame.image.load("inventar.png").convert_alpha()
        while playing:
            screen.blit(movie_screen,(0,0))
            pygame.display.update()
        screen.blit(image, (0, 0))
        screen.blit(inventar, (800 - 350,600 - 70))
        if(not holding == ""):
            screen.blit(holdingsurface, (x + 20,y + 20))
        j = 0
        #for i in slotsurfaces:
         #   if(not slots[j] == ""):
          #      screen.blit(i, (530 + j * 55,550))

           # j = j + 1
            #print(j)
        
                    
        
        
        fobj = codecs.open(logik, "r", "utf-8")
        if(labeltime > time()):
            label = myfont.render(labeltext[0], 1, (200,200,200), (0,0,0))
            screen.blit(label, (0 + 30, (600-30) - 15))
            #print(labeltime)
            #print(time())
            #print(labeltext[0])
        elif(len(labeltext) > 0):
            del(labeltext[0])
            if(not len(labeltext) == 0):
                labeltime = time() + 2
            #print("Zwei wurde addiert")

        linie = None
        for line in fobj:
            #print line.rstrip()
            if(x >= int(line[0] + line[1] + line[2]) and y >= int(line[4] + line[5] + line[6]) and x <= int(line[8] + line[9] + line[10]) and y <= int(line[12] + line[13] + line[14])):
                linie = line
        if(not linie == None):
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        fobj.close()
 

        # Alle aufgelaufenen Events holen und abarbeiten.

        for event in pygame.event.get():

            # Spiel beenden, wenn wir ein QUIT-Event finden.

            if event.type == pygame.QUIT:

                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                if(not linie == None):
                    labeltext=[]
                    labeltime = 0
                    linie = linie.split("\n")[0]
                    while("PRINT" in linie):
                        gespalten = linie.rsplit("PRINT", 1)
                        #print(gespalten[1])
                        labeltext.append(gespalten[1])
                        labeltime = time() + 2
                        
                        linie = gespalten[0]
                    while("GOTO" in linie):
                        gespalten = linie.rsplit("GOTO", 1)
                        raum = "fertig/" + gespalten[1]
                        linie = gespalten[0]
                    while("SAY" in linie):
                        gespalten = linie.rsplit("SAY", 1)
                        sound = gespalten[1]
                        linie = gespalten[0]
                        pygame.mixer.Sound(sound).play()  #load sound
                    while("SUBTRACT" in linie):
                        gespalten = linie.rsplit("SUBTRACT", 1)
                        successfull = False
                        if(not raum in alreadytook or not gespalten[1] in alreadytook[raum]):
                            if(gespalten[1] == holding):
                                #print(holding)
                                holding = ""
                                #print(holding)
                                successfull = True
                            
                        linie = gespalten[0]
                    while("ADD" in linie and successfull):
                        
                        gespalten = linie.rsplit("ADD", 1)
                        successfull = False
                        if(not raum in alreadygot or not gespalten[1] in alreadygot[raum]):
                            if(holding == ''):
                                #print('checkpoint')
                                #print('checkpoint')
                                successfull = True
                                #print(holding)
                                #print(gespalten[1])
                                #print('checkpoint')
                                holding = gespalten[1]
                                #print(holding)
                                holdingsurface = pygame.image.load(holding)
                                if(raum in alreadygot):
                                    alreadygot[raum].append(gespalten[1])
                                else:
                                    alreadygot[raum] = [gespalten[1]]
                                output = open('alreadygot.dat', 'w')
                                pickle.dump(alreadygot, output)
                                output.close()
                                    
                                   
                        linie = gespalten[0]
                    if("IFSUCGO" in linie and successfull):
                        gespalten = linie.rsplit("IFSUCGO", 1)
                        raum = "fertig/" + gespalten[1]
                        linie = gespalten[0]    
                    while("PLAY" in linie and False):
                        clock = pygame.time.Clock()
                        movie = pygame.movie.Movie('fertig/bild0.mpg')
                        screen = pygame.display.set_mode(movie.get_size())
                        movie_screen = pygame.Surface(movie.get_size()).convert()
                        movie.set_display(movie_screen)
                        movie.play()
                        playing = True
                    while("INVENTORY" in linie):
                        gespalten = linie.rsplit("INVENTORY", 1)
                        inventarslot = int(gespalten[1])
                        if(inventarslot == 1):
                            f = open("inventory.dat")
                            slots = pickle.load(f)
                            f.close()
                            f = open("holding.dat")
                            holding = pickle.load(f)
                            f.close()
                            f = open("position.dat")
                            raum = pickle.load(f)
                            f.close()
                            f = open("alreadygot.dat")
                            alreadygot = pickle.load(f)
                            f.close()
                            f = open("alreadytook.dat")
                            alreadytook = pickle.load(f)
                            f.close()
                            print("loaded")
                        elif(inventarslot == 6):
                            output = open('inventory.dat', 'w')
                            pickle.dump(slots, output)
                            output.close()
                            output = open('holding.dat', 'w')
                            pickle.dump(holding, output)
                            output.close()
                            output = open('position.dat', 'w')
                            pickle.dump(raum, output)
                            output.close()
                            output = open('alreadygot.dat', 'w')
                            pickle.dump(alreadygot, output)
                            output.close()
                            output = open('alreadytook.dat', 'w')
                            pickle.dump(alreadytook, output)
                            output.close()
                            print("saved")
                            
                        else:
                            inventarslot = inventarslot - 2
                            if(not holding == ""):
                                tempholding = slots[inventarslot]
                                slots[inventarslot] = holding
                                holding = tempholding
                                tempholding = ""
                            else:
                                holding = slots[inventarslot]
                                slots[inventarslot] = ""
                            if(holding == ""):
                                holdingsurface = pygame.image.load("cursor.jpg")
                            else:
                                holdingsurface = pygame.image.load(holding)
                        j = 0
                        for i in slots:
                            if(not i == ""):
                                slotsurfaces[j] = pygame.image.load(i)
                            
                            j = j + 1
                        linie = gespalten[0]
                            
            # Wir interessieren uns auch für "Taste gedrückt"-Events.

            if event.type == pygame.KEYDOWN:

                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.

                if event.key == pygame.K_ESCAPE:

                    pygame.event.post(pygame.event.Event(pygame.QUIT))

 

        # Inhalt von screen anzeigen.
        
            
        pygame.display.flip()
 

 

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.

if __name__ == '__main__':

    # Unsere Main-Funktion aufrufen.

    main()
