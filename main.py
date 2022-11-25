import tweepy
import time
import config



auth = tweepy.OAuthHandler(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret)
auth.set_access_token(access_token=config.access_token, access_token_secret=config.access_token_secret)
print(consumer_key)
api = tweepy.API(auth)
client = tweepy.Client(consumer_key, consumer_secret, access_token, access_token_secret)

FILE_NAME = 'last.txt'
GIF = 'image.jpg'

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

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if 'location:' in tweet.full_text.lower():
            
            print("Location: " + str(tweet.id) + " - " + tweet.full_text.lower())
            api.update_with_media(GIF, "@"+ tweet.user.screen_name, in_reply_to_status_id=tweet.id)

        elif 'location:' not in tweet.full_text.lower():
            print("Liked!: " + str(tweet.id) + " - " + tweet.full_text.lower())

        api.create_favorite(tweet.id)
        store_last_seen(FILE_NAME, tweet.id)

# client = tweepy.Client(consumer_key=config.consumer_key, consumer_secret=config.consumer_secret,
#                         access_token=config.access_token, access_token_secret=config.access_token_secret)
                     
# def reply():
#     response=client.get_users_mentions(config.userId) 
#     print(response)
#     #print(config.userId)
#     #response = client.create_tweet(text='test 3')
while True:
    reply()
    time.sleep(30)