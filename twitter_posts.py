import tweepy
# barier : AAAAAAAAAAAAAAAAAAAAAIJzqAEAAAAALnJoLN3rJCifAw%2FP6U4Q4EQPCO4%3DPn9LLLM8UdgV8Ux5aLBuijjgegnbAujvb7amGc4dKXoouLRL3D
# API key: hhsYFyo968HpIKmveNWr7JGOJ
# API key secret: OBvFxiyU5bP9IDPghXuef9SNLlIUOclYq0JbnKhLb1D4QZdbai

# Twitter API credentials
consumer_key = 'hhsYFyo968HpIKmveNWr7JGOJ'
consumer_secret = 'OBvFxiyU5bP9IDPghXuef9SNLlIUOclYq0JbnKhLb1D4QZdbai'
access_token = '1410887318186205184-AUd3bSYzMFr8TBmlKkPzpBDd2BBgnL'
access_token_secret = 'MtVXWQ0h1IROS71LbD95OXXkKXFoR6dHSkEZlvZWY1WdR'

# Twitter user ID
user_id = 'TARGET_USER_ID'

# Initialize Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch user's tweets
tweets = api.user_timeline(user_id=user_id, count=200, tweet_mode='extended')

# Create a text file to save tweets
with open('tweets.txt', 'w', encoding='utf-8') as file:
    for tweet in tweets:
        file.write(tweet.full_text + '\n')

print('Tweets saved to tweets.txt')
