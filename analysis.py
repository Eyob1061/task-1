import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator
from ta.trend import MACD
import os

# Create a directory for plots if it doesn't exist
os.makedirs('plots', exist_ok=True)

# Use a simple style
plt.style.use('default')
plt.rcParams['figure.figsize'] = (14, 7)

# Load data
data = pd.read_csv('AAPL_historical_data.csv')

# Display the first few rows
print(data.head())

# Check for NaN values
if data['Close'].isnull().any():
    data['Close'].fillna(method='ffill', inplace=True)  # Forward fill

# Calculate Moving Averages
sma_200 = SMAIndicator(close=data['Close'], window=200)
data['SMA_200'] = sma_200.sma_indicator()

# Add 50-day SMA for the plot
sma_50 = SMAIndicator(close=data['Close'], window=50)
data['SMA_50'] = sma_50.sma_indicator()

# Calculate RSI
rsi = RSIIndicator(close=data['Close'], window=14)
data['RSI'] = rsi.rsi()

# Calculate MACD
macd = MACD(close=data['Close'])
data['MACD'] = macd.macd()
data['MACD_signal'] = macd.macd_signal()

# Plot 1: Stock Price and Moving Averages
plt.figure()
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['SMA_50'], label='50-Day SMA', color='red')
plt.plot(data['SMA_200'], label='200-Day SMA', color='green')
plt.title('Stock Price and Moving Averages')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/stock_price_ma.png')
print("Saved plot: plots/stock_price_ma.png")
plt.close()

# Plot 2: RSI
plt.figure(figsize=(14, 5))
plt.plot(data['RSI'], label='RSI', color='purple')
plt.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought (70)')
plt.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold (30)')
plt.title('Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/rsi.png')
print("Saved plot: plots/rsi.png")
plt.close()

# Plot 3: MACD
plt.figure(figsize=(14, 5))
plt.plot(data['MACD'], label='MACD', color='blue')
plt.plot(data['MACD_signal'], label='Signal Line', color='red')
plt.title('Moving Average Convergence Divergence (MACD)')
plt.xlabel('Date')
plt.ylabel('MACD Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/macd.png')
print("Saved plot: plots/macd.png")
plt.close()

print("\nAll plots have been saved to the 'plots' directory.")
print("You can find the following files:")
print("- plots/stock_price_ma.png")
print("- plots/rsi.png")
print("- plots/macd.png")