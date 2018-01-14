import sys
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer, TweetTokenizer
from usertweets import UserTweets
from nltk.corpus import stopwords

def similar_tweeters(user1, user2):
    user1_tweets = UserTweets(user1)
    user2_tweets = UserTweets(user2)
    user1_token = []
    for tweets in user1_tweets._tweets:
        print(''.join(tweets[2]))
        #user1_token.append(word_tokenize(''.join(tweets[2])))
    #print(user1_token)    
    #filter_crap(user1_token) 

    
def filter_crap(tweet_tokens):
    #remove stopwords
    stop = stopwords.words('english')
    result = []
    for item in tweet_tokens:
        result.append([words for words in item if words not in stop])
    print(result) 
    #remove urls
    
    #remove digits
    #for item in result:
    #   result = [words for words in item if words.isdigit()]

    #remove puntuation
    tokenizer = RegexpTokenizer(r'\w+')
    result = [tokenizer.tokenize(words) for words in result]
    #print(result)  
    #remove words which occurs only once
    result = [words for words in result if result.count(words) < 2]
    #remove words with less than 3 char
    result = [words for words in result if len(words) < 3]
    #print(result)
    
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)
    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)


