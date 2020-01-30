# Creates three matplotlib visualizations of entity match between captions and articles
import json
import csv
import os
import matplotlib
from matplotlib import pyplot as plt


# Returns a dictionary with article headlines as keys and a lit containing website, match rate,
# extra caption entity count, and journalist name count as the values.
def create_data_dict():
    data = {}
    with open("../Data/processed_data/Main_Entities/caption_main_figures_edited.csv", 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[3] != "NONE":
                data[row[1]] = [row[0], row[6], row[7], row[8]]
    return data


def main():
    data = create_data_dict()
    # Create a matplotlib visualization of entity match rate by website
    fox_matches = 0
    nyt_matches = 0
    fox_count = 0
    nyt_count = 0
    for key in data:
        if key[0] == "FOX":
            fox_matches += float(key[1])
            fox_count += 1
        elif key[0] == "NYT":
            nyt_matches += float(key[1])
            nyt_count += 1
        fox_avg = fox_matches / fox_count
        nyt_avg = nyt_matches / nyt_count
        x = ["NYT", "FOX"]
        y = [nyt_avg, fox_avg]
        plt.bar(x, y)
        plt.show()

    # Create a matplotlib visualization of extra named entities in captions by website

    # Create a matplotlib visualization of extra named entities in captions, excluding journalist names


main()
