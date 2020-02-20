# Writes a csv file containing a list of aligned article pairs which BOTH contain media/captions.
# This offers a different approach to website comparison than previous analyses, which considered ALL articles with
# media/captions, regardless of website (and ended up with a different number of articles from each website).

import csv

source_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Caption_General_Analysis/" \
                  "caption_general_analysis_combined.csv"

url_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/" \
               "caption_main_figures_edited.csv"


# Returns a list of Article IDs for articles in pairs which both contain media/captions.
def create_article_id_list():
    all_ids = []
    paired_ids = []
    # This file was chosen because it only contains articles with media/captions
    with open(source_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Add all Article IDs to first dictionary
            all_ids += row[:1]
    # Look for matching pairs and add only those matching IDs to second dictionary
    for i in range(len(all_ids) - 1):
        if all_ids[i][0:2] == all_ids[(i + 1)][0:2]:
            paired_ids.append(all_ids[i])
            paired_ids.append(all_ids[i + 1])
    return paired_ids


# Returns a dictionary with Article IDs as keys and URLs as values.
# Does NOT check for aligned article pairs, as this will be checked in the next function.
def create_metadata_dict():
    metadata = {}
    # This file was chosen because it contains headline and URL metadata for all articles
    with open(url_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Article ID : Headline, URL
            metadata[row[0]] = [row[2], row[3]]
    return metadata


# Creates a dictionary of article metadata for only those articles
# which are aligned with an article from the other website
def create_combined_dict(id_list, metadata_dict):
    combined = {}
    for key in metadata_dict:
        # Check whether article ID has an aligned match
        if key in id_list:
            # Move key and value to the new dictionary
            combined[key] = metadata_dict[key]
    return combined


# Creates a csv file to display metadata of aligned articles.
def create_csv(combined_dict):
    with open('../Data/processed_data/Caption_General_Analysis/aligned_articles_with_captions.csv', mode='w') as \
            metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Set metadata values for each row and write to file
        for key in combined_dict:
            # key = article ID, key[0] = headline, key[1] = url
            metadata_writer.writerow([key, combined_dict[key][0], combined_dict[key][1]])


def main():
    create_csv(create_combined_dict(create_article_id_list(), create_metadata_dict()))


main()
