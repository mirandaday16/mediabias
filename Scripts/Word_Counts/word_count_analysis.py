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


# Returns a dictionary with article headlines as keys and a list containing the caption word count (word tokens) and
# the caption entity token count (from data_csv_file) as the values.
def create_data_dict():
    data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Get length of tokenized caption, excluding punctuation (word count)
            caption = str(row[3])
            tokenized_caption = word_tokenize(caption)
            caption_words = [word.lower() for word in tokenized_caption if word.isalpha()]
            print(caption)
            print(caption_words)
            # Ignore articles without captions
            if row[3] != "NONE" and row[6] != "-":
                # len(caption_words) is the number of word tokens in the caption. row[9] is the manually annotated #
                # of entity name tokens.
                data[row[1]] = [len(caption_words), row[9]]
    return data


