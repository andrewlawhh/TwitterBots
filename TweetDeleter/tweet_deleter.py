import tweepy
from TweetDeleter.credentials import *

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def delete_tweets(filter : 'func' = lambda x : False) -> None:
    '''
    Deletes tweets on user's timeline where function(tweet) evaluates to true.

    For instance, if the user wished to delete all tweets containing the word "white":
        has_white = lambda tweet : 'white' in tweet.text
        delete_tweets(has_white)

    :param filter: function
    :return: None
    '''
    my_tweets = tweepy.Cursor(api.user_timeline).items()

    num_deleted = 0
    for tweet in my_tweets:
        if filter(tweet):
            api.destroy_status(tweet.id)
            print("Tweet deleted.")
            num_deleted += 1
    print(num_deleted, 'tweets deleted.')

def main():
    delete_tweets(lambda x : True)

if __name__ == '__main__':
    main()