import os, json, urllib.request
from bs4 import BeautifulSoup


directory = "./emnlp19_BASIL/data/"

def get_website(filename: str):
    return filename.split(".")[0].split("_")[1].upper()


def get_url(json_file_path: str):
    json_obj = json.load(open(json_file_path))
    url = json_obj['url'].split("?")[0]
    print("FILENAME: " + json_file_path)
    print("TITLE: " + json_obj["title"])
    print("URL: " + url)
    return url


def get_alt_text(url):
    page_content = urllib.request.urlopen(url)
    soup = BeautifulSoup(page_content, "html.parser")
    for div in soup.find_all('div'):
        img = div.find('img', alt=True)
        if img is not None:
            return img['alt']


def main():
    # outfile = open("metadata.txt", 'a')
    for file in os.listdir(directory):
        website = get_website(file)
        if website != "HPO":
            url = (get_url(directory + file))
            print(get_alt_text(url))
            break

    #     outfile.write(website + "\n" + alt_text + "\n\n")
    # outfile.close()

main()