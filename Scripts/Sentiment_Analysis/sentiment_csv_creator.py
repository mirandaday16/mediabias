# Writes sentiment data to a csv file to compare attributes using MPQA Subjectivity Lexicon
import csv

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                "aligned_articles_with_captions.csv"


# Returns a dictionary with article IDs as keys and a list containing # of positive sentiment words,
# list of positive sentiment words, # of negative sentiment words, list of negative sentiment words, and total
# word count as values
def create_data_dict(website):
    sentiment_data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Find articles from specified website
            if row[0][2:] != website:
                # Article ID = # Positive, Positive List, # Negative, Negative List, Total WC
                sentiment_data[row[0]] = ['', '', '', '', '']
    return sentiment_data


# Creates a csv table to store sentiment data for comparison
def main():
    nyt_data = create_data_dict('NYT')
    fox_data = create_data_dict('FOX')
    print("NYT: ", nyt_data)
    print("FOX: ", fox_data)

main()
