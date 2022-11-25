import tweepy
import config
import time
import requests
import os
import shutil

import requests

import geopy

# GIF = input('image.jpg')


auth = tweepy.OAuthHandler(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
FILE_NAME = 'last.txt'
GIF = open('image.jpg')

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(float(file_read.read().strip()))
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def tweet_image(url, message):
                
                filename = 'temp.jpg'
                request = requests.get(url, stream=True)
                print(request.status_code)
                if request.status_code == 200:
                    with open(filename, 'wb') as image:
                        for chunk in request:
                            image.write(chunk)

                    api.update_with_media(filename, status=message)
                    os.remove(filename)
                else:
                    print("Unable to download image")


url = 'http://example.com/img.png'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
               

api = tweepy.API(auth)
print(read_last_seen(FILE_NAME))
def reply():

    public_tweets = api.mentions_timeline(since_id=read_last_seen(FILE_NAME))
    for tweet in public_tweets:
        if 'Location:' in tweet.text:
            
            media = api.media_upload(filename='image.jpg')
            api.update_status(status="test media @"+ tweet.user.screen_name, media_ids=[media.media_id], in_reply_to_status_id=tweet.id)
            message = "Nice one"
            # api.update_with_media(GIF, status=message)
            tweet_image(url, message)
            store_last_seen(FILE_NAME, tweet.id)
            print("tweet successful")
            # api.update_status("location fetched for @"+ tweet.user.screen_name, in_reply_to_status_id=tweet.id)
            # api.update_status_with_media('', in_reply_to_status_id=tweet.id)
        elif 'location:' not in tweet.full_text.lower():
            print("Liked!: " + str(tweet.id) + " - " + tweet.full_text.lower())
    
        print(tweet.text)
        store_last_seen(FILE_NAME, tweet.id)
while True:
    reply()
    time.sleep(30)