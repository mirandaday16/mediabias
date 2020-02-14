## Entity Analyses

### Average Caption-to-Article Entity Match, by Website
![Average Entity Match Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/avg_match_rate.png | width=200)

This figure shows the average number of main entities **from the article** that appear in the caption, separated by news outlet. We can see that NYT captions tend to be somewhat more thorough in mentioning main entities (65%) than FOX captions (52%). Note that these percentages only include articles which contain media **with captions**.

Calculation for each article: Match Rate = ((All Caption Entities) - (Caption Entities Which Are NOT Article Main Entities)) / (# of Article Main Entities)

Calculation for website average: (Sum of all match rates for articles from that site) / (# of articles considered)

**NOTE**: Because only articles with captions are considered, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Main_Entities/caption_entity_analysis.py)

---

### Average Number of Non-Main Entities in Captions, by Website
![Extra Entity Avg Plot](https://github.com/mirandaday16/mediabias/blob/master/Data/processed_data/Main_Entities/extra_entities_rate.png | width=200)

This figure shows the average number of named entities in captions that are **NOT** main entities in the article. **This does not account for journalist or photographer names/credits that may appear in captions.** As you can see, the rates are fairly similar (0.53 entities for NYT captions vs. 0.56 entities for FOX captions). As above, note that these percentages only include articles which contain media **with captions**.

Calculation for each article: Extra Entity Rate = ((All Caption Entities) - (Caption Entities Which ARE Article Main Entities)) / (# of Article Main Entities)

Calculation for website average: ((Sum of all extra entity rates for articles from that site) - (# of journalist names occurring in each caption)) / (# of articles considered)

**NOTE**: As above, the # of NYT articles and the # of FOX articles considered are not equal. 85 FOX and 73 NYT articles are considered in this calculation.

Based on this [spreadsheet](caption_main_figures_edited.csv)

[Script](https://github.com/mirandaday16/mediabias/blob/master/Scripts/Main_Entities/caption_entity_analysis.py)
