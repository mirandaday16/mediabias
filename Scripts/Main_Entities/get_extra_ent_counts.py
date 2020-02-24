# Finds max and min # of extra entities per website (out of all articles WITH CAPTIONS)

import csv

data_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
            "caption_main_figures_edited.csv"


# Finds maximum number of extra entities in the captions from a given website
def find_max_extra_entities(website):
    max_extras = 0
    with open(data_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Only check articles from certain website
            if row[1] == website:
                try:
                    if int(row[8]) > max_extras:
                        max_extras = int(row[8])
                except ValueError:
                    continue
    return max_extras


# Uses previous function to find the minimum number of extra entities in the captions from a given website
def find_min_extra_entities(website, max_extras):
    min_extras = max_extras
    with open(data_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Only check articles from certain website
            if row[1] == website:
                try:
                    if int(row[8]) < min_extras:
                        min_extras = int(row[8])
                except ValueError:
                    continue
    return min_extras


def main():
    print("Max # of Extra Entities:\n")
    fox_max_extras = find_max_extra_entities('FOX')
    nyt_max_extras = find_max_extra_entities('NYT')
    print('FOX: ', fox_max_extras, "\n")
    print('NYT: ', nyt_max_extras, '\n\n')
    print("0% Matches:\n")
    print('FOX: ', find_min_extra_entities('FOX', fox_max_extras), '\n')
    print('NYT: ', find_min_extra_entities('NYT', nyt_max_extras), "\n")


main()
