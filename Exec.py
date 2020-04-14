import os, random
import catsDownloader
import dogsDownloader
import CattoPoster
import DoggoPoster
import tweetMe
import DataCleaner


mainin = input("1.Post cat n fact\n2.Post dog n fact\n3.Clean up used data (from posts)\n4.Download Doggos\n5.Download cattos\n6.Clean up pic-doubles (do this after you download the pics)\n>")
if mainin == "1":
    catimage = CattoPoster.catgetimgfile()
    catfact = CattoPoster.catgettextfile()
    with open('UsedImages.txt','a') as filer:
        filer.write("\n" + catimage)
    filer.close()
    tweetMe.goTweet(catfact, catimage)
elif mainin == "2":
    dogimage = DoggoPoster.doggetimgfile()
    doggofacto = DoggoPoster.doggettextfile()
    with open('UsedImages.txt','a') as filer:
        filer.write("\n" + dogimage)
    filer.close()
    tweetMe.goTweet(doggofacto, dogimage)
elif mainin == "3":
    print("Loading the cleaner...")
    print("THERE HAS TO BE AT LEAST 2 FILES IN EACH .txt FILE !\n")
    DataCleaner.cleaner()
elif mainin == "4":
    print("Downloading doggos...")
    dogsDownloader.dog()
elif mainin == "5":
    print("Downloading cattos...")
    catsDownloader.cat()
elif mainin == "6":
    print("Loading...")
    import imageChecker
    #ovo necemo importat odma jer ima previse modula anyway; We dont wanna bloat
    imageChecker.checkmypics()
else:
    print("No. Dont be rude.")

