# -*- coding: UTF-8 -*-

     

# Pygame-Modul importieren.

import pygame
import string
import os, sys
import platform
import easygui
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

def open_file_browser():
    d = gui.FileDialog()
    d.connect(gui.CHANGE, handle_file_browser_closed, d)
    d.open()

#else:
 #   os.environ["SDL_VIDEODRIVER"] = "x11"
while(True):
     

    # Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

    if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

    if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

     

    def main():

        # Initialisieren aller Pygame-Module und    

        # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
       # root = tk.Tk()
        #embed = tk.Frame(root, width = 800, height = 600) #creates embed frame for pygame window
        #embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        
        #os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

        screen = pygame.display.set_mode((800, 600))
        pygame.display.init()
        pygame.display.update()
        
     

        # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

        pygame.display.set_caption("Vereinfachung")

        pygame.mouse.set_visible(1)

        pygame.key.set_repeat(1, 30)

     

        # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
        clock = pygame.time.Clock()
        path = easygui.fileopenbox()
        image = path
        fname = string.replace(image, '.jpg', '.txt')
        if(not os.path.isfile(fname)):
            datei = open(fname, "w")
            datei.close()
        inventar = pygame.image.load("inventar.png").convert_alpha()
        
        #myfile = file(string.replace(image, '.jpg', '.txt'), 'w')   # File-Handle auf File 'test.txt' erstellen
        #myfile.close()
        print("Klick auf den ersten Punkt.")
        # Die Schleife, und damit unser Spiel, läuft solange running == True.

        running = True
        counter = 2
        while running:

            # Framerate auf 30 Frames pro Sekunde beschränken.

            # Pygame wartet, falls das Programm schneller läuft.

            clock.tick(30)
        
     


            screen.blit(pygame.image.load(image), (0, 0))
            screen.blit(inventar, (800 - 350,600 - 70))
     

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
                        
                            print("Klick auf den zweiten Punkt.")
                        elif(counter == 1):
                            path = easygui.fileopenbox()
                            path = path.rsplit('/', 1)
                            zeile = ""
                            if(x < 100):
                                x = "0" + str(x)
                            if(y < 100):
                                y = "0" + str(y)
                            if(not path[1].find(".jpg") == -1):
                                zeile = zeile1 + str(x) + "B" + str(y) + "GOTO" + path[1]
                            elif(not path[1].find(".wav") == -1):
                                zeile = zeile1 + str(x) + "B" + str(y) + "SAY" + path[1]
                            else:
                                meintollerstring = raw_input("Was soll da drinstehen? ")
                                zeile = zeile1 + str(x) + "B" + str(y) + "PRINT" + str(meintollerstring)
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
                            if(str(fobj_in).find("461A540X507B585INVENTORY1\n516A540X561B585INVENTORY2\n572A540X616B585INVENTORY3\n630A540X671B585INVENTORY4\n682A540X727B585INVENTORY5\n738A540X781B585INVENTORY6\n") == -1):
                                zweitezeile = "461A540X507B585INVENTORY1\n516A540X561B585INVENTORY2\n572A540X616B585INVENTORY3\n630A540X671B585INVENTORY4\n682A540X727B585INVENTORY5\n738A540X781B585INVENTORY6\n"
                            else:
                                zweitezeile = ""
                            fobj_out.write(fobj_in + zeile + "\n" + zweitezeile)
                            
                            fobj_out.close()
                            print("Klick auf den ersten Punkt.")

                # Wir interessieren uns auch für "Taste gedrückt"-Events.

                if event.type == pygame.KEYDOWN:

                    # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.

                    if event.key == pygame.K_ESCAPE:

                        running = False

     

            # Inhalt von screen anzeigen.

            pygame.display.flip()

     

     

    # Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.

    if __name__ == '__main__':

        # Unsere Main-Funktion aufrufen.

        main()
        
    #while True:
     #   pygame.display.update()
      #  root.update()    
