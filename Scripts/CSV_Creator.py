# Writes web page details to csv outfile in table form
import Article_Crawler_Functions
import assigning_article_ids
import csv
import os


def main():
    # Create or open metadata csv file
    with open('../Data/processed_data/metadata.csv', mode='w') as metadata_table:
        metadata_writer = csv.writer(metadata_table, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write header rows
        metadata_writer.writerow(['ID', 'Website', 'Headline', 'URL', 'Media Type', 'Media Link', 'Alt Text',
                                  'Caption Text'])
        for file in sorted(os.listdir(Article_Crawler_Functions.directory)):
            # Assign metadata for each article
            website = Article_Crawler_Functions.get_website(file)
            article_id = assigning_article_ids.get_article_id(file, website)
            headline = Article_Crawler_Functions.get_headline(Article_Crawler_Functions.directory + file)
            url = (Article_Crawler_Functions.get_url(Article_Crawler_Functions.directory + file))
            if Article_Crawler_Functions.get_media(url) is not None:
                media_link = Article_Crawler_Functions.get_media(url)
            else:
                media_link = ''
            if website == "FOX":
                alt_text = (Article_Crawler_Functions.fox_get_alt_text(url))
                caption = Article_Crawler_Functions.fox_get_captions_text(url)
                media_type = Article_Crawler_Functions.fox_get_media_type(url)
            elif website == "NYT":
                alt_text = Article_Crawler_Functions.nyt_get_alt_text(url)
                caption = Article_Crawler_Functions.nyt_get_captions_text(url)
                media_type = Article_Crawler_Functions.nyt_get_media_type(url)
            else:
                alt_text = ''
                caption = ''
                media_type = ''
            # Write metadata to file for FOX and NYT articles
            if website != "HPO":
                metadata_writer.writerow([article_id, headline, url, media_type, media_link, alt_text, caption])


main()
