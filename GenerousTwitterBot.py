import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	follower.follow()
	