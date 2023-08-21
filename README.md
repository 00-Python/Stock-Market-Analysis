# Stock Data Analysis and Plotting Tool

The **Stock Data Analysis and Plotting Tool** is a Python program that allows users to retrieve stock data from different online sources, visualize the data through candlestick and linear plots, and export the data to CSV and Excel files. The tool also provides functionality to explore stock market lists and stock symbol lists. 

## Features

- Retrieve stock data from supported data sources (currently supports Yahoo Finance).
- Visualize stock data using candlestick and linear plots.
- Export stock data to CSV and Excel files for further analysis.
- Explore stock market lists and stock symbol lists.
- User-friendly command-line interface.

## Getting Started

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/00-Python/Stock-Market-Analysis.git
   cd Stock-Market-Analysis
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key for the StockSymbol API from [https://stock-symbol.herokuapp.com/](https://stock-symbol.herokuapp.com/) and save it in `apis/stock_symbol_api.txt`.

4. Run the program:

   ```
   python market.py
   ```

5. Follow the on-screen prompts to select the market, stock symbol, data source, and time frame for the stock data analysis.

6. Choose from various actions such as plotting, exporting data, and exploring market lists.

## Project Structure

The project consists of the following components:

- `market.py`: The main script that interacts with the user and coordinates different functionalities.
- `plotting_system/system.py`: The module containing the `Trading_plotter` class for plotting and exporting stock data.
- `apis/stock_symbol_api.txt`: API key for the StockSymbol API (replace with your own API key).

## Usage

The **Stock Data Analysis and Plotting Tool** offers a range of functionalities to help you analyze and visualize stock data. Here's how to make the most of its features:

### Retrieving Stock Data

1. Run the `market.py` script by executing the following command:

   ```
   python market.py
   ```

2. Follow the on-screen prompts to select the market, stock symbol, data source, and time frame for the stock data analysis.

### Plotting Stock Data

1. After retrieving stock data, you'll be presented with a menu. Choose the option to "Plot Stock Data."

2. Select the type of plot you want to create:
   - **Candlestick Plot:** Visualizes stock price movements using candlestick charts.
   - **Linear Plot:** Plots stock price data in a line chart.

3. The plot will be displayed in a new window. You can interact with the plot, zoom in/out, and save it as an image (if using a GUI).

### Exporting Stock Data

1. Once you have retrieved stock data, you can export it for further analysis.

2. Choose the "Export Stock Data" option from the main menu.

3. Select the export format:
   - **CSV:** Export the stock data to a CSV file for use in spreadsheet software.
   - **Excel:** Export the stock data to an Excel (xlsx) file.

## Contributing

Contributions are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
