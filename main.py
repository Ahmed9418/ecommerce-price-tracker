# main.py
import database as db
from scraper import get_current_price
from notifier import send_price_alert

def setup_seed_data():
    """Populates the database with initial products to track."""
    db.init_db()
    
    # We will track two books, setting one target price artificially high to trigger an alert
    db.add_product(
        name="A Light in the Attic",
        url="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        target_price=40.00  # Actual price is ~£51.77, so no alert
    )
    db.add_product(
        name="Tipping the Velvet",
        url="https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
        target_price=60.00  # Actual price is ~£53.74, THIS WILL TRIGGER AN ALERT
    )

def run_tracker():
    """Main execution loop for the tracker."""
    print("Starting Daily Price Tracker...")
    
    products = db.get_all_products()
    
    if not products:
        print("No products in database to track.")
        return

    for product in products:
        prod_id, name, url, target_price = product
        print(f"\nChecking: {name}")
        
        current_price = get_current_price(url)
        
        if current_price is not None:
            print(f" - Current Price: ${current_price:.2f} (Target:${target_price:.2f})")
            
            # 1. Log the price history
            db.log_price(prod_id, current_price)
            
            # 2. Check threshold and trigger alert
            if current_price <= target_price:
                # Set mock_mode=False when you have configured your real email credentials
                send_price_alert(name, current_price, target_price, url, mock_mode=True)
        else:
            print(f" - Failed to retrieve price for {name}")

if __name__ == "__main__":
    # Ensure database and seed data exists
    setup_seed_data()
    
    # Run the tracking cycle
    run_tracker()