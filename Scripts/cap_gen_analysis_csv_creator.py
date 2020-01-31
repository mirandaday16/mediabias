# Writes caption details to a spreadsheet to compare various attributes
import csv

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/" \
                "Main_Entities/caption_main_figures_edited.csv"

media_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/metadata.csv"


# Returns a dictionary with article headlines as keys and a lit containing website, match rate,
# extra caption entity count, and journalist name count as the values.
def create_data_dict():
    data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[3] != "NONE":
                # Headline = Website, Caption, Caption Main Entities
                data[row[1]] = [row[0], row[3], row[4]]
    return data


def create_media_dict():
    media = {}
    with open(media_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[6] != "":
                # Headline = Media Type, Media Link
                media[row[1]] = [row[3], str(row[4])]
    return media


def main():
    data = create_data_dict()
    media = create_media_dict()
    # Updated dictionary. Headline: Website, Caption, Caption Main Entities, Media Type, Media Link
    all_data = {**media, **data}
    merged_data = {}
    for key, value in all_data.items():
        if key in data and key in media:
            merged_data[key] = (value + media[key])
    # Create or open metadata csv file
    with open('../Data/processed_data/caption_general_analysis.csv', mode='w') as metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Set metadata values for each row and write to file
        for all_key in merged_data:
            website = merged_data[all_key][0]
            headline = all_key
            caption = merged_data[all_key][1]
            media_type = merged_data[all_key][3]
            media_link = merged_data[all_key][4]
            cap_entities = merged_data[all_key][2]
            metadata_writer.writerow([website, headline, caption, media_type, media_link, cap_entities, "", "", "", ""])


main()
