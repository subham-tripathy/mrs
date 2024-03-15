# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis



# def analyze_sentiment(description):
#     sid = SentimentIntensityAnalyzer()
#     sentiment_scores = sid.polarity_scores(description)
#     return sentiment_scores['pos']




from textblob import TextBlob

def get_sentence_score(sentence):
    # Perform sentiment analysis
    analysis = TextBlob(sentence)
    # Get the sentiment score
    score = analysis.polarity
    # Map the score from -1 to 1 to 0 to 5
    score = (score + 1)*2.5
    return score