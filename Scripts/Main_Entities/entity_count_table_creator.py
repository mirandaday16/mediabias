# Creates a comparison chart of ALIGNED articles from both websites and the number of captions from each site
# which contain 0 MAIN entities, 1 main entity, etc.

import plotly.graph_objects as graph_obj
import csv
from Scripts import parallel_articles_list_creator

main_entities_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
                         "caption_main_figures_edited.csv"


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

# Gets values for each possible number of main entities for a given website
def get_caption_numbers(website):



# Creates a plotly table to visualize the distribution of main entity counts in captions, by website
def create_table(data_dict, maximum):
    possible_values = []
    for i in range(maximum + 1):
        possible_values.append(i)
    print(possible_values)
    table = graph_obj.Figure(data=[graph_obj.Table(header=dict(values=['# of Main Entities', 'NYT', 'FOX']),
                                                   cells=dict(values=[possible_values, [], []]))
                                   ])
    table.show()


# Gets data for aligned article captions and then creates a table to display the data.
def main():
    get_max_entities(create_match_rate_dict())
    create_table(create_match_rate_dict(), get_max_entities(create_match_rate_dict()))


main()
