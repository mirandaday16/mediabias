# Writes a csv file containing a list of aligned article pairs which BOTH contain media/captions.
# This offers a different approach to website comparison than previous analyses, which considered ALL articles with
# media/captions, regardless of website (and ended up with a different number of articles from each website).

import csv

source_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                  "caption_general_analysis_combined.csv"

url_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
               "caption_main_figures_edited.csv"


# Returns a dictionary with Article IDs as keys and Headlines as values.
# Only includes aligned article pairs which both contain media/captions.
def create_article_id_list():
    all_ids = []
    paired_ids = []
    with open(source_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            all_ids += row[:1]
    for i in range(len(all_ids) - 1):
        if all_ids[i][0:2] == all_ids[(i + 1)][0:2]:
            paired_ids.append(all_ids[i])
            paired_ids.append(all_ids[i + 1])
    return paired_ids


# Returns a dictionary with Article IDs as keys and URLs as values.
# Does NOT check for aligned article pairs, as this will be checked in the next function.
def create_metadata_dict():
    metadata = {}
    with open(url_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Article ID : Headline, URL
            metadata[row[0]] = [row[2], row[3]]
    return metadata


def create_combined_dict(id_list, metadata_dict):
    combined = {}
    for key in metadata_dict:
        if key in id_list:
            combined[key] = metadata_dict[key]
    return combined


def main():
    print(create_combined_dict(create_article_id_list(), create_metadata_dict()))


main()
