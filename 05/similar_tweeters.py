import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from usertweets import UserTweets

def similar_tweeters(user1, user2):
    user1_tweets = UserTweets(user1)
    user2_tweets = UserTweets(user2)
    user1_token = []
    for tweets in user1_tweets._tweets:
        user1_token.append(word_tokenize(tweets[2]))

    

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)
    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)


