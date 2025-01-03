KuCoin Real-time Price Tracker

This script fetches and displays the current price of a trading pair from the KuCoin API in real-time. It is designed to run in the terminal and updates the price information every few seconds.
Features

    Fetches real-time price data from the KuCoin API.
    Displays price, size, and current time.
    Updates price information every 2 seconds.
    Includes error handling for API requests.
    Enhances terminal output with colors and styles for better readability.

Prerequisites

    Python 3.6 or higher
    requests library
    colorama library
    termcolor library

You can install the required libraries using pip:

pip install requests colorama termcolor
Usage

    Clone the repository:

git clone
cd

    Run the script:

python kucoin_price_tracker.py

    Enter the trading pair:

When prompted, enter the trading pair you want to track (e.g., BTC-USDT).

    View real-time price updates:

The script will continuously fetch and display the price information every 2 seconds. Press Ctrl+C to stop the tracker.
Project Structure

kucoin-price-tracker/
│
├── kucoin_price_tracker.py # Main script file
├── requirements.txt # Python dependencies
├── LICENSE # License file
└── README.md # This file
Installation

    Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt
Requirements

Create a requirements.txt file with the following content:

requests==2.31.0
colorama==0.4.6
termcolor==2.3.0
Code Structure
Main Components

    KucoinPriceTracker Class

class KucoinPriceTracker:
def init(self):
self.base_url = "https://api.kucoin.com/api/v1"
self.headers = {'Accept': 'application/json'}

    Price Fetching Method

def get_price(self, symbol: str) -> Optional[Dict]:
"""Get current price for a trading pair"""
try:
url = f"{self.base_url}/market/orderbook/level1?symbol={symbol}"
response = requests.get(url, headers=self.headers, timeout=10)
response.raise_for_status()
data = response.json()
undefined

if data['code'] == '200000':
        return data['data']
    return None

    Price Formatting Method

def format_price_info(self, symbol: str, price_data: Dict) -> str:
"""Format price information for display"""
if not price_data or 'price' not in price_data:
return colored(f"Unable to get price for {symbol}", 'red')
undefined

current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
price = float(price_data['price'])
size = float(price_data.get('size', 0))

Configuration

No additional configuration is required. The script uses the public KuCoin API endpoints.
Error Handling

The script includes comprehensive error handling for:

    Network connection issues
    Invalid API responses
    Invalid trading pair format
    Keyboard interruption (Ctrl+C)

Contributing

    Fork the repository
    Create your feature branch (git checkout -b feature/AmazingFeature)
    Commit your changes (git commit -m 'Add some AmazingFeature')
    Push to the branch (git push origin feature/AmazingFeature)
    Open a Pull Request

Author

    s3nh - Initial work - GitHub Profile

Created: 2025-01-03 21:16:29 UTC
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    KuCoin API Documentation
    Colorama - Terminal text colors
    Termcolor - ANSI color formatting

Support

For support, please create an issue in the GitHub repository or contact the maintainer.
Disclaimer

This script is for educational and informational purposes only. Use at your own risk. The author is not responsible for any financial losses incurred while using this script.
Future Improvements

    Add support for multiple trading pairs simultaneously
    Implement historical price data visualization
    Add price alerts and notifications
    Include more detailed market information
    Add configuration file support
    Implement logging functionality

