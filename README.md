# tds_project2
# Autolysis: Automated Data Analysis Framework

## Overview
Autolysis is an automated data analysis framework that processes any valid CSV file to generate meaningful insights, visualizations, and a detailed Markdown report. Designed to be flexible and efficient, the script performs a wide range of analyses, including detecting outliers, clustering, correlation analysis, and more.

The tool also integrates with a language model (LLM) to provide narrative insights based on the dataset, making it highly adaptable for various datasets like books, happiness metrics, and media.

---

## Features
1. **Automated Analysis**:
   - Generates summary statistics for the dataset.
   - Detects missing values and highlights areas for improvement.
   - Identifies outliers using statistical methods (Z-scores).

2. **Machine Learning Techniques**:
   - Clustering using K-means to group data naturally.
   - Feature importance using Random Forest to identify key predictors (optional).

3. **Data Visualization**:
   - Creates a correlation heatmap to explore relationships between variables.
   - Generates distribution plots for all numeric columns.

4. **AI-Powered Insights**:
   - Queries a language model (LLM) to provide high-level insights, interpret findings, and suggest actionable recommendations.

5. **Customizable Output**:
   - Saves analysis results in a `README.md` file.
   - Outputs visualizations in `.png` format for easy embedding.

---

## Directory Structure
The output files are organized as follows:

Key Analytical Capabilities
Outlier Detection: Highlights anomalies that may represent data errors or high-impact opportunities.
Correlation Analysis: Identifies strong relationships between variables.
Clustering: Groups data for targeted insights or segmentation.
LLM Integration: Provides human-readable narratives to enhance analysis.



Supported Datasets
Goodreads: Analyzes book-related data (ratings, reviews, publication years, etc.).
Happiness: Evaluates global happiness metrics (GDP, life expectancy, emotional well-being).
Media: Explores content performance metrics (engagement, repeatability, quality).


Requirements
Python 3.7+
Required libraries: pandas, numpy, matplotlib, seaborn, requests, scikit-learn.

License
This project is licensed under the MIT License.




