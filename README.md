# Stock Analysis Dashboard

> This is the task-1 implementation of the stock analysis project.

This project provides a Python-based stock analysis tool that visualizes stock data using various technical indicators.

## Features

- Loads historical stock data from CSV
- Calculates technical indicators:
  - Simple Moving Averages (SMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Generates visualizations of stock data and indicators

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Eyob1061/task-1.git
   cd task-1
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your stock data in a CSV file named `AAPL_historical_data.csv` in the project root.
2. Run the analysis script:
   ```bash
   python analysis.py
   ```
3. View the generated plots in the `plots` directory.

## Project Structure

- `analysis.py` - Main analysis script
- `requirements.txt` - Python dependencies
- `plots/` - Directory containing generated visualizations

## Branches

- `main` - Production-ready code
- `task-1` - Initial implementation
- `task-2` - Dashboard development (in progress)

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

This project is licensed under the MIT License.
