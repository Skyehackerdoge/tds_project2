import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
import json
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import zscore

# AI Proxy details
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIxZjMwMDIwOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.L6vVLu2KA5m0RglcGDmTNyj_0k1PEeTRoBcQynJykCc"

def query_llm(prompt):
    """Query the LLM using AI Proxy."""
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a data analyst. Provide insights based on the provided dataset summary."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error querying the LLM: {e}")
        return "Unable to retrieve insights from the LLM due to an error."

def detect_outliers(df):
    """Detect outliers using z-scores."""
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    outliers = {}
    for col in numeric_cols:
        z_scores = zscore(df[col].dropna())
        z_scores = pd.Series(z_scores, index=df[col].dropna().index)
        outliers[col] = df.loc[z_scores[np.abs(z_scores) > 3].index]
    return outliers

def perform_clustering(df):
    """Perform k-means clustering on numerical data."""
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    if len(numeric_cols.columns) < 2:
        return None  # Clustering requires at least 2 features

    numeric_data = numeric_cols.dropna()
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(numeric_data)

    # Create a cluster column with NaN for rows with missing values
    df['Cluster'] = np.nan
    df.loc[numeric_data.index, 'Cluster'] = clusters

    return df, kmeans.cluster_centers_

def feature_importance(df, target_col):
    """Identify feature importance using a random forest regressor."""
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).drop(columns=[target_col], errors='ignore')
    target = df[target_col]
    if numeric_cols.empty or target.isnull().all():
        return None

    model = RandomForestRegressor(random_state=42)
    model.fit(numeric_cols.fillna(0), target.fillna(0))
    importance = pd.Series(model.feature_importances_, index=numeric_cols.columns)
    return importance.sort_values(ascending=False)

def create_visualizations(df):
    """Generate visualizations from the dataset and save as PNG."""
    correlation_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("correlation_heatmap.png")
    plt.close()

    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"{col}_distribution.png")
        plt.close()

def generate_readme(summary_stats, missing_values, llm_response, df):
    """Generate a README.md file with the analysis results."""
    llm_response = llm_response or "No insights could be retrieved from the LLM due to an error."

    with open("README.md", "w") as f:
        f.write("# Automated Data Analysis Report\n\n")
        f.write("## Dataset Summary\n")
        f.write(summary_stats.to_markdown() + "\n\n")
        f.write("## Missing Values\n")
        f.write(missing_values.to_markdown() + "\n\n")
        f.write("## Insights\n")
        f.write(llm_response + "\n\n")
        f.write("## Visualizations\n")
        f.write("![Correlation Heatmap](correlation_heatmap.png)\n")
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            f.write(f"![Distribution of {col}]({col}_distribution.png)\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python autolysis.py <dataset.csv>")
        return

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Error: File {filename} not found.")
        return

    try:
        # Load the dataset
        df = pd.read_csv(filename, encoding="ISO-8859-1")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return

    if df is None or df.empty:
        print("The dataset is empty or could not be loaded.")
        return

    # Perform generic analysis
    summary_stats = df.describe(include='all')
    missing_values = df.isnull().sum()

    # Detect outliers
    outliers = detect_outliers(df)

    # Perform clustering
    clustering_result = perform_clustering(df)
    if clustering_result:
        clustered_df, cluster_centers = clustering_result
    else:
        print("Clustering could not be performed due to insufficient data.")

    # Query LLM for insights
    column_info = {col: str(dtype) for col, dtype in df.dtypes.items()}
    prompt = f"""
    Analyze this dataset with the following column information:
    {json.dumps(column_info, indent=2)}

    Summary statistics:
    {summary_stats.to_string()}

    Missing values:
    {missing_values.to_string()}

    Outliers detected:
    {outliers}
    """
    llm_response = query_llm(prompt)

    # Create visualizations and generate README
    create_visualizations(df)
    generate_readme(summary_stats, missing_values, llm_response, df)
    print("Analysis complete. Results saved in README.md and visualization PNG files.")

if __name__ == "__main__":
    main()
