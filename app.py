import requests
import time
import os
import sys
from datetime import datetime
from typing import Optional, Dict
from colorama import init, Fore, Style
from termcolor import colored

# Initialize colorama
init(autoreset=True)

class KucoinPriceTracker:
    def __init__(self):
        self.base_url = "https://api.kucoin.com/api/v1"
        self.headers = {'Accept': 'application/json'}
        
    def get_price(self, symbol: str) -> Optional[Dict]:
        """Get current price for a trading pair"""
        try:
            url = f"{self.base_url}/market/orderbook/level1?symbol={symbol}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data['code'] == '200000':
                return data['data']
            return None
            
        except requests.exceptions.RequestException as e:
            print(colored(f"\nError fetching price: {e}", 'red'))
            return None

    def format_price_info(self, symbol: str, price_data: Dict) -> str:
        """Format price information for display"""
        if not price_data or 'price' not in price_data:
            return colored(f"Unable to get price for {symbol}", 'red')
            
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        price = float(price_data['price'])
        size = float(price_data.get('size', 0))
        
        return (f"\n{colored(symbol, 'cyan', attrs=['bold'])} {colored('Price Information', 'magenta')}"
                f"\n{colored('-' * 24, 'yellow')}"
                f"\n{colored('Price:', 'green')} {Fore.YELLOW}${price:,.8f}"
                f"\n{colored('Size:', 'green')} {Fore.YELLOW}{size:,.8f}"
                f"\n{colored('Time:', 'green')} {Fore.YELLOW}{current_time}")

def clear_terminal_line():
    """Clear the current terminal line"""
    sys.stdout.write('\r')
    sys.stdout.write(' ' * 80)
    sys.stdout.write('\r')

def main():
    tracker = KucoinPriceTracker()
    
    print(colored("KuCoin Real-time Price Tracker", 'blue', attrs=['bold']))
    print(colored("-" * 30, 'yellow'))
    
    # Get trading pair from user
    symbol = input(colored("Enter trading pair (e.g., BTC-USDT): ", 'cyan')).upper().strip()
    
    # Validate symbol format
    if '-' not in symbol:
        print(colored("Invalid symbol format. Example format: BTC-USDT", 'red'))
        return
    
    print(colored(f"\nStarting price tracking for {symbol}", 'green'))
    print(colored("Press Ctrl+C to exit\n", 'yellow'))
    
    update_interval = 2  # seconds between updates
    
    try:
        while True:
            os.system('clear')
            price_data = tracker.get_price(symbol)
            clear_terminal_line()
            print(tracker.format_price_info(symbol, price_data), end='')
            time.sleep(update_interval)
            
    except KeyboardInterrupt:
        print(colored("\n\nStopping price tracker...", 'yellow'))
    except Exception as e:
        print(colored(f"\nAn error occurred: {e}", 'red'))
    finally:
        print(colored("\nTracker stopped. Goodbye!", 'blue'))

if __name__ == "__main__":
    main()
