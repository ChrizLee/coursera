import sys
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf-8')

all_terms = {}
total = 0

def scan_tweet(text):
    global all_terms, total
    #print text
    text =  repr(text)
    for word in text.split(' '):
        word = word.lower().strip(',.?#!:')
        if not word.isalpha() or word[0] == '@':
            continue          
        elif not word in all_terms:
            all_terms[word] = {}
            all_terms[word]['count'] = 1.0
            total += 1.0         
        else:           
            all_terms[word]['count'] += 1.0
            total += 1.0

def print_result():
    global all_terms, total

    for term, value in all_terms.iteritems():
        print '%s %.3f' % (term, value['count'] / total)


def main():
    tweet_file = codecs.open(sys.argv[1], "r", "utf-8")

    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            scan_tweet(tweet['text'])

    print_result()

    tweet_file.close()


if __name__ == '__main__':
    main()