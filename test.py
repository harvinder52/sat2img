import tweepy
import config


# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

client = tweepy.Client( consumer_key=config.consumer_key,
                        consumer_secret=config.consumer_secret,
                        access_token=config.access_token,
                        access_token_secret=config.access_token_secret)

response = client.create_tweet(
    text="hello @harvindergeek"
)
print(f"https://twitter.com/user/status/{response.data['id']}")