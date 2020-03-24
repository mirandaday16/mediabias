# Writes sentiment word data to a spreadsheet to compare attributes, using only aligned articles
import csv

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                "caption_general_analysis_combined.csv"


# Returns a dictionary with article IDs as keys and a list containing the # of positive sentiment words,
# of negative sentiment words, total word count, list of positive words, and list of negative words as values
def create_data_dict(website):
    sentiment_data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[0][2:] != website:
                # Article ID = # Positive, # Negative, Total WC, List Positive, List Negative
                sentiment_data[row[0]] = ['', '', '', '', '']
    return sentiment_data


def main():
    NYT_data = create_data_dict('NYT')
    FOX_data = create_data_dict('FOX')
