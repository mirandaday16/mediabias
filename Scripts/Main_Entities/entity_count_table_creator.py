# Creates a comparison chart of ALIGNED articles from both websites and the number of captions from each site
# which contain 0 MAIN entities, 1 main entity, etc.

import plotly.graph_objects as graph_obj

aligned_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                   "aligned_articles_with_captions.csv"

main_entities_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
                         "caption_main_figures_edited.csv"


# Creates a dictionary of article metadata from ALIGNED article set. {Article ID : Headline}

# Creates a dictionary of caption entity data from caption main figures file, with articles narrowed down to the
# ALIGNED article set. {Article ID : [Website, Match Rate]}
def create_match_rate_dict():



# Creates a plotly table to visualize the distribution of main entity counts in captions, by website
def create_table():
    table = graph_obj.Figure(data=[graph_obj.Table(header=dict(values=['A Scores', 'B Scores']),
                                   cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                          ])
    fig.show()