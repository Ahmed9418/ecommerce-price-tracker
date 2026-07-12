# scraper.py
import requests
from bs4 import BeautifulSoup
import re

# Standard headers to mimic a real web browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_current_price(url: str) -> float:
    """Fetches the URL, parses the HTML, and returns the price as a float."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Specific CSS selector for books.toscrape.com
        price_element = soup.select_one("p.price_color")
        
        if price_element:
            price_text = price_element.get_text()
            # Extract just the numbers/decimals using regex (e.g., "£51.77" -> 51.77)
            clean_price = re.sub(r'[^\d.]', '', price_text)
            return float(clean_price)
        else:
            print(f"Failed to locate price element on: {url}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Network error while scraping {url}: {e}")
        return None