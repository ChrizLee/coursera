import sys
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf-8')

all_terms = {}
total = 0

def get_state(tweet):
    if 'place' in tweet and tweet['place'] is not None:
        print 'place', tweet['place']
    if 'geo' in tweet and tweet['geo'] is not None:
        print 'geo', tweet['geo']
    if 'coordinates' in tweet and tweet['coordinates'] is not None:
        print 'coordinates', tweet['coordinates']

def print_result():
    global all_terms, total

    for term, value in all_terms.iteritems():
        print '%s %.3f' % (term, value['count'] / total)


def main():
    tweet_file = codecs.open(sys.argv[1], "r", "utf-8")

    for line in tweet_file:
        tweet = json.loads(line)
        get_state(tweet)
        #if 'text' in tweet:
        #    scan_tweet(tweet['text'])

    #print_result()

    tweet_file.close()


if __name__ == '__main__':
    main()