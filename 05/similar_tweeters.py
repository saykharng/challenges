import sys
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer, TweetTokenizer
from usertweets import UserTweets
from nltk.corpus import stopwords
from itertools import chain

def similar_tweeters(user1, user2):
    user1_tweets = UserTweets(user1)
    user2_tweets = UserTweets(user2)
    tknzr = TweetTokenizer(strip_handles = True, reduce_len = True)
    user1_token = []
    for tweets in user1_tweets._tweets:
        user1_token.append(tknzr.tokenize(tweets[2]))
    filter_crap(user1_token) 

    
def filter_crap(tweet_tokens):
    #remove stopwords
    stop = stopwords.words('english')
    result = []
    for item in tweet_tokens:
        result.append([words for words in item if words not in stop])
    #remove puntuation
    tokenizer = RegexpTokenizer(r'\w+')
    result = [tokenizer.tokenize(words) for words in list(chain.from_iterable(result))]
    #remove words which occurs only once
    temp_list = list(chain.from_iterable(result))
    result = [words for words in temp_list if temp_list.count(words) > 1]
    #remove URL from tweets
    result = [words for words in result if 'http' not in words]
    #remove digits
    result = [words for words in result if words.isalpha()]
    #remove words with less than 3 char
    result = [words for words in result if len(words) > 2]
    return result
    
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)
    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)


