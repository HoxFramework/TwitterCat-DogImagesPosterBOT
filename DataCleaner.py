import os
def cleaner():
       prefix = './pets'
       with open('UsedFacts.txt','r') as my_file:
           my_data = my_file.read()
           my_data = my_data.split(prefix)

       for k in my_data:
         if k == "":
             pass
         elif k == "\n":
             pass
         else:
             try:
                 #
                 k = k.replace("\n","")
                 k = k.replace("\n","")
                 combined = str(prefix + k)
                 if combined.endswith(".txt"):
                     os.remove('{0}'.format(combined))
                     print('[+] cleaning : ','{0}'.format(combined))
                 else:
                     print("Program attempted to delete an unwanted file. Prevented it :",combined)
             except FileNotFoundError:
                 print("File not found. Already deleted.")
             
       my_file.close()
       with open('UsedFacts.txt','a') as deleter:
           deleter.write("\n")
       deleter.close()

             
       with open('UsedImages.txt','r') as my_file_two:
           #
           my_data_two = my_file_two.read()
           my_data_two = my_data_two.split(prefix)

       for k in my_data_two:
         if k == "":
             pass
         elif k == "\n":
             pass
         else:
             try:
                 #
                 k = k.replace("\n","")
                 k = k.replace("\n","")
                 combined = str(prefix + k)
                 if combined.endswith(".jpg"):
                     os.remove('{0}'.format(combined))
                     print('[+] cleaning : ','{0}'.format(combined))
                 else:
                     print("Program attempted to delete an unwanted file. Prevented it :", combined)
             except FileNotFoundError:
                 print("File not found. Already deleted.")
       my_file_two.close()
       with open('UsedImages.txt','a') as deleter:
           #
           deleter.write("\n")
       deleter.close()

