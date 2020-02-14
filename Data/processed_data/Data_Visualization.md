## Entity Analyses

### Average Caption-to-Article Entity Match, by Website
![Average Entity Match Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/avg_match_rate.png)

This figure shows the average number of main entities **from the article** that appear in the caption, separated by news outlet. We can see that NYT captions tend to be somewhat more thorough in mentioning main entities (65%) than FOX captions (52%). Note that these percentages only include articles which contain media **with captions**.

Calculation for each article: Match Rate = ((All Caption Entities) - (Caption Entities Which Are NOT Article Main Entities)) / (# of Article Main Entities)

Calculation for website average: (Sum of all match rates for articles from that site) / (# of articles considered)

**NOTE**: Because only articles with captions are considered, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Main_Entities/caption_entity_analysis.py)

---

### Average Number of Non-Main Entities in Captions, by Website (Excluding Journalists)
![Extra Entity Avg Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/extra_entities_rate.png)

This figure shows the average number of named entities in captions that are **NOT** main entities in the article. **This does not account for journalist or photographer names/credits that may appear in captions.** As you can see, the rates are fairly similar (0.53 entities for NYT captions vs. 0.56 entities for FOX captions). As above, note that these percentages only include articles which contain media **with captions**.

Calculation for each article: Extra Entity Rate = ((All Caption Entities) - (Caption Entities Which ARE Article Main Entities)) / (# of Article Main Entities)

Calculation for website average: ((Sum of all extra entity rates for articles from that site) - (# of journalist names occurring in each caption)) / (# of articles considered)

**NOTE**: As above, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Main_Entities/caption_entity_analysis.py)

---

### Average Number of Non-Main Entities in Captions, by Website (Including Journalists)
![Extra Entity Plot w Journalists](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/extra_entities_rate_with_journalists.png)

This figure shows the average number of named entities in captions that are **NOT** main entities in the article. **This DOES INCLUDE journalist or photographer names/credits that appear in captions.** As you can see, the disparity between FOX and NYT rates increases sharply compared to the previous graph (an average of 0.55 extra entities in NYT captions -- similar to the rate not including journalist names -- compared to an average of 0.79 extra entities in FOX articles). **This shows that FOX articles are more likely to use their captions as a space for crediting photographers/journalists involved in creation if the media and/or article**. The implications of this finding are unclear. As above, note that these percentages only include articles which contain media **with captions**.

Calculation for each article: Extra Entity Rate = ((All Caption Entities) - (Caption Entities Which ARE Article Main Entities)) / (# of Article Main Entities)

Calculation for website average: (Sum of all extra entity rates for articles from that site) / (# of articles considered)

**NOTE**: As above, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Main_Entities/caption_entity_analysis.py)

---
### Average Word Count in Captions, by Website
![Word Count Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Word_Counts/basic_word_counts.png)

This figure shows the average number of words in captions for articles on each website. As you can see, the rates are fairly similar (19.4 words for NYT captions vs. 19.0 words for FOX captions). As above, note that these percentages only include articles which contain media **with captions**.

Calculation for each article: (# of tokens in caption after NLTK tokenization) - (# of punctuation tokens)

Calculation for website average: (Sum of all caption lengths) / (# of articles considered)

**NOTE**: As above, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Word_Counts/word_count_analysis.py)

---
### Average Word Count in Captions, by Website (not including Entity Names)
![Word Count No Names Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Word_Counts/word_counts_without_entities.png)

This figure shows the average number of words in captions for articles on each website. **This DOES INCLUDE journalist or photographer names or other entity names** (based on manual annotation of caption entities in the spreadsheet linked below). As you can see, the rates are fairly similar (14.6 words for NYT captions vs. 14.3 for FOX captions). **This shows that there is not a significant difference in the amount of entity names included in each website's captions, on average**. As above, note that these percentages only include articles which contain media **with captions**.

Calculation for each article: (# of tokens in caption after NLTK tokenization) - (# of punctuation tokens) - (# of tokens in all entity names in caption)

Calculation for website average: (Sum of all caption lengths) / (# of articles considered)

**NOTE**: As above, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Word_Counts/word_count_analysis.py)
