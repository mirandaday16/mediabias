###  Mid-Week Updates: Tuesday, January 21, 2020

- Purchased NYT student subscription (first 4 weeks free, then talk to Lu about reimbursement)
- Updated crawler to capture alt text and captions from NYT articles, and media type/link for all articles
- Updated metadata file with latest crawl

To do:
- Decide on a method of storing/displaying data more efficiently
- Begin thinking about guidelines for annotating data manually (notes about potential bias)

---
### Mid-Week Updates: Wednesday, January 22, 2020

- Possible replacement for HuffPost: The Atlantic (more center-left compared to HuffPo and NYT, media seems to have alt text/caption/both based on cursory search).
    - Related: rating of overall bias of online news outlets: https://www.allsides.com/media-bias/media-bias-ratings
- Created updated .txt and .csv files containing article media metadata. .csv file will be especially useful in visualization/comparison. Can possibly also be expanded to include annotation notes.
    - Note: The articles in both files are now sorted by file name, so articles on the same topic will be next to each other
- Reorganized repo to be more easily navigable

---
### Mid-Week Updates: Thursday, January 23, 2020

- Created a script which writes a spreadsheet (.csv file) that can be used to help find relevant aligned articles from another news source(s), such as The Atlantic
- Finished reading Hamborg article, made some notes and highlighted most important sections (see [Literature notes](../Literature/README.md) )
- Currently thinking about best ways to **quantify**, or at least accurately compare, bias in photos and videos

---
### Mid-Week Updates: Wednesday, January 29, 2020

- Manually fixed URLs and gathered metadata for "HTTP Error" articles
- Manually double-checked and fixed Caucus article metadata and articles labelled as "no media", and fixed erroneous media links
- Wrote script to create .csv file for comparing main figures in captions vs their articles (using data from json files)

To do:
- Manually fill in caption main entities and match rate
- Compare caption main entities to media main entities
- Other caption analysis: detailed/not, subjective/not (read Jurafsky for this)

---
### Mid-Week Updates: Thursday, January 30, 2020

- Manually filled in caption main entities, match rate, and other entity data ([spreadsheet here](../Data/processed_data/caption_main_figures_edited.csv))
- Created separate folders for main entity analysis in [Scripts](../Scripts/Main_Entities/) and [Data](../Data/processed_data/Main_Entities/)
- Analyzed and plotted the match rate of main entities in captions v. their articles, [comparing NYT to FOX](../Data/processed_data/Main_Entities/README.md)
- Analyzed and plotted the average number of additional entities in captions v. main entities of their articles, [comparing NYT to FOX](../Data/processed_data/Main_Entities/README.md)
- Added dedicated section for current hypotheses [here](../Data/processed_data/README.md)
- Created file for comparing general attributes of captions (relevance to media, level of detail, subjectiveness)

---
### Mid-Week Updates: Sunday, February 2, 2020

- Manually filled in automatically-created spreadsheet rating captions for relevance to media, level of detail, and subjectiveness
- Read Ch. 21 of Jurafsky textbook ([Lexicons for Sentiment, Affect, and Connotation](https://web.stanford.edu/~jurafsky/slp3/21.pdf))
    - Downloaded info on [MPQA Subjectivity lexicon](../Literature/MPQA_Subjectivity_Lexicon) to explore options for austomatic subjectivity analysis of caption
