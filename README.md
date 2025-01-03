# KuCoin Real-time Price Tracker

This script fetches and displays the current price of a trading pair from the KuCoin API in real-time. It is designed to run in the terminal and updates the price information every few seconds.
Features
```
    Fetches real-time price data from the KuCoin API.
    Displays price, size, and current time.
    Updates price information every 2 seconds.
    Includes error handling for API requests.
    Enhances terminal output with colors and styles for better readability.
```
Prerequisites
```
    Python 3.6 or higher
    requests library
    colorama library
    termcolor library
```
You can install the required libraries using pip:
```
pip install requests colorama termcolor
```
Usage

    Clone the repository:
```
git clone
cd
```
    Run the script:
```
python kucoin_price_tracker.py
```
    Enter the trading pair:

When prompted, enter the trading pair you want to track (e.g., BTC-USDT).
```
    View real-time price updates:
```
The script will continuously fetch and display the price information every 2 seconds. Press Ctrl+C to stop the tracker.
Project Structure
```
kucoin-price-tracker/
│
├── kucoin_price_tracker.py # Main script file
├── requirements.txt # Python dependencies
├── LICENSE # License file
└── README.md # This file
```
Installation

    Create a virtual environment (optional but recommended):
```python
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
    Install dependencies:
```
pip install -r requirements.txt
```

Author

    s3nh - Initial work - GitHub Profile

Created: 2025-01-03 21:16:29 UTC
License

This project is licensed under the WTFPL License - see the LICENSE file for details.
Acknowledgements
```
    KuCoin API Documentation
    Colorama - Terminal text colors
    Termcolor - ANSI color formatting
```
Support

For support, please create an issue in the GitHub repository or contact the maintainer.
Disclaimer

This script is for educational and informational purposes only. Use at your own risk. The author is not responsible for any financial losses incurred while using this script.
Future Improvements
```
    Add support for multiple trading pairs simultaneously
    Implement historical price data visualization
    Add price alerts and notifications
    Include more detailed market information
    Add configuration file support
    Implement logging functionality
```
