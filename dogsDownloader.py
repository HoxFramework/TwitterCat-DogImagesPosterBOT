import urllib.request
import requests
import json
import random
import string

def dog():
    #
    for k in range(1,51):
        print('Beginning file download with urllib2...Operation {0} out of 50'.format(k))
        url = 'https://some-random-api.ml/img/dog'
        url = requests.get(url)
        url = json.loads(url.text)
        url = url['link']

        response = requests.get(url)
        setup = str(random.choice(string.digits)) + str(random.choice(string.digits)) + str(random.choice(string.digits))
        if response.status_code == 200:
            with open("./pets/doggos/dog{}.jpg".format(setup), 'wb') as f:
                f.write(response.content)

        req = requests.get("https://some-random-api.ml/facts/dog")
        qoute = req.text
        key = json.loads(qoute)
        #print("[+] Qoute:\n",key['fact'])

        myqoute = key['fact']

        with open('./pets/doggofactos/dog{}.txt'.format(setup), 'w+') as file:
            file.write(myqoute)
        file.close()
        
        print("[*] DONE !")


