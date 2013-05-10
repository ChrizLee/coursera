import sys
import codecs
import json
import math

reload(sys)
sys.setdefaultencoding('utf-8')

def get_hashtags(tweet):
    if 'entities' in tweet:
        hashtags = tweet['entities']['hashtags']
        return hashtags

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

def add_tag(tag, tags):
    tag_text = tag['text']
    if not tag_text in tags:
        tags[tag_text] = { 'text': tag_text, 'count': 1 }
    else:
        tags[tag_text]['count'] += 1


def main():
    tweet_file = codecs.open(sys.argv[1], "r", "utf-8")

    tags = {}
    top_ten = []
    for i in range(10):
        top_ten.append({'text': '', 'count': 0})

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_tag = get_hashtags(tweet)
      
        if not tweet_tag:
            continue
       
        for tag in tweet_tag:
            add_tag(tag, tags)

    for key, tag in tags.iteritems():
        top_ten = insert_top_ten(tag, top_ten)

    for tag in top_ten:
        print tag['text'], tag["count"]

    tweet_file.close()


if __name__ == '__main__':
    main()