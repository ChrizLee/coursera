import sys
import codecs
import json
import math

reload(sys)
sys.setdefaultencoding('utf-8')

def get_hashtag(tweet):
    if 'entities' in tweet:
        hashtags = tweet['entities']['hashtags']
        if hashtags:
            for tag in hashtags:
                return repr(tag['text'])
    return ""

def insert_top_ten(tag, top_ten):
    start, end  = 0, 9
    if top_ten[end]['count'] > tag['count']: 
        return top_ten

    count = tag['count']
    while not start == end:
        i = (start + end) / 2
        curr_count = top_ten[i]['count']
        if count > curr_count:
            end = i
        else:
            start = i + 1
    
    new_list = top_ten[0:start]
    new_list.append(tag)
    new_list.extend(top_ten[start:9])
    return new_list


def main():
    tweet_file = codecs.open(sys.argv[1], "r", "utf-8")

    tags = {}
    top_ten = []
    for i in range(10):
        top_ten.append({'text': '', 'count': 0})

    for line in tweet_file:
        tweet = json.loads(line)
        tag = get_hashtag(tweet)
        if tag:
            if not tag in tags:
                tags[tag] = { 'text': tag, 'count': 1 }
            else:
                tags[tag]['count'] += 1

    for key, tag in tags.iteritems():
        top_ten = insert_top_ten(tag, top_ten)

    print top_ten

    tweet_file.close()


if __name__ == '__main__':
    main()