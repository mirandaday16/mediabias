# Creates three matplotlib visualizations of entity match between captions and articles
import csv
import numpy as np
from matplotlib import pyplot as plt

data_csv_file = "/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/" \
                "Main_Entities/caption_main_figures_edited.csv"


# Returns a dictionary with article headlines as keys and a lit containing website, match rate,
# extra caption entity count, and journalist name count as the values.
def create_data_dict():
    data = {}
    with open(data_csv_file, 'rt')as file:
        open_file = csv.reader(file)
        for row in open_file:
            # Ignore articles without captions
            if row[3] != "NONE" and row[6] != "-":
                data[row[1]] = [row[0], row[6], row[7], row[8]]
    return data


def main():
    data = create_data_dict()
    # Create a matplotlib visualization of entity match rate by website
    fox_matches = 0
    nyt_matches = 0
    fox_count = 0
    nyt_count = 0
    for key in data:
        if data[key][0] == "FOX":
            fox_matches += float(data[key][1])
            fox_count += 1
        elif data[key][0] == "NYT":
            nyt_matches += float(data[key][1])
            nyt_count += 1
    # Get average match rates for each site
    fox_avg = fox_matches / fox_count
    nyt_avg = nyt_matches / nyt_count
    # Format matplotlib
    x_val = [0, 1]
    y_val = [nyt_avg, fox_avg]
    plt.bar(x_val, y_val)
    labels = ["NYT", "FOX"]
    plt.xticks(x_val, labels)
    plt.ylabel("% of main entities from article present in caption")
    y_pos = np.arange(len(x_val))
    plt.yticks(np.arange(0, 1, 0.05))
    plt.title("Average Article Entity Match Rate in Captions")
    plt.bar(y_pos, y_val, color=["blue", "red"])
    for i in range(len(x_val)):
        plt.text(x=x_val[i] - 0.1,
                 y=y_val[i] + 0.005,
                 s=y_val[i],
                 size=8)
    plt.show()
    plt.savefig('/Users/mirandadayadkins/Desktop/Media_Bias/Data/processed_data/Main_Entities/avg_match_rate.png')


    # Create a matplotlib visualization of extra named entities in captions by website

    # Create a matplotlib visualization of extra named entities in captions, excluding journalist names


main()
