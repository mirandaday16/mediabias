# Finds # of captions per website (out of all articles WITH CAPTIONS) which contain ALL article main entities
# and NO article main entities.

import csv

data_file = "/Data/processed_data/Main_Entities/caption_main_figures_edited.csv"


# Finds # of captions from a given website with 100% main entity match rate
def find_perfect_match_rate(website):
    perfect_matches = 0
    with open(data_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Only check articles from certain website
            if row[1] == website:
                if row[7] == '1':
                    perfect_matches += 1
    return perfect_matches


# Finds # of captions from a given website with 0% main entity match rate
def find_zero_match_rate(website):
    zero_matches = 0
    with open(data_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Only check articles from certain website
            if row[1] == website:
                if row[7] == '0' and row[4] != 'NONE':
                    zero_matches += 1
    return zero_matches


def main():
    print("100% Matches:\n")
    print('FOX: ', find_perfect_match_rate('FOX'), "\n")
    print('NYT: ', find_perfect_match_rate('NYT'), '\n\n')
    print("0% Matches:\n")
    print('FOX: ', find_zero_match_rate('FOX'), '\n')
    print('NYT: ', find_zero_match_rate('NYT'), "\n")


main()
