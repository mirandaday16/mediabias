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


def main():
    # Create or open csv file for comparing main entities
    with open('../Data/processed_data/caption_main_figures.csv', mode='w') as metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write header rows
        metadata_writer.writerow(['Website', 'Headline', 'URL', 'Caption', 'Caption Main Entities',
                                  'Article Main Entities', 'Match Rate'])
        for file in sorted(os.listdir(Article_Crawler_Functions.directory)):
            # Assign metadata for each article
            website = Article_Crawler_Functions.get_website(file)
            headline = Article_Crawler_Functions.get_headline(Article_Crawler_Functions.directory + file)
            url = (Article_Crawler_Functions.get_url(Article_Crawler_Functions.directory + file))
            article_entities = get_main_entities(Article_Crawler_Functions.directory + file)
            if website == "FOX":
                caption = Article_Crawler_Functions.fox_get_captions_text(url)
            elif website == "NYT":
                caption = Article_Crawler_Functions.nyt_get_captions_text(url)
            else:
                caption = ''
            # Write metadata to file for FOX and NYT articles
            if website != "HPO":
                metadata_writer.writerow([website, headline, url, caption, "", article_entities, ""])


main()
