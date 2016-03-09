# -*- coding: utf-8 -*-
import pygame
import string
import os.path
import sys
# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

 

def main():

    # Initialisieren aller Pygame-Module und    

    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

 

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 30)

    raum = "raum1.jpg"
 

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

    clock = pygame.time.Clock()

 

    # Die Schleife, und damit unser Spiel, läuft solange running == True.

    running = True

    while running:

        # Framerate auf 30 Frames pro Sekunde beschränken.

        # Pygame wartet, falls das Programm schneller läuft.

        clock.tick(30)

        x, y = pygame.mouse.get_pos()
        logik = string.replace(raum, '.jpg', '.txt')
        image = pygame.image.load(raum)
        screen.blit(image, (0, 0))
        fobj = open(logik)


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
                    if("PRINT" in linie):
                        print(linie.split("PRINT")[1])
                    elif("GOTO" in linie):
                        raum = linie.split("GOTO")[1]
                        raum = raum.split("\n")[0]
                        print raum

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
