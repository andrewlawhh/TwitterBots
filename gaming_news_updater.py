import tweepy
import time
from credentials import *

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Helper function to get user ID by username
def get_id(user_name):
    return str(api.get_user(screen_name = user_name).id)

def get_name(id):
    return api.get_user(id).screen_name

followed_accounts = [get_id('E3'),
                            get_id('Sony'),
                            get_id('Bethesda'),
                            get_id('BethesdaStudios'),
                            get_id('Microsoft'),
                            get_id('CDPROJEKTRED'),
                            get_id('Activision'),
                            get_id('BandaiNamcoUS'),
                            get_id('CapcomUSA_'),
                            get_id('Dell'),
                            get_id('EpicGames'),
                            get_id('nvidia'),
                            get_id('Ubisoft'),
                            get_id('EA'),
                            get_id('Naughty_Dog')
                            ]

# Set up stream to retweet
class GameAccListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            print('tweet by:', get_name(status.user.id))
            print('user id:', status.user.id)
            print('tweet text :', status.text)

            # followed accounts list contains strings
            if str(status.user.id) in followed_accounts:
                print('retweeted tweet by', get_name(status.user.id))
                api.retweet(status.id)

            # loop every 15 seconds
            time.sleep(15)
        except Exception as e:
            print(e)
        return True

    def on_error(self, status_code):
        print("error : ", str(status_code))
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
