#to wipe duplicates (after download) but NOT to wipe used.
def checkmypics():
    """Checks pics u downloaded."""
    #
    import numpy as np
    import cv2
    import os
    import random
    from itertools import combinations
    #2 dirs:
    animals_dir = ['./pets/doggos/','./pets/cattos/'] #how many times to scan ALL; Put the same dir twice to can it twice
    for directory in animals_dir:
        dirlister = os.listdir(directory)
        #For every pic in the directory
        for a, b in combinations(dirlister, 2):
            if a == b:
                pass
            else:
                imagenameone = a
                imagenametwo = b
                imgnddirtwo = directory + b
                a = directory + a
                b = directory + b
                #print("Comparing: ",b ," with ",a)
                a = cv2.imread(a)
                b = cv2.imread(b)
                img1 = a.shape
                img2 = b.shape
                #print(img1,img2)
                if img1 == img2:
                    #print("[+] COPY FOUND ! The images are the same.\n")
                    #
                    #now we gotta double check.. cause now we are working with 3 numbers
                    #and it gives false positives sometimes
                    if np.array_equal(b,a):
                        print(imagenameone," is a copy of ", imagenametwo)
                        print("Deleting the second image...%s"% imgnddirtwo)
                        #################os.remove(imgnddirtwo)
                        
                    else:
                        #print("False positive. Skipping.")
                        pass
                else:
                    #print("[-] The images are different.")
                    pass
    ##        except Exception:
    ##            print("[---]error")
        
    
