Happiness Dataset Analysis
Overview
This analysis focuses on global happiness indicators, exploring the factors that contribute to well-being and life satisfaction across countries and years. The dataset provides insights into socio-economic, health, and emotional aspects that influence happiness.

Data Description
The dataset contains the following columns:

Country name: The country where the data was collected.
Year: The year of data collection.
Life Ladder: An overall life satisfaction score on a ladder scale (0 to 10).
Log GDP per capita: The logarithm of GDP per person, reflecting economic status.
Social support: The extent to which individuals feel they can rely on others in times of need.
Healthy life expectancy at birth: The number of years a newborn is expected to live in good health.
Freedom to make life choices: The perceived freedom to choose what one does with their life.
Generosity: A measure of self-reported charitable behavior.
Perceptions of corruption: The level of corruption perceived in the country's government and business sectors (lower is better).
Positive affect: The frequency of positive emotions experienced, such as happiness and laughter.
Negative affect: The frequency of negative emotions experienced, such as sadness or worry.
Analysis
Key steps in the analysis included:

Exploring Distributions:

Visualized the distributions of key indicators like Life Ladder, Log GDP per capita, and Healthy life expectancy.
Identified trends in socio-economic and emotional factors over time.
Correlation Analysis:

Examined relationships between variables to understand what drives happiness.
Identified strong positive correlations between Life Ladder and Log GDP per capita, Social support, and Healthy life expectancy.
Temporal Trends:

Tracked changes in happiness scores over years and identified global patterns.
Insights
Economic and Social Support:
Higher GDP per capita and stronger social support networks strongly correlate with greater life satisfaction.
Health and Happiness:
Healthy life expectancy is a key driver of happiness, reinforcing the importance of access to healthcare.
Emotional Indicators:
Positive affect correlates with higher Life Ladder scores, while negative affect correlates negatively.
Freedom and Corruption:
Perceived freedom to make life choices boosts happiness, whereas high corruption perceptions diminish it.

![Log GDP per capita_distribution](https://github.com/user-attachments/assets/c89ddf39-b4f0-47c6-9805-f3cb736ff5c9)


Distribution of Log GDP per Capita
Bell-shaped Distribution: The distribution is fairly symmetric, with most countries having a Log GDP per capita between 9 and 11, suggesting an even spread among medium to high-income countries.
Fewer Low-Income Countries: There are fewer countries with a Log GDP per capita below 8, indicating that extreme poverty is less common in the dataset.
Implication for Happiness: Higher Log GDP per capita aligns with greater access to resources, contributing positively to life satisfaction.


![Generosity_distribution](https://github.com/user-attachments/assets/ca89b356-533c-4adb-96a1-1dbfc1df41ad)


Distribution of Generosity
Peak Near Zero: The majority of generosity values cluster around 0, meaning that self-reported generosity is relatively neutral for most countries.
Asymmetric Spread: A longer tail toward positive values indicates some countries have a significantly higher sense of generosity.
Implication for Happiness: Positive generosity scores can contribute to a stronger sense of community and well-being, enhancing happiness levels.



  ![Positive affect_distribution](https://github.com/user-attachments/assets/f084754e-5a9c-4760-bb37-8deea5204cdd)

Distribution of Positive Affect
Skewed Toward Higher Values: Most countries report positive affect scores between 0.6 and 0.8, suggesting that experiencing positive emotions like happiness and laughter is common globally.
Few Low Scores: Very few countries report scores below 0.5, indicating that widespread low positive affect is rare.
Implication for Happiness: Higher positive affect strongly correlates with overall life satisfaction and happiness, highlighting the emotional component of well-being.
