import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

# parse the setiment file and put score of word into a dictionary
def score_term(term_file):
	scores = {} # initialize an empty dictionary
	for line in term_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	#print scores.items() # Print every (term, score) pair in the dictionary
	return scores;

def calc_score(scores, text):
	

def get_tweets(tweet_file):
	tweets = json.load(tweet_file)
	print len(tweets)
	for t in tweets:
		text = 

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

    try: 
    	term_score = score_term(sent_file)
    finally:
	    sent_file.close()
	    tweet_file.close()

if __name__ == '__main__':
    main()
