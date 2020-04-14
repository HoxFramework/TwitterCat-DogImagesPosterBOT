import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

def goTweet(textfile,imagefile):
        print("[+] Tweeting : ",textfile,"\nAnd pic:",imagefile,"\n")
        #access_token = 
        #access_token_secret = 

        #consumer_api = 
        #consumer_api_secret = 

        def OAuth():
            try:
                auth = tweepy.OAuthHandler(consumer_api, consumer_api_secret)
                auth.set_access_token(access_token, access_token_secret)
                return auth
            except Exception as e:
                return None
        oauth = OAuth()
        api = tweepy.API(oauth)

        #api.update_status('testtweet using API')
        api.update_with_media(imagefile, textfile)
        
        print("[+] SUCCESS ! Tweet posted.")


        

