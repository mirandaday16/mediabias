# Creates two matplotlib visualizations of word counts in articles, including and excluding entity names

# Note: Entity token count includes full names (with initials and suffixes) and titles used directly before entity
# names. It does not include pronouns referring to a main entity or party affiliation of a main entity, even if used as
# part of a title.

import csv
import numpy as np
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/" \
                "Main_Entities/caption_main_figures_edited.csv"


# Returns a dictionary with article headlines as keys and a list containing the website, caption word count
# (word tokens) and the caption entity token count (from data_csv_file) as the values.
def create_data_dict():
    data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore header row
            if row[0] != "Website":
                # Ignore articles without captions
                if row[3] != "NONE" and row[6] != "-" and row[9] != '-':
                    # Get length of tokenized caption, excluding punctuation (word count)
                    caption = str(row[3])
                    tokenized_caption = word_tokenize(caption)
                    caption_words = [word.lower() for word in tokenized_caption if word.isalpha()]
                    # row[0] is website name, len(caption_words) is the number of word tokens in the caption.
                    # row[9] is the manually annotated of entity name tokens.
                    data[row[1]] = [row[0], len(caption_words), int(row[9])]
    return data


# Formats matplotlib based on average data - adjusted to handle wc data
def plot_data(nyt_avg, fox_avg, file_path, title, y_label):
    x_val = [0, 1]
    y_val = [nyt_avg, fox_avg]
    plt.bar(x_val, y_val)
    labels = ["NYT", "FOX"]
    plt.xticks(x_val, labels)
    plt.ylabel(y_label)
    y_pos = np.arange(len(x_val))
    plt.yticks(np.arange(0, (max(y_val) + 1), 1))
    plt.title(title)
    plt.bar(y_pos, y_val, color=["blue", "red"])
    for i in range(len(x_val)):
        plt.text(x=x_val[i] - 0.1,
                 y=y_val[i] + 0.005,
                 s=y_val[i],
                 size=8)
    plt.savefig(file_path)
    plt.show()


# Create a matplotlib visualization of average total word count of captions on each website
def plot_basic_word_count(data):
    fox_words = 0
    nyt_words = 0
    fox_article_count = 0
    nyt_article_count = 0
    for key in data:
        if data[key][0] == "FOX":
            fox_words += data[key][1]
            fox_article_count += 1
        elif data[key][0] == "NYT":
            nyt_words += data[key][1]
            nyt_article_count += 1
    # Get average match rates for each site
    fox_avg = fox_words / fox_article_count
    nyt_avg = nyt_words / nyt_article_count
    # Plot data
    plot_data(nyt_avg, fox_avg, '/Users/mirandadayadkins/Desktop/'
                                                        'Media_Bias/Data/processed_data/Word_Counts/'
                                                        'basic_word_counts.png',
                                      'Average Total Word Count of Captions', '# of word tokens present in caption')


# Create a matplotlib visualization of average total word count of captions on each website, not including entity names
def plot_word_count_without_entities(data):
    fox_words = 0
    nyt_words = 0
    fox_article_count = 0
    nyt_article_count = 0
    for key in data:
        if data[key][0] == "FOX":
            fox_words += (data[key][1] - data[key][2])
            fox_article_count += 1
        elif data[key][0] == "NYT":
            nyt_words += (data[key][1] - data[key][2])
            nyt_article_count += 1
    # Get average match rates for each site
    fox_avg = fox_words / fox_article_count
    nyt_avg = nyt_words / nyt_article_count
    # Plot data
    plot_data(nyt_avg, fox_avg, '/Users/mirandadayadkins/Desktop/'
                                                        'Media_Bias/Data/processed_data/Word_Counts/'
                                                        'word_counts_without_entities.png',
                                      'Average Word Count of Captions (EXCLUDING main entities)',
                                      '# of word tokens present in caption')


def main():
    data = create_data_dict()
    # plot_basic_word_count(data)
    plot_word_count_without_entities(data)


main()
