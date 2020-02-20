# Writes a csv file containing a list of aligned article pairs which BOTH contain media/captions.
# This offers a different approach to website comparison than previous analyses, which considered ALL articles with
# media/captions, regardless of website (and ended up with a different number of articles from each website).

import csv

source_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/" \
                "Main_Entities/caption_main_figures_edited.csv"