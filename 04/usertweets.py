from collections import namedtuple
import csv
import os

import tweepy

##from config import CONSUMER_KEY, CONSUMER_SECRET
##from config import ACCESS_TOKEN, ACCESS_SECRET
CONSUMER_KEY = '8JpOdh5D8ufSHm9uEZLmDEnpi'
CONSUMER_SECRET = 'uGCzK2LxvseEPoecYM84TeR7EOdnziopJLVEoxkDKaSbKNLBD5'
ACCESS_TOKEN = '3247378184-yLm1Iyo8aiI4BKHV4YSzuUzb6cWz5n4QT61Zc2Z'
ACCESS_SECRET = 'h4I9oj2yaGqsyd0wh7kBrMELI8oHhMuVngDMsMg8YCxjA'


DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100
output_file ='scrapped_tweet.csv'
Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id = None):
        """Get handle and optional max_id.
        Use tweepy.OAuthHandler, set_access_token and tweepy.API
        to create api interface.
        Use _get_tweets() helper to get a list of tweets.
        Save the tweets as data/<handle>.csv"""
        self.output_file = 'scrapped_tweet.csv'
        self.handle = handle
        self._count = 100
        self.max_id = max_id
        self.auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET, 'https://twitter.com')
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)
        self._tweets = self._get_tweets()
        self._save_tweets()
 
    def _get_tweets(self):
        """Hint: use the user_timeline() method on the api you defined in init.
        See tweepy API reference: http://docs.tweepy.org/en/v3.5.0/api.html
        Use a list comprehension / generator to filter out fields
        id_str created_at text (optionally use namedtuple)"""
        tweets = self.api.user_timeline(screen_name = self.handle, count = self._count, max_id = self.max_id)
        return [Tweet(item.id_str, item.created_at, item.text.replace('\n', '')) for item in tweets]
                
        #for tweet_object in self.api.user_timeline(screen_name = self.handle, max_id = self.max_id, count = NUM_TWEETS+1, tweet_mode = 'extended'):
            #yield tweet_object
        
    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets.
        If you use a namedtuple get the column names with Tweet._fields.
        Otherwise define them as: id_str created_at text
        You can use writerow for the header, writerows for the rows"""
        with open('scrapped_tweet.csv', 'w', newline='', encoding='utf-8') as csvfile:
            tweetwriter = csv.writer(csvfile)
            tweetwriter.writerow(Tweet._fields)
            tweetwriter.writerows(self._tweets)
                
    def __len__(self):
        """See http://pybit.es/python-data-model.html"""
        self_len = len(self._tweets)
        return self_len

    def __getitem__(self, pos):
        """See http://pybit.es/python-data-model.html"""
        return self._tweets[pos]


if __name__ == "__main__":
    for handle in ('pybites', 'elonmusk', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
