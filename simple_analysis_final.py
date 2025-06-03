"""
Simple Stock News Sentiment Analysis
-----------------------------------
A minimal implementation for analyzing stock and news data.
"""

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from scipy import stats
import os

def load_stock_data():
    """Load and process stock data."""
    try:
        df = pd.read_csv('AAPL_historical_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date').sort_index()
        df['returns'] = df['Close'].pct_change() * 100
        return df
    except Exception as e:
        print(f"Error loading stock data: {e}")
        return None

def load_news_data():
    """Load and process news data."""
    try:
        df = pd.read_csv('sample_news_data.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df.set_index('date').sort_index()
    except Exception as e:
        print(f"Error loading news data: {e}")
        return None

def analyze_sentiment(text):
    """Basic sentiment analysis."""
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0.0

def main():
    print("\n=== Stock & News Analysis ===\n")
    
    # Load data
    print("Loading data...")
    stock_df = load_stock_data()
    news_df = load_news_data()
    
    if stock_df is None or news_df is None:
        print("Error: Could not load required data files.")
        return
    
    # Analyze sentiment
    print("Analyzing news sentiment...")
    news_df['sentiment'] = news_df['headline'].apply(analyze_sentiment)
    
    # Get daily average sentiment
    daily_sentiment = news_df['sentiment'].resample('D').mean()
    
    # Merge with stock returns
    merged = pd.merge(
        stock_df[['returns']],
        daily_sentiment,
        left_index=True,
        right_index=True,
        how='inner'
    )
    
    if len(merged) < 2:
        print("Error: Not enough data points for analysis.")
        return
    
    # Calculate correlation
    corr, p_value = stats.pearsonr(merged['returns'].dropna(), 
                                 merged['sentiment'].dropna())
    
    # Print results
    print("\n=== Results ===")
    print(f"Analysis Period: {merged.index.min().date()} to {merged.index.max().date()}")
    print(f"Trading Days: {len(merged)}")
    print(f"Correlation: {corr:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    # Simple interpretation
    if abs(corr) > 0.5:
        strength = "Strong"
    elif abs(corr) > 0.3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    direction = "positive" if corr > 0 else "negative"
    sig = "significant" if p_value < 0.05 else "not significant"
    
    print(f"\n{strength} {direction} correlation ({sig}).")
    
    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(merged.index, merged['returns'], 'b-', label='Stock Returns')
    plt.scatter(merged.index, merged['sentiment'] * 10, color='red', label='Sentiment (x10)')
    
    # Add headlines
    for date, row in news_df.iterrows():
        if date in merged.index:
            plt.annotate(
                row['headline'][:10] + '...',
                (date, merged.loc[date, 'sentiment'] * 10),
                rotation=45,
                fontsize=8,
                alpha=0.7
            )
    
    plt.title('Stock Returns vs News Sentiment')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save plot
    os.makedirs('plots', exist_ok=True)
    plot_path = os.path.join('plots', 'simple_analysis.png')
    plt.savefig(plot_path, dpi=150)
    
    print(f"\nPlot saved to: {os.path.abspath(plot_path)}")

if __name__ == "__main__":
    main()
