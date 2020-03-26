# Uses MPQA download file (originally .tff, manually copy/pasted to .txt) to create a usable csv file for
# sentiment analysis

import csv


def create_data_dict():
    source_file = open(r"/Users/mirandadayadkins/Desktop/Media_Bias/MPQA_Lexicon/MPQA_Lexicon.txt", "r")
    data_dict = {}
    row_count = 0
    for line in source_file:
        data_dict[row_count] = []
        split_line = line.split(" ")
        for string in split_line:
            content_word = string.lstrip("=")
            data_dict[row_count].append(content_word)
    print(data_dict)
    return data_dict


# TODO: get data dictionary creator working so I can use it to build a csv file

create_data_dict()