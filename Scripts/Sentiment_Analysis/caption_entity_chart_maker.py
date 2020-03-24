# Creates chart of # of captions per website containing 0, 1, etc. MAIN entities
import csv
import os

# Our current directory
csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
           "caption_main_figures_edited.csv"


# Gets max number of main entities from csv file per website
def find_max_main_entities(website):
    max_main_entities = 0
    with open(csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            if row[1] == website:
                if len(row[5].split(',')) > max_main_entities:
                    max_main_entities = len(row[5].split(','))
    print(max_main_entities)
    return max_main_entities


# find_max_main_entities('FOX')
# Returns 4

# find_max_main_entities('NYT')
# Returns 4

