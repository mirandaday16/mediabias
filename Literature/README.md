## Literature Notes:

- Fan et. al., [In Plain Sight: Media Bias through the Lens of Factual Reporting](https://arxiv.org/pdf/1909.02670.pdf), 2019
    - Precursor paper written by this lab
    - Source of our initial [dataset](../Data/JSON_files/emnlp19_BASIL/)
---
    
- Hamborg et. al., [Automated identification of media bias in news articles: an interdisciplinary literature review](https://link.springer.com/content/pdf/10.1007%2Fs00799-018-0261-y.pdf), 2019
    - "Yet, established [news aggregation] systems currently provide no support for showing the different perspectives contained in articles reporting on the same news event." p. 392
    - Section 2: types of media bias
        - [Williams](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1460-2466.1975.tb00656.x) framework:
            - Bias must be both _intentional_ and _sustained_
            - This article focuses on intentional media bias
        - [Mullainathan and Shleifer](https://www.nber.org/papers/w9295.pdf) framework:
            1. ideology
            2. spin
        - [D'Alessio and Allen](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1460-2466.2000.tb02866.x) framework:
            1. coverage
            2. gatekeeping
            3. statement
    - Effects of media bias on consumer percetion:
        1. priming
        2. agenda-setting
        3. framing
    - Multi-modal bias (photos and videos) is introduced in the third step (Editing) of the spin process, and includes both **picture selection** and **picture explanation**
    - Section 3.6: Picture Selection
        - Cites [Rosenberg et. al.](https://www.jstor.org/stable/2111296?seq=1#metadata_info_tab_contents)
            - "Pictures contained in news articles strongly influence how readers perceive a reported topic. In particular, readers who wish to get an overview of current events are likely to browse many articles and thus only view each article's headline and image." Hamborg et. al. p. 405
        - Important to know if a picture is used out-of-context
        - Two types of picture selection analysis:
            - **Person-oriented**: 
                - typical rating dimensions:
                    - Expression
                    - Activity
                    - Interaction
                    - Background
                    - Camera angle
                    - Body posture
            - **Topic-oriented**: see p. 405-406 for example
        - "To our knowledge, there are currently no systems or approaches from computer science that analyze media bias through image selection. However, methods in _computer vision_ can measure some of the previously described dimensions." Hamborg et. al. p. 406
    - Section 3.7: Picture Explanation
        - Includes example of "looting" vs. "finding" food during Hurrican Katrina
            - Cites [Sommers et. al.](https://spssi.onlinelibrary.wiley.com/doi/full/10.1111/j.1530-2415.2006.00103.x)
        - Types of analysis in social sciences:
            1. jointly analyzing image and caption
            2. Analyzing caption alone, ignoring image (much more common)
                - Mentioned in Sections 3.3 (Commission and Omission) and 3.4 (Labeling and Word Choice)
        - "We found that most studies in the social sciences either analyze image captions as a component of the main text, or analyze images but disregard their captions entirely." Hamborg et. al., p. 406
        - "The few analyses on captions suggest that bias by picture explanation is not very common. However, more fundamental studies show strong impact of captions on the perception of images and note rather subtle differences in word choice. While many studiess= analyzed captions as part of the regular text, e.g., analyzing bias by labeling and word choice, research currently lacks specialized analyses that examine captions in conjunction with their images." Hamborg et. al., p. 406
