import os
import Image
if (True):
    bilder_ordner = os.getcwd() + '/bilder'
    print(bilder_ordner)
    bild_dateien = os.listdir(bilder_ordner)
    print(bild_dateien)
    for bild in bild_dateien:
        bild_pfad = bilder_ordner + '/' + bild
        img=Image.open(bild_pfad)
        size=[800, 600]
        img=img.resize(size)
        img.save(bild)
        
        
        
       
