import tweepy
import time

auth = tweepy.OAuthHandler('8pScqXU7kEddPBwQIIAB7dEbc', 'Ai3vmKgPZSijOQEush2MZA3oiiezSQOjdjJ9uWyvFgVxbxIlzI')
auth.set_access_token('810392409834192896-bo5Oz6zPSETgzN0ASE2SRikuete1dT4', 'xiCH5jS2lIyHYUioiniz7S9mtiYXvgSbZLSyYYJmKC4UH')

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
	