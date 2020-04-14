import urllib.request
import requests
import json
import random
import string

def cat():
    #
    for k in range(1,51):
        print('Beginning file download with urllib2...Operation {0} out of 50'.format(k))
        url = 'https://cataas.com/cat'
        urllib.request.urlretrieve(url, './pets/cattos/cat{}.jpg'.format(setup))
        req = requests.get("https://catfact.ninja/fact?max_length=140")
        qoute = req.text
        key = json.loads(qoute)

        myqoute = key['fact']
        setup = str(random.choice(string.digits)) + str(random.choice(string.digits)) + str(random.choice(string.digits))
        with open('./pets/cattofactos/cat{}.txt'.format(setup),'w+') as file:
            file.write(myqoute)
        file.close()
        
        print("[*] DONE !")

