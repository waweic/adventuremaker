# -*- coding: UTF-8 -*-

     

# Pygame-Modul importieren.

import pygame
import string
if(True):
     

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

     

        # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

        clock = pygame.time.Clock()

        image = raw_input("Was willst du bearbeiten?")
        myfile = file(string.replace(image, '.jpg', '.txt'), 'w')   # File-Handle auf File 'test.txt' erstellen
        myfile.close()
        print("Klick auf den ersten Punkt.")
        # Die Schleife, und damit unser Spiel, läuft solange running == True.

        running = True
        counter = 2
        while running:

            # Framerate auf 30 Frames pro Sekunde beschränken.

            # Pygame wartet, falls das Programm schneller läuft.

            clock.tick(30)
        
     


            screen.blit(pygame.image.load(image), (0, 0))

     

            # Alle aufgelaufenen Events holen und abarbeiten.

            for event in pygame.event.get():

                # Spiel beenden, wenn wir ein QUIT-Event finden.

                if event.type == pygame.QUIT:

                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if(counter == 2):
                            zeile1 = ""
                            if(x < 100):
                                x = "0" + str(x)
                            if(y < 100):
                                y = "0" + str(y)
                            zeile1 = str(x) + "A" + str(y) + "X"
                            counter = 1
                        
                            print("Klick auf den zweiten Pumkt.")
                        elif(counter == 1):
                            zeile = ""
                            if(x < 100):
                                x = "0" + str(x)
                            if(y < 100):
                                y = "0" + str(y)
                            zeile = zeile1 + str(x) + "B" + str(y) + "PRINTNur ein Platzhalter"
                            counter = 2
                            print(zeile)
                            try:
                                fobj_in = ""
                            except IOError, err:
                                if err.errno == errno.ENOENT: # No 2: No such file or directory
                                    print "Bitte Verzeichnis erstellen!"
                                    sys.exit()
                            fobj_in = open(string.replace(image, '.jpg', '.txt')).read()
                            fobj_out = open(string.replace(image, '.jpg', '.txt'),"w")
                            fobj_out.write(fobj_in + zeile + "\n")
                            
                            fobj_out.close()
                            print("Klick auf den ersten Punkt.")

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
