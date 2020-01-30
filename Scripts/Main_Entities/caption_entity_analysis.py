# Creates three matplotlib visualizations of entity match between captions and articles
import json
import Article_Crawler_Functions
import csv
import os
import matplotlib


# Returns a dictionary with article headlines as keys and a lit containing website, match rate,
# extra caption entity count, and journalist name count as the values.
def create_data_dict():
    data = {}
    with open("../Data/processed_data/caption_main_figures_edited.csv", 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[3] != "NONE":
                data[row[1]] = [row[0], row[6], row[7], row[8]]
    return data


def main():
    create_data_dict()
    # Create a matplotlib visualization of entity match rate by website

    # Create a matplotlib visualization of extra named entities in captions by website

    # Create a matplotlib visualization of extra named entities in captions, excluding journalist names


main()