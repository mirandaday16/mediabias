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

# Finding the number of captions on each website that contain 0, 1, 2, 3, and 4 main entities (4 is the max; see above)
# Row 1 is website, Row 5 is caption entities (listed), Row 9 is # of non-main ("Extra") entities in caption
def get_caption_counts(website):
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    with open(csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            if row[1] == website:
                if row[9] != "-":
                    if (len(row[5].split(',')) - int(row[9])) == 0:
                        zero += 1
                    elif (len(row[5].split(',')) - int(row[9])) == 1:
                        one += 1
                    elif (len(row[5].split(',')) - int(row[9])) == 2:
                        two += 1
                    elif (len(row[5].split(',')) - int(row[9])) == 3:
                        three += 1
                    elif (len(row[5].split(',')) - int(row[9])) == 4:
                        four += 1
                else:
                    if len(row[5].split(',')) == 0:
                        zero += 1
                    elif len(row[5].split(',')) == 1:
                        one += 1
                    elif len(row[5].split(',')) == 2:
                        two += 1
                    elif len(row[5].split(',')) == 3:
                        three += 1
                    elif len(row[5].split(',')) == 4:
                        four += 1
    print("\n" + website + ":")
    print("zero: ", zero)
    print("one: ", one)
    print("two: ", two)
    print("three: ", three)
    print("four: ", four)
    return [zero, one, two, three, four]


get_caption_counts('FOX')

get_caption_counts('NYT')

# FOX:
# zero:  8
# one:  54
# two:  27
# three:  8
# four:  3
#
# NYT:
# zero:  0
# one:  60
# two:  28
# three:  9
# four:  3
