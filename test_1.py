from bs4 import BeautifulSoup
import urllib.request
import os


def readFileNYT(file_name):
    infile = open(file_name)
    outfile = open("multi,model_data", "a")
    for line in infile:
        if "url" in line:
            url = line[7:-1]        # characters 7 through second to last, since there is a comma at the end
            outfile.write(line)     # unsure about this
            page_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(page_content)
            for soup_line in soup:
                if "meta itemprop" in soup_line:
                    outfile.write(soup_line)
                elif "figcaption itemprop" in soup_line:
                    for child in soup_line:
                        if "<p>" in child:
                            outfile.write(child)
                outfile.write("\n")
    infile.close()
    outfile.close()

def readFileHPO(file_name):
    infile = open(file_name)
    outfile = open("multi,model_data", "a")
    for line in infile:
        if "url" in line:
            url = line[7:-1]  # characters 7 through second to last, since there is a comma at the end
            outfile.write(line)  # unsure about this
            page_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(page_content)
            for soup_line in soup:
                if "figcaption class" in soup_line:
                    outfile.write(soup_line)
    infile.close()
    outfile.close()
    
def readFileFOX(file_name):
    infile = open(file_name)
    outfile = open("multi,model_data", "a")
    for line in infile:
        if "url" in line:
            url = line[7:-1]  # characters 7 through second to last, since there is a comma at the end
            outfile.write(line)  # unsure about this
            page_content = urllib.request.urlopen(url)
            soup = BeautifulSoup(page_content)
            for soup_line in soup:
                if "caption" in soup_line:
                    for child in soup_line:
                        if "<p" in child:
                            outfile.write(child)
                        elif "<a" in child:
                            outfile.write(child)
    infile.close()
    outfile.close()
    
    
def get_website(filename: str):
    return filename.split(".")[0].split("_")[1].upper()

def main():
    for file in os.listdir("./emnlp19_BASIL/data"):
        website = get_website(file)
        if website == "NYT":
            readFileNYT(file)
        elif website == "HPO":
            readFileHPO(file)
        elif website == "FOX":
            readFileFOX(file)


main()