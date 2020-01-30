# Creates table for comparing main entities in caption and article (to be finished manually)
import json
import Article_Crawler_Functions
import csv
import os


def get_main_entities(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    main_entities = json_obj["main-entities"]
    if main_entities:
        return main_entities
    else:
        return ""


# Get captions for articles updated via manual annotation (automatic capture leaves errors)
def get_updated_captions():
    captions = []
    with open("../Data/processed_data/metadata.csv", 'rt')as file:
        data = csv.reader(file)
        for row in data:
            captions.append(row[6])
    return captions


def main():
    # Create or open csv file for comparing main entities
    with open('../Data/processed_data/caption_main_figures.csv', mode='w') as metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write header rows
        metadata_writer.writerow(['Website', 'Headline', 'URL', 'Caption', 'Caption Main Entities',
                                  'Article Main Entities', 'Match Rate'])
        count = 1
        for file in sorted(os.listdir(Article_Crawler_Functions.directory)):
            # Assign metadata for each article
            website = Article_Crawler_Functions.get_website(file)
            headline = Article_Crawler_Functions.get_headline(Article_Crawler_Functions.directory + file)
            url = (Article_Crawler_Functions.get_url(Article_Crawler_Functions.directory + file))
            article_entities = get_main_entities(Article_Crawler_Functions.directory + file)
            captions = get_updated_captions()
            # Write metadata to file for FOX and NYT articles
            if website != "HPO":
                metadata_writer.writerow([website, headline, url, captions[count], '', article_entities, ""])
                count += 1


main()
