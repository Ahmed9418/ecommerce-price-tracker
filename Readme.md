# 🛒 Automated E-Commerce Price Tracker

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Web%20Scraping-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)

A modular data pipeline that automatically scrapes e-commerce product pages, logs historical pricing data into an SQLite database, and dispatches automated email alerts when a product's price drops below a user-defined threshold.

## 📂 Architecture

*   **`database.py`**: Manages the SQLite database, handling product ingestion and relational time-series price logging.
*   **`scraper.py`**: Utilizes `requests` and `BeautifulSoup4` to parse raw HTML and extract target numerical values using regex.
*   **`notifier.py`**: Connects to SMTP servers to dispatch secure email alerts using Python's `email.message` module.
*   **`main.py`**: The central orchestrator that iterates through the database, executes the scraper, and evaluates price thresholds.

## 🚀 Quick Start

### 1. Install Dependencies

    pip install requests beautifulsoup4

### 2. Configure Alerts (Optional)
By default, the pipeline runs in `mock_mode` and will print the email alert to the console. To send real emails:
1. Open `main.py` and set `mock_mode=False` inside the `run_tracker()` function.
2. Open `notifier.py` and enter your Sender Email and App Password (if using Gmail, you must generate an App Password in your Google Account Security settings).

### 3. Run the Tracker

    python main.py

## 📊 Output Example

    Starting Daily Price Tracker...

    Checking: A Light in the Attic
     - Current Price: $51.77 (Target: $40.00)

    Checking: Tipping the Velvet
     - Current Price: $53.74 (Target: $60.00)

    ========================================
    [MOCK EMAIL SENT]
    Subject: 🚨 Price Drop Alert: Tipping the Velvet!
    Body: Great news! 
        
    The price for 'Tipping the Velvet' has dropped below your target of $60.00.
    It is currently available for $53.74.
    ========================================
