import tweepy

print('this is my twitter bot')

CONSUMER_KEY= 'S2jrVYEzi3judBMYKhGC0fcrK'
CONSUMER_SECRET= 'tZM1K9b2TgVW3uAtD0hgPJP4heXk5RSJPLA2qYhQw9yTibohhf'
ACCESS_KEY='1383185090759385089-WZLFVmHrO88MG5eF7CR1XYARhhby4I'
ACCESS_SECRET='Ne22JyoF06bpYCk4sEtVnDasvI4tYfpuul7XnD91aq7t6'

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