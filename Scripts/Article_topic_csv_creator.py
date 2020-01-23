# Writes article "main events" and dates to CSV file so that equivalent articles can be found on other news sites
import Article_Crawler_Functions
import csv
import os
import json


# Gets publication date of equivalent article from other news source in initial dataset
def get_date(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    date = json_obj['date']
    return date


# Gets "main event", or topic, data of equivalent article from other news source in initial dataset
def get_main_event(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    main_event = json_obj['main-event']
    return main_event


# Gets article alignment number from json filename in initial dataset
def get_number(filename: str):
    return filename.split("_")[0]


def main():
    # Create or open article topics csv file
    with open('../Data/Processed_Metadata/article_topics.csv', mode='w') as article_topics_table:
        topics_writer = csv.writer(article_topics_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write header rows
        topics_writer.writerow(['Alignment #', 'Topic', 'Date', 'Headline', 'Publication Date', 'URL'])
        for file in sorted(os.listdir(Article_Crawler_Functions.directory)):
            website = Article_Crawler_Functions.get_website(file)
            # Using Fox as baseline, since corresponding topics are all the same and dates should be the
            # same or similar to NYT
            if website == 'FOX':
                topics_writer.writerow([get_number(file), get_main_event(Article_Crawler_Functions.directory + file),
                                        get_date(Article_Crawler_Functions.directory + file), "", "", ""])


main()
