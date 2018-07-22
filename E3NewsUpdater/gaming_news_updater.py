import tweepy
import time
from credentials import *

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.wait_on_rate_limit = True


# Helper function to get user ID by username
def get_id(user_name):
    return str(api.get_user(screen_name = user_name).id)

def get_name(id):
    return api.get_user(id = id).screen_name

account_names = ['E3', 'Sony', 'Bethesda',' BethesdaStudios', 'Microsoft',
                 'CDPROJEKTRED', 'Activision', 'BandaiNamcoUS', 'CapcomUSA_',
                 'Dell', 'EpicGames', 'nvidia', 'Ubisoft', 'EA', 'Naughty_Dog',
                 'anthemgame', 'Fallout', 'gameinformer', 'IGN', 'Nintendo',
                 'Treyarch']

followed_accounts = [get_id(name) for name in account_names]

# Set up stream to retweet
class GameAccListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            print('tweet by:', get_name(status.user.id))
            print('user id:', status.user.id)
            print('tweet text:', status.text)
            if status.text.startswith('RT @') or get_name(status.user.id) in account_names:
                print('RETWEET')
                api.retweet(status.id)
            time.sleep(5)
            # loop every 5 seconds
        except Exception as e:
            print(e)
        return True

    def on_error(self, status_code):
        print("error occurred")
        return True

    def on_exception(self, exception):
        print("exception occured", exception)
        return True

    def on_timeout(self):
        print('Timeout occurred')
        return True


def main():
    # Initialize listener and stream
    listener = GameAccListener()
    stream = tweepy.Stream(auth = auth, listener = listener)


    # Stream Filter
    try:
        stream.filter(follow = followed_accounts,
                      #track = ['#E3', '#Fallout76', '#BE3', '#Cyberpunk2077', '#E32018'],
                      async = True
                      )
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
