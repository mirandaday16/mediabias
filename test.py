import os, json
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
    page_content = urlopen(req).read()
    soup = BeautifulSoup(page_content, "html.parser")
    for div in soup.find_all('div'):
        img = div.find('img', alt=True)
        video = div.find('video', alt=True)
        if img is not None:
            if img['alt'] is not None:
                # Accounts for captions that only contain the website name, e.g. "HuffPost"
                if len(img['alt']) > 15:
                    return img['alt']
        elif video is not None:
            if video['alt'] is not None:
                if len(video['alt']) > 15:
                    return video['alt']


# Gets caption text for first image or video
# def get_captions(url):


# Iterates through all files and writes alt text from each article to a new file
def main():
    outfile = open("metadata.txt", 'w')
    for file in os.listdir(directory):
        # website = get_website(file)
        url = (get_url(directory + file))
        alt_text = (get_alt_text(url))      # Still needs to be implemented
        caption = get_captions(url)
        if alt_text is not None:
            if caption is not None:
                outfile.write(url + "\n" + alt_text + "\n" + caption +"\n\n")
    outfile.close()

main()