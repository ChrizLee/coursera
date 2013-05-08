import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

# parse the setiment file and put score of word and phrase into two dicts
def parse_score(term_file):
    scores = { 'word': {}, 'phrase': {} } # initialize an empty dictionary
    print scores.items()
    for line in term_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        if ' ' in term:
            scores['phrase'][term] = int(score)
        else:
            scores['word'][term] = int(score)

    #print len(scores['phrase'].items())
    #print len(scores['word'].items())

    return scores

# get score of a given text
def get_score(text, scores):
    score = 0
    # add word scores first
    for word in  text.split(' '):
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

def cal_senti_score(tweet_file, term_score):
    for line in tweet_file:
        tweet = json.loads(line)
        if not 'text' in tweet:
            print 0
        else:
            print '%d' % get_score(tweet['text'], term_score)

        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

    try: 
        term_score = parse_score(sent_file)
        cal_senti_score(tweet_file, term_score)
    finally:
        sent_file.close()
        tweet_file.close()

if __name__ == '__main__':
    main()
