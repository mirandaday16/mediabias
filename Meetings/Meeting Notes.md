## Weekly Meeting Notes

### Friday, January 17, 2020

Progress so far:
- wrote program to get caption/alt text information for photo/video media (works for Fox News)
- began literature review, gathering papers based on recommendations from Eva and Ian/Xinyu (current focus)

Currently:
- reading literature related to media bias, multi-modal deception detection, and journalistic practices
- attempting to narrow the scope of the project and determine next steps
Potential issues to discuss:
- How well does caption/alt text really describe the content of a photo video? I am hesitant to use caption text in order to analyze the bias of photos.
- Need for manual labelling?
- Computer vision?

Post-meeting ACTION ITEMS:
- [x] Gather alt-text and captions for NYT sources
- [x] Consider replacement sources for HuffPost (does not have captions)
- [x] Consider how to store data: website, article title, type of media, link to media, caption text, alt-text, notes about potential bias (see Hamborg paper)
- [x] Pause literary review for now (but read Hamborg paper this week)

---

### Friday, January 24, 2020

Progress this past week:
- Crawled for and collected the following metadata from FOX and NYT sources: headline, url, media type, media link, alt text, and caption
    - Note that not all articles contain photo/video media, and not all media have both alt text and a caption. NYT especially does not seem to use alt text, but they use captions consistently
    - Created scripts to produce metadata files: [.txt](../Data/processed_data/metadata.txt) and [.csv](../Data/processed_data/metadata.csv)
- Read Hamborg paper recommended by Lu and left key takeaways in [Literature Notes](../Literature/README.md)
    - Next step: consider ways to **quantitatively compare** bias in media across aligned articles
- Brainstormed replacement news outlets for HuffPost. I checked The Atlantic, which skews more center-left than HPO and NYT, and they seem to use alt-text and/or captions fairly consistently.
    - Next step: find articles aligned by topic with those from FOX and NYT in the initial dataset
    - Regarding the above, I wrote a script to produce a [.csv spreadsheet](../Data/processed_data/Article_Topics/article_topics_edited.csv) to track the article topics and dates in the initial FOX and NYT articles, which will help me to search for appropriate articles in the Atlantic (or another/more source(s) in the future)
    
Post-meeting ACTION ITEMS:
- [x] Manually find metadata for HTTP Error articles
- [x] Manually double-check Caucus links
- [x] Manually check "No Media" articles and make sure they really don't have media
- [x] Does caption/media contain main figures? Compare to json files. If not, why? (edit by Lu: for each caption, we should also label all the entities mentioned in it, then compare with the main figures in article.)
- [ ] Check whether captions reflect the content in the multimedia (added by Lu: I think we discussed this too?) (**IN PROGRESS**)
- [ ] How many captions are detailed/not? (**IN PROGRESS**)
- [ ] Check out Marshall's annotation tool -- email him if you can't find
- [ ] Annotate captions as subjective or not. Refer to Jurafsky's textbook for guidelines on subjectivity (Chapter 21). Label using binary. (**IN PROGRESS**)
- [x] Write down hypotheses/thoughts somewhere specific in repo.


Questions:
- Does the caption correctly reflect the content? Are there opinions inserted into the caption?
- Which is more helpful: alt text or caption? What is the difference? When there is a difference, why? Is alt text more objective?

---

### Monday, February 3, 2020

**Progress this past week**:
- Manually fixed all broken links and missing data
- Conducted analysis on main entities of articles (based on json file data) compared to entities in captions.
    - You can see the data plotted [here](../Data/processed_data/Main_Entities/README.md)
- Based on above analysis, added a dedicated section for current hypotheses [here](../Data/processed_data/README.md)
- Created [spreadsheet](../Data/processed_data/Caption_General_Analysis/caption_general_analysis_edited.csv) for comparison of general caption attributes -- relation to media, level of detail, and subjectiveness
    - Manually filled out spreadsheet with my own analyses (**IN PROGRESS**)

**Other Questions**:
- How frequently does each website use video v. photo (v. no media?)
- Are captions which contain more entities than their corresponding media more detailed?
- Should we create a separate data subset of article pairs which BOTH contain media/captions?

**Next steps**:
- Read through subjectivity resources mentioned in Jurafsky, including [MPQA Subjectivity Lexicon](../Literature/MPQA_Subjectivity_Lexicon)
- Assign articles individual IDs in order to more easily update metadata across files
    - standardize correct links/metadata across files (as of right now, [caption_general_analysis_edited.csv](../Data/processed_data/Caption_General_Analysis/caption_general_analysis_edited.csv) has the most up-to-date media links)
- Finish manually annotating caption analysis spreadsheet
- Lu: next step will be to add more data -- possibly use some article's from Ian's dataset?

**ACTION ITEMS**:
- [ ] Look for secondary media (not at the top of articles) and add that information too.
- [ ] Explore other useful lexicons for sentiment analysis (ask Xinyu if you have questions)
    - [ ] Also ask Xinyu about Valence/Arousal/Dominance (see p. 18 in Jurafsky chapter)
- [ ] Harvard
- [x] Clarify how data in matplotlibs was calculated, and make more matplotlibs
- [x] Think about new methods for displaying data
- [x] For analyzing detail: calculate number of words in caption, number of words minus entities, etc.
- [ ] Assign unique article IDs to articles
- [ ] Annotate sentiment towards **entities** in caption (positive or negative), so that we can compare to sentiment on article level later. (**IN PROGRESS**)
- [ ] Find out how many article **pairs** both have caption and media, and let Lu and Shuyang know.
- [ ] Look at ratio of sentiment words in caption (and compare to article) (**IN PROGRESS**)
    - [x] Figure out a good way to display this data
    
---

### Friday, February 14, 2020

**Progress this past week**:
- Clarified [matplotlib](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/README.md) calculations regarding entity matching
- Added new plots and descriptions to matplotlib file (see above)
- Added individual IDs to each article for easier data comparison using [this function](https://github.com/mirandaday16/mediabias/blob/master/Scripts/assigning_article_ids.py). Meant to simplify data comparison.
    - **Note**: Updating all CSV files in progress
- 3 current analysis areas for captions: main entities, word count, and sentiment

**Some thoughts**:
- Possible data display methods: found some suggestions [here](https://mode.com/blog/python-data-visualization-libraries/); interested in trying pygal and Seaborn
    - May try using JSON files instead of .csv going forward (the spreadsheets are becoming unwieldy)

**Next steps**:
- Annotate and analyze sentiment words/sentiment towards entities in captions, and compare to article sentiment/bias (**IN PROGRESS**)
    - Plan to use MPQA Subjectivity Lexicon for sentiment-word tagging
- Add secondary media to dataset (photos/videos not at the top of articles) -- how to incorporate?
- Create list of article **_PAIRS_** which both contain media/captions

**ACTION ITEMS:**
- [ ] Include motivation in matplotlib graphics
- [ ] Create chart of # of captions which mention 0, 1, etc. main entities.
- [ ] Double-check word counts of captions
- [ ] Start talking to Ian/Xinyu about other data sources

---

### Friday, February 20, 2020

**Progress This Week**:
- Updated all files with unique article IDs
- Created a [list](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Caption_General_Analysis/aligned_articles_with_captions.csv) of aligned article pairs which BOTH contain media and caption
    - **Question**: should we compare websites using this set of articles, or all articles which have captions? So far, I have been using the set of all articles containing captions.
- Annotated sentiment:
    - Sentiment words in caption (using MPQA Lexicon)
    - Ratio of sentiment words to caption length
    - Sentiment toward caption entities (manual; positive or negative)
    - Caption sentiment compared to article sentiment (annotated in JSON files)
- Created a chart of # of captions which mention 0, 1, etc. MAIN entities
- Updated matplotlib displays with charts of most important numbers

---
