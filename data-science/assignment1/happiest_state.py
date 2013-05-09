import sys
import codecs
import json

reload(sys)
sys.setdefaultencoding('utf-8')

scores = { 'word': {}, 'phrase': {} } # initialize an empty dictionary

# parse the setiment file and put score of word and phrase into two dicts
def parse_score(term_file):
    global scores

    for line in term_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        if ' ' in term:
            scores['phrase'][term] = int(score)
        else:
            scores['word'][term] = int(score)

def get_state(tweet):
    if 'place' in tweet and tweet['place'] is not None:
        place = tweet['place']
        if place["country_code"] == "US" and place["place_type"] == "city":
            return place['full_name'][-2:]

    return ""


def get_score(tweet):
    global score

    if not "text" in tweet:
        return 0

    text = repr(tweet['text'])
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


def main():
    sent_file = codecs.open(sys.argv[1], "r", "utf-8")
    tweet_file = codecs.open(sys.argv[2], "r", "utf-8")

    parse_score(sent_file)

    states = {}
    for line in tweet_file:
        tweet = json.loads(line)
        state = get_state(tweet)
        if not state == "":
            score = get_score(tweet)
            if not state in states:
                states[state] = 0
            states[state] += score

    max_state = ""
    max_score = 0
    for state in states:
        score = states[state]
        if score > max_score:
            max_state = state
            max_score = score

    #print states
    print max_state

    sent_file.close()
    tweet_file.close()


if __name__ == '__main__':
    main()