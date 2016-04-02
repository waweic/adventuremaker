# -*- coding: UTF-8 -*-

     

# Pygame-Modul importieren.

import pygame
import string
import os
import Image
if(True):
     

    # Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.

    if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

    if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

     

    def main():

        # Initialisieren aller Pygame-Module und    

        # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).

        pygame.init()
        verhaeltnis = 3.0 / 4.0
        normalsizex = 800
        normalsizey = 600

        screen = pygame.display.set_mode((normalsizex, normalsizey))

     

        # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

        pygame.display.set_caption("Ausschneiden und Größe ändern")

        pygame.mouse.set_visible(1)

        pygame.key.set_repeat(1, 30)

     

        # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

        clock = pygame.time.Clock()

        
        print("Klick auf den ersten Punkt.")
        # Die Schleife, und damit unser Spiel, läuft solange running == True.
        verhaeltnis = 3.0 / 4.0
        normalsizex = 800
        normalsizey = 600
        running = True
        counter = 2
        bildnummer = 0
        bilder_ordner = os.getcwd() + '/bilder/'
        print(bilder_ordner)
        bild_dateien = os.listdir(bilder_ordner)
        bild_pfad = bilder_ordner + bild_dateien[0]
        #print(bild_dateien)
        while running:

            # Framerate auf 30 Frames pro Sekunde beschränken.

            # Pygame wartet, falls das Programm schneller läuft.

            clock.tick(30)
        
     

            if (not bildnummer == len(bild_dateien)):
                #print(bild_pfad)
                bild_pfad = bilder_ordner + bild_dateien[bildnummer]
                #print(bild_dateien[bildnummer])
                #print(bild_pfad)
                img=Image.open(bild_pfad)
                width, height = img.size
                #print(width, height)
                #print (width)
                #print (height)
                xfactor = float(width) / normalsizex
                #print(xfactor)
                yfactor = float(height) / normalsizey
                #print(yfactor)
                img.resize([normalsizex, normalsizey]).save("temp.jpg")
                
                screen.blit(pygame.image.load("temp.jpg"), (0, 0))
            else:
                running = False
                    
     

            # Alle aufgelaufenen Events holen und abarbeiten.

            for event in pygame.event.get():

                # Spiel beenden, wenn wir ein QUIT-Event finden.

                if event.type == pygame.QUIT:

                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if(counter == 2):
                            firstx = x
                            firsty = y
                            counter = 1
                            print("Klick auf den zweiten Punkt.")
                        elif(counter == 1):
                            counter = 2
                            secondx = x
                            secondy = y
                            #if(True):#(secondx - firstx) * verhaeltnis > (secondy - firsty) * verhaeltnis):
                             #   xsize = (secondx - firstx)
                              #  ysize = int(xsize * verhaeltnis) - 100 
                               # print(xsize)
                                #print(ysize)
                                #print('first')
                            #else:
                             #   ysize = secondy - firsty
                              #  xsize = int(ysize / verhaeltnis)
                               # print(xsize)
                                #print(ysize)
                                #print('second')
                            #crop
                            #
                            print(firsty)
                            print(secondy)
                            if((secondx - firstx) / (secondy - firsty) > verhaeltnis):
                                print('Heye ist cool')
                                irgendwasy = (secondx - firstx) * verhaeltnis / 2
                                print(irgendwasy)
                                irgendwaszweiy = (firsty + (secondy - firsty)) / 2
                                print(irgendwaszweiy)
                                if(irgendwaszweiy - irgendwasy < 0):
                                    firsty = 0
                                elif(irgendwaszweiy - irgendwasy > normalsizey):
                                    firsty = normalsizey
                                    
                                else:
                                    firsty = (irgendwaszweiy - irgendwasy) * 2
                                secondy = firsty + irgendwasy * 2
                            else:
                                irgendwasx = ((secondy - firsty) / verhaeltnis) / 2
                                print(irgendwasx)
                                irgendwaszweix = (firstx + (secondx - firstx)) / 2
                                print(irgendwaszweix)
                                if(irgendwaszweix - irgendwasx < 0):
                                    firstx = 0
                                elif(irgendwaszweix - irgendwasx > normalsizex):
                                    firstx = normalsizex
                                    
                                else:
                                    firstx = (irgendwaszweix - irgendwasx) * 2
                                secondx = firstx + irgendwasx * 2
                            
                            box=[int(firstx * xfactor),int(firsty * yfactor),int(secondx * xfactor),int(secondy * yfactor)]
                            print(box)   
                            img=img.crop(box)
                            img.save(os.getcwd() + "" + "debug" + str(bildnummer) + ".jpg")
                            sizebox=[normalsizex, normalsizey]
                            img=img.resize(sizebox)
                            img.save(os.getcwd() + "/fertig/" + "bild" + str(bildnummer) + ".jpg")
                            #print(bilder_ordner)
                            print(bild_dateien[bildnummer])
                            print(bildnummer)
                            bildnummer = bildnummer + 1
                            print(bildnummer)
                            print(bild_dateien[bildnummer])
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
