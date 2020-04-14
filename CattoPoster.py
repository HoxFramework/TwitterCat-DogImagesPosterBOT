import os
import random
def catgettextfile():
   path = "./pets/cattofactos/"
   global catfact
   catfact = os.listdir(path)
   rndm = random.choice(catfact)
   catfact = path + rndm
   #print(catfact)
   with open('UsedFacts.txt','a') as fileBe:
      fileBe.write(catfact)
   fileBe.close()
   
   global fileA
   with open(catfact, 'r') as fileA:
       fileA = fileA.read()
       return fileA
   

def catgetimgfile():
   global catimage
   path = './pets/cattos/'
   catimage = os.listdir(path)
   catimage = random.choice(catimage)
   catimage = path + catimage
   return catimage
