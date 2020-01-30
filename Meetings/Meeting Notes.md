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
    - Regarding the above, I wrote a script to produce a [.csv spreadsheet](../Data/processed_data/article_topics_edited.csv) to track the article topics and dates in the initial FOX and NYT articles, which will help me to search for appropriate articles in the Atlantic (or another/more source(s) in the future)
    
Post-meeting ACTION ITEMS:
- [x] Manually find metadata for HTTP Error articles
- [x] Manually double-check Caucus links
- [ ] Manually check "No Media" articles and make sure they really don't have media
- [ ] Does caption/media contain main figures? Compare to json files. If not, why? (edit by Lu: for each caption, we should also label all the entities mentioned in it, then compare with the main figures in article.)
- [ ] Check whether captions reflect the content in the multimedia (added by Lu: I think we discussed this too?)
- [ ] How many captions are detailed/not?
- [ ] Check out Marshall's annotation tool -- email him if you can't find
- [ ] Annotate captions as subjective or not. Refer to Jurafsky's textbook for guidelines on subjectivity (Chapter 21). Label using binary.
- [ ] Write down hypotheses/thoughts somewhere specific in repo.


Questions:
- Does the caption correctly reflect the content? Are there opinions inserted into the caption?
- Which is more helpful: alt text or caption? What is the difference? When there is a difference, why? Is alt text more objective?
