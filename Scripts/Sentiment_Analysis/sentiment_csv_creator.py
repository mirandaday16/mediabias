# Writes sentiment data to a csv file to compare attributes using MPQA Sentiment Lexicon
import csv

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                "caption_general_analysis_combined.csv"


# Returns a list containing # of positive sentiment words,
#  list of positive sentiment words, # of negative sentiment words, list of negative sentiment words, and total
#  word count
def analyze_sentiment(caption):
    # analyzer = SentimentIntensityAnalyzer()
    word_count = 0
    pos_words = []
    neg_words = []
    for word in caption.split(" "):
        word_count += 1
        # word_sentiment = analyzer.polarity_scores(word)
        if word_sentiment['pos'] > 0.5:
            pos_words.append(word)
        elif word_sentiment['neg'] < 0.5:
            neg_words.append(word)
    return [len(pos_words), pos_words, len(neg_words), neg_words, word_count]


# Returns a dictionary with article IDs as keys and output from analyze_sentiment() as values
def create_data_dict(website):
    sentiment_data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        # Skip header row
        next(open_file)
        for row in open_file:
            # Find articles from specified website
            if row[0][2:] != website:
                # Article ID = # Positive, Positive List, # Negative, Negative List, Total WC
                sentiment_data[row[0]] = analyze_sentiment(row[3])
    return sentiment_data


# Creates a csv table to store sentiment data for comparison
def main():
    # nyt_data = create_data_dict('NYT')
    # fox_data = create_data_dict('FOX')
    # print(nyt_data)
    # print(SentimentIntensityAnalyzer.polarity_scores()


main()
