import os
import Article_Crawler_Functions


# Writes web page details to txt outfile in list form
def write_text_list(url, headline, outfile, website, count):
    media_link = Article_Crawler_Functions.get_media(url)
    if website == "FOX":
        alt_text = (Article_Crawler_Functions.fox_get_alt_text(url))
        caption = Article_Crawler_Functions.fox_get_captions_text(url)
        media_type = Article_Crawler_Functions.fox_get_media_type(url)
    elif website == "NYT":
        alt_text = Article_Crawler_Functions.nyt_get_alt_text(url)
        caption = Article_Crawler_Functions.nyt_get_captions_text(url)
        media_type = Article_Crawler_Functions.nyt_get_media_type(url)
    else:
        alt_text = None
        caption = None
        media_type = None
    outfile.write(str(count) + ". " + website + "\n" + "HEADLINE: " + headline +
                  "\n" + url + "\n")
    if media_link is not None and media_type is not None:
        outfile.write(media_type + ": " + media_link + "\n")
    else:
        outfile.write("No media\n")
    if alt_text is not None:
        outfile.write("ALT TEXT: " + alt_text + "\n")
    if caption is not None:
        outfile.write("CAPTION: " + caption)
        outfile.write("\n\n")
    else:
        outfile.write("\n")


# Iterates through all files and writes alt text/caption from each article to a new file, if it doesn't yet exist
def main():
    outfile = open("metadata.txt", 'w')
    count = 1
    for file in os.listdir(Article_Crawler_Functions.directory):
        website = Article_Crawler_Functions.get_website(file)
        if website != "HPO":
            url = (Article_Crawler_Functions.get_url(Article_Crawler_Functions.directory + file))
            headline = Article_Crawler_Functions.get_headline(Article_Crawler_Functions.directory + file)
            write_text_list(url, headline, outfile, website, count)
            count += 1
    outfile.close()


main()
