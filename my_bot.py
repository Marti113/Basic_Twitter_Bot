import tweepy
import secret_keys
import time
print('this is my twitter bot')


CONSUMER_KEY= secret_keys.CONSUMER_KEY
CONSUMER_SECRET= secret_keys.CONSUMER_SECRET
ACCESS_KEY=secret_keys.ACCESS_KEY
ACCESS_SECRET=secret_keys.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                    last_seen_id,
                    tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + "-"+ mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if 'fail' in  mention.full_text.lower():
            print("found the fail")
            api.update_status('@' + mention.user.screen_name + '#Woot', mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)
