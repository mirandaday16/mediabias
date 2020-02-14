# Adds unique article IDs to each article for better ease of comparison
# To be implemented in CSV_Creator.py, which creates metadata.csv


# Returns unique article ID using website name and alignment number
def get_article_id(filename: str, website):
    if filename[1] == "_":
        article_id = ("0" + filename[0]) + website
    else:
        article_id = (filename.split('_')[0] + website)
    return article_id
