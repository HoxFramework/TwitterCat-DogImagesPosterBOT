import os
import random
def doggettextfile():
    path = "./pets/doggofactos/"
    global dogfact
    dogfact = os.listdir(path)
    rndm = random.choice(dogfact)
    rndm = rndm.replace("'","")
    dogfact = path + rndm
    #print(dogfact)
    with open('UsedFacts.txt','a') as fileBe:
        fileBe.write(dogfact)
    fileBe.close()
    global doggofacto
    with open(dogfact, 'r') as doggofacto:
        doggofacto = doggofacto.read()
        return doggofacto
    

def doggetimgfile():
    global dogimage
    path = './pets/doggos/'
    dogimage = os.listdir(path)
    dogimage = random.choice(dogimage)
    dogimage = dogimage.replace("'","")
    dogimage = path + dogimage

    return dogimage
