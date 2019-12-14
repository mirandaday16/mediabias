import soup as soup
from bs4 import BeautifulSoup
import urllib.request
import emnlp19_BASIL


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
    
    
def main():
    for file in emnlp19_BASIL.data:
        if file[3,5].upper() == "NYT":
            readFileNYT(file)
        elif file[3,5].upper() == "HPO":
            readFileHPO(file)
        elif file[3,5].upper() == "FOX":
            readFileFOX(file)