import sys
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf-8')

scores = { 'word': {}, 'phrase': {} } # initialize an empty dictionary
all_terms = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp))

# parse the setiment file and put score of word and phrase into two dicts
def parse_score(term_file):
    global scores

    for line in term_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        if ' ' in term:
            scores['phrase'][term] = int(score)
        else:
            scores['word'][term] = int(score)


# get score of a given text
def get_score(text):
    global scores

    score = 0
    # add word scores first
    for word in text.split(' '):
        word = word.lower()
        if word in scores['word']:
            score += scores['word'][word]

    # add phrase scores and, if duplicated with word, substract the word score
    for phrase, phrase_score in scores['phrase'].iteritems():
        if phrase in text:
            score += phrase_score
            for word_in_phrase in phrase.split(' '):
                if word_in_phrase in scores['word']:
                    score -= scores['word'][word_in_phrase]

    return score

def scan_tweet(text):
    global scores, all_terms
    #print text
    text =  repr(text)
    score = get_score(text)
    for word in text.split(' '):
    	word = word.lower().strip(',.?#!:')
        if not word.isalpha() or word in scores['word'] or word[0] == '@':
            continue
    	elif not word in all_terms:
    		all_terms[word] = {}
    		all_terms[word]['count'] = 1.0
    		all_terms[word]['score'] = float(score)
    	else:    		
    		all_terms[word]['count'] += 1.0
    		all_terms[word]['score'] += float(score)

def print_result():
	global all_terms

	for term, value in all_terms.iteritems():
		print '%s %.3f' % (term, value['score'] / value['count'])


def main():
    sent_file = codecs.open(sys.argv[1], "r", "utf-8")
    tweet_file = codecs.open(sys.argv[2], "r", "utf-8")
    #hw()

    sent_file_content = sent_file.readlines()
    tweet_file_content = tweet_file.readlines()

    #lines(sent_file_content)
    #lines(tweet_file_content)

    parse_score(sent_file_content)
    for line in tweet_file_content:
        tweet = json.loads(line)
        if 'text' in tweet:
            scan_tweet(tweet['text'])

    print_result()

    sent_file.close()
    tweet_file.close()


if __name__ == '__main__':
    main()
