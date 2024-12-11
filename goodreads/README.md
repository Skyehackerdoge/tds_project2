# Goodreads Dataset Analysis

## Overview
This analysis explores the Goodreads dataset, focusing on book-related data such as IDs, ratings, and publication years. The dataset reveals fascinating insights into book popularity, user preferences, and rating distributions.

## Data
The dataset contains information about:
- `book_id`, `best_book_id`, `work_id`: Unique identifiers for books.
- `books_count`: Number of copies or editions available.
- `ratings_count` and `average_rating`: User feedback metrics.
- `original_publication_year`: Year of first publication.
- `isbn13`: Book identification numbers.

## Analysis
We conducted the following:
1. **Distribution Analysis**:
   - Analyzed the frequency of `book_id`, `ratings_count`, and `average_rating`.
   - Visualized the distribution of `original_publication_year` to identify trends over time.

2. **Correlation Heatmap**:
   - Evaluated relationships between variables such as ratings, counts, and publication year.
   - Discovered strong positive correlations between higher ratings and the number of ratings.

## Insights
- Most books are published recently, showing an exponential growth in publication trends.
- Ratings are generally clustered around 4.0, indicating a tendency for readers to rate books positively.
- `ratings_count` distribution shows only a few books have high visibility or popularity.
- Strong correlations between rating categories (`ratings_4`, `ratings_5`) and `average_rating`.

## Implications
- Publishers can focus marketing efforts on newer publications and highly-rated books to increase user engagement.
- Recommendation systems should prioritize books with high ratings and numerous user reviews.
- Further cleaning of outlier `original_publication_year` data can improve historical analyses.

## Visualizations
### Distribution of Ratings Count
![ratings_count_distribution](https://github.com/user-attachments/assets/48055d1c-2e91-489f-8f14-bf578d196c1d)
Skewed Popularity: Most books have low ratings counts, while a small number of popular books dominate the higher end.

Visibility Challenge: Authors and publishers should focus on strategies to boost engagement for lesser-known books.

Recommendation Optimization: Recommendation systems should address the skewed distribution to provide diverse suggestions, not just bestsellers.



![average_rating_distribution](https://github.com/user-attachments/assets/32bf6e8c-abad-40a1-beb1-2953fed557b9)


Normal Distribution: The average ratings follow a bell-curve pattern, with most books clustered around a rating of 4.0.

Positive Bias: The skew toward higher ratings suggests that users tend to rate books favorably, with few books rated below 3.5.

Implications for Decision-Making: High average ratings alone may not differentiate books effectively, requiring additional factors like ratings count or reviews for more precise recommendations.



![correlation_heatmap](https://github.com/user-attachments/assets/27707b8d-a6da-4c2f-8828-9430e2361f2c)


Strong Positive Correlations: High correlations are observed among ratings_4, ratings_5, and average_rating, indicating that higher ratings strongly influence the overall average rating.

Weak Relationships: Variables like isbn13 and publication_year show minimal correlation with most other features, suggesting they are not critical factors in determining book popularity or ratings.

Actionable Insights: Focus on metrics like ratings_count and average_rating for predicting a book’s success, as they show significant relationships with overall user engagement.
