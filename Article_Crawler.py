import os
import json
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

def get_headline(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    headline = json_obj["title"]
    return headline


# # FOX: Determines whether media is an image or video and returns media link
# def fox_get_media(url):


# FOX: Gets alt text of first image/video in the article, if it exists
def fox_get_alt_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        for div in soup.find_all('div'):
            img = div.find('img', alt=True)
            if img is not None:
                if img['alt'] is not None:
                    return img['alt']


# FOX: Gets caption text for first image or video
def fox_get_captions_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
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

# NYT: Determines whether media is an image or video
def nyt_get_media_type(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        if soup.find('video') is not None:
            return 'VIDEO'
        elif soup.find('img') is not None:
            return 'IMAGE'

# NYT: Returns media link
def nyt_get_media(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        if soup.find('video') is not None:
            return soup.find('video')['src']
        elif soup.find('img') is not None:
            return soup.find('img')['src']

# NYT: Gets alt text of first image/video in the article, if it exists
def nyt_get_alt_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        for img in soup.find_all('img'):
            alt = img.find('img', alt=True)
            if img is not None:
                if img['alt'] is not None:
                    return img['alt']


# NYT: Gets caption text for first image or video
def nyt_get_captions_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        captions = soup.find('figcaption', {'itemprop': 'caption description'})
        if captions is not None:
            cap = captions.find("span")
            if cap is not None:
                cap_text = str(cap.getText())
                if cap_text != "":
                    if cap_text[0] == "\n":
                        return cap_text[1:]
                    else:
                        return cap_text


# Writes web page details to outfile
def printText(url, headline, outfile, website, count):
    if website == "FOX":
        alt_text = (fox_get_alt_text(url))
        caption = fox_get_captions_text(url)
        media_link = fox_get_media(url)
        media_type = fox_get_media_type(url)
    elif website == "NYT":
        alt_text = nyt_get_alt_text(url)
        caption = nyt_get_captions_text(url)
        media_link = nyt_get_media(url)
        media_type = nyt_get_media_type(url)
    else:
        alt_text = None
        caption = None
    outfile.write(str(count) + ". " + website + "\n" + "HEADLINE: " + headline +
                  "\n")
    if media_link is not None:
        outfile.write(media_type + ": " + media_link + "\n")
    else:
        outfile.write("No media")
    if alt_text is not None:
        outfile.write("ALT TEXT: " + alt_text + "\n")
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
        if website != "HPO":
            url = (get_url(directory + file))
            headline = get_headline(directory + file)
            printText(url, headline, outfile, website, count)
            count += 1
    outfile.close()


main()
