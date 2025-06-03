# Task 3: News Sentiment and Stock Movement Correlation

This task analyzes the correlation between news sentiment and stock price movements for Apple Inc. (AAPL).

## Features

- **Sentiment Analysis**: Uses TextBlob to analyze sentiment in news headlines
- **Stock Data Processing**: Processes historical stock price data
- **Correlation Analysis**: Calculates Pearson correlation between sentiment scores and stock returns
- **Visualization**: Generates plots showing the relationship between sentiment and stock movements

## Setup

1. Ensure you have Python 3.8+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Download NLTK data (run Python and execute):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```

## Files

- `sentiment_analysis.py`: Main script for sentiment analysis and correlation
- `sample_news_data.csv`: Sample news headlines with dates
- `AAPL_historical_data.csv`: Historical stock price data
- `plots/sentiment_correlation.png`: Generated visualization

## Usage

Run the analysis:
```
python sentiment_analysis.py
```

## Results

The analysis will output:
- Correlation coefficient between news sentiment and stock returns
- P-value of the correlation
- A visualization saved as `plots/sentiment_correlation.png`

## Interpretation

- **Correlation Coefficient**: Ranges from -1 to 1
  - 1: Perfect positive correlation
  - 0: No correlation
  - -1: Perfect negative correlation
- **P-value**: Indicates statistical significance (typically < 0.05 is considered significant)

## Next Steps

- Expand news dataset for more robust analysis
- Implement more sophisticated sentiment analysis models
- Add additional technical indicators for comparison
