import json
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Our current directory
directory = "../Data/JSON files/emnlp19_BASIL/data/"


# Returns source website: either HPO, FOX, or NYT
def get_website(filename: str):
    return filename.split(".")[0].split("_")[1].upper()


# Gets URL by searching JSON object for each file. Also prints file path, title, and URL
def get_url(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    url = json_obj['url'].split("?")[0]
    # These print statements help keep track of articles in real time as they are being analyzed
    print("FILENAME: " + json_file_path)
    print("TITLE: " + json_obj["title"])
    print("URL: " + url)
    return url


def get_headline(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    headline = json_obj["title"]
    if headline != "":
        return headline
    # The below accounts for rare instances where article headline was not recorded in json file
    else:
        req = Request(get_url(json_file_path), headers={'User-Agent': 'Mozilla/5.0'})
        try:
            page_content = urlopen(req).read()
        except urllib.error.HTTPError:
            return "HTTP Error"
        except urllib.error.URLError:
            return "URL Error"
        else:
            soup = BeautifulSoup(page_content, "html.parser")
            header = soup.find('h1')
            if header is not None:
                headline = header.find("span")
                if headline is not None:
                    headline_text = str(headline.getText())
                return headline_text


# Returns media link (image or video)
def get_media(url):
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
            # Accounts for The Caucus header image, which is not useful
            if soup.find('img')['src'] != "https://static01.nyt.com/images/blogs_v5/thecaucus/thecaucus_post.png":
                return soup.find('img')['src']


# FOX: Determines whether media is an image or video
def fox_get_media_type(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        page_content = urlopen(req).read()
    except urllib.error.HTTPError:
        return "HTTP Error"
    except urllib.error.URLError:
        return "URL Error"
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        if soup.find('div',{'class': 'video-container'}) is not None:
            return 'VIDEO'
        elif soup.find('div',{'class': 'm'}) is not None:
            return 'IMAGE'


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
        if fox_get_media_type(url) == "IMAGE":
            for div in soup.find_all('div'):
                img = div.find('img', alt=True)
                if img is not None:
                    if img['alt'] is not None:
                        return img['alt']
        elif fox_get_media_type(url) == "VIDEO":
            for div in soup.find_all('div'):
                vid = div.find('video', alt=True)
                if vid is not None:
                    if vid['alt'] is not None:
                        return vid['alt']


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
        if get_media(url) is not None:
            if "video" in get_media(url):
                return 'VIDEO'
            elif get_media(url) is not None:
                return 'IMAGE'


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
        if nyt_get_media_type(url) == "IMAGE":
            for img in soup.find_all('img'):
                alt = img.find('img', alt=True)
                if alt is not None:
                    if alt['alt'] is not None:
                        return alt['alt']


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
        captions = soup.find('figcaption')
        if captions is not None:
            cap = captions.find("span")
            if cap is not None:
                cap_text = str(cap.getText())
                if cap_text != "":
                    if cap_text[0] == "\n":
                        return cap_text[1:]
                    else:
                        return cap_text

