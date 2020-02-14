# Combines longer caption_main_figures_edited file with manually edited and updated
# caption_general_analysis_edited.csv file. Primary purpose is to insert article IDs into the latter file.

import csv

ids_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/" \
                "Main_Entities/caption_main_figures_edited.csv"

data_csv_file = "/Data/processed_data/Caption_General_Analysis/caption_general_analysis_edited.csv"

# Returns a dictionary with headlines as keys and article ids as values
def create_id_dict():
    data = {}
    with open(ids_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            if row[2] != "Headline":
                # Headline = Article ID
                data[row[2]] = [row[0]]
    return data


# Returns a dictionary with headlines as keys and a list of all other values (website, caption, media type, media link,
# caption main entities, Media Main Entities,Media to Caption Match Rate) as values
def create_data_dict():
    data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            if row[1] != "Headline":
                # Headline = Website, Caption, Media Type, Media Link, Cap Main Entities, Media Main Entities,
                # Match Rate
                data[row[1]] = [row[0], row[2], row[3], row[4], row[5], row[6], row[7]]
    return data


def main():
    id = create_id_dict()
    data = create_data_dict()
    # Updated dictionary. Headline: Article ID, Website, Caption, Media Type, Media Link, Cap Main Entities,
    # Media Main Entities, Match Rate
    all_data = {**data, **id}
    merged_data = {}
    for key, value in all_data.items():
        if key in id and key in data:
            merged_data[key] = (value + data[key])
    print(merged_data)
    # Create or open metadata csv file
    with open('../Data/processed_data/Caption_General_Analysis/caption_general_analysis_combined.csv', mode='w') as metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        metadata_writer.writerow(['Article ID', 'Website', 'Headline', 'Caption', 'Media Type', 'Media Link',
                                  'Caption Entities','Media Main Entities', 'Match Rate'])
        # Set metadata values for each row and write to file
        for all_key in merged_data:
            article_id = merged_data[all_key][0]
            website = merged_data[all_key][1]
            headline = all_key
            caption = merged_data[all_key][2]
            media_type = merged_data[all_key][3]
            media_link = merged_data[all_key][4]
            cap_entities = merged_data[all_key][5]
            media_entities = merged_data[all_key][6]
            match_rate = merged_data[all_key][7]
            metadata_writer.writerow([article_id, website, headline, caption, media_type, media_link, cap_entities,
                                      media_entities, match_rate, "", ""])


main()
