# Creates a comparison chart of ALIGNED articles from both websites and the number of captions from each site
# which contain 0 MAIN entities, 1 main entity, etc.

import plotly.graph_objects as graph_obj
import csv
import os
import psutil
import orca
from Scripts import parallel_articles_list_creator

main_entities_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
                         "caption_main_figures_edited.csv"

save_location = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
                "main_entity_count_in_captions.png"


# Creates a dictionary of caption entity data from caption main figures file, with articles narrowed down to the
# ALIGNED article set. {Article ID : [Website, Match Rate]}
def create_match_rate_dict():
    data = {}
    aligned_ids = parallel_articles_list_creator.create_article_id_list()
    with open(main_entities_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles that are not aligned/parallel
            if row[0] in aligned_ids:
                # Article ID = Website, Match Rate
                data[row[0]] = [row[1], row[8]]
    return data


# Gets the max # of article main entities which appear in any caption in the aligned list.
def get_max_entities(data_dict):
    max_entities = 0
    for key in data_dict:
        try:
            if int(data_dict[key][1]) > max_entities:
                max_entities = int(data_dict[key][1])
        except ValueError:
            continue
    return max_entities


# Creates a plotly table to visualize the distribution of main entity counts in captions, by website
def create_table(data_dict, maximum):
    possible_values = []
    for i in range(maximum + 1):
        possible_values.append(i)
    possible_values.append("TOTAL")

    # Initialize values which will be used in table columns
    nyt_values = [0] * (maximum + 1)
    nyt_total = 0
    fox_values = [0] * (maximum + 1)
    fox_total = 0

    # Get values for each possible # of entities, and add to total # of captions for each site (should be equal)
    for key in data_dict:
        if data_dict[key][0] == 'NYT':
            nyt_total += 1
            # Increment for # of entities value
            entities = 0
            try:
                if int(data_dict[key][1]) > 0:
                    entities = int(data_dict[key][1])
            except ValueError:
                continue
            nyt_values[entities] += 1
        elif data_dict[key][0] == 'FOX':
            fox_total += 1
            entities = 0
            try:
                if int(data_dict[key][1]) > 0:
                    entities = int(data_dict[key][1])
            except ValueError:
                continue
            fox_values[entities] += 1

    # Add total caption counts for final row in table
    nyt_values.append(nyt_total)
    fox_values.append(fox_total)

    table = graph_obj.Figure(data=[graph_obj.Table(header=dict(values=['# of Main Entities', '# of NYT captions',
                                                                       '# of FOX captions']),
                                                   cells=dict(values=[possible_values, nyt_values, fox_values]))
                                   ])
    table.show()
    table.to_image(format='png')


# Gets data for aligned article captions and then creates a table to display the data.
def main():
    create_table(create_match_rate_dict(), get_max_entities(create_match_rate_dict()))


main()
