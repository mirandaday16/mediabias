import os, json
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Our current directory
directory = "./emnlp19_BASIL/data/"


# Returns source website: either HPO, FOX, or NYT
def get_website(filename: str):
    return filename.split(".")[0].split("_")[1].upper()


# Gets URL by searching JSON object for each file. Also prints file path, title, and URL
def get_url(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    url = json_obj['url'].split("?")[0]
    print("FILENAME: " + json_file_path)
    print("TITLE: " + json_obj["title"])
    print("URL: " + url)
    return url


# Gets alt text of first image/video in the article, if it exists
def get_alt_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        for div in soup.find_all('div'):
            img = div.find('img', alt=True)
            if img is not None:
                if img['alt'] is not None:
                    if img['alt'] == 'Video player loading':
                        return 'VIDEO'
                    # Accounts for captions that only contain the website name, e.g. "HuffPost"
                    if len(img['alt']) > 15:
                        return img['alt']
                    else:
                        return 'IMAGE'


# Gets caption text for first image or video
def get_captions_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        captions = soup.find('div',{'class': 'caption'})
        if captions is not None:
            cap = captions.find('p')
            if cap is not None:
                cap_text = str(cap.getText())
                if cap_text != "":
                    if cap_text[0] == "\n":
                        return cap_text[1:]
                    else:
                        return cap_text


# Writes web page details to outfile
def printText(url, outfile, website, count):
    alt_text = (get_alt_text(url))
    caption = get_captions_text(url)
    if alt_text is not None:
        outfile.write(str(count) + ". " + website + "\n" + url +
                      "\n" + "ALT TEXT: " + alt_text + "\n")
    if caption is not None:
        outfile.write("CAPTION: " + caption)
        outfile.write("\n\n")
    else:
        outfile.write("\n")


# Iterates through all files and writes alt text/caption from each article to a new file
def main():
    outfile = open("metadata.txt", 'w')
    count = 1
    for file in os.listdir(directory):
        website = get_website(file)
        url = (get_url(directory + file))
        printText(url, outfile, website, count)
        count += 1
    outfile.close()


main()
