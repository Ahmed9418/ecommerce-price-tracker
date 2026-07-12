# notifier.py
import smtplib
from email.message import EmailMessage
import os

# Configuration (Use Environment Variables in production)
EMAIL_ADDRESS = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
EMAIL_PASSWORD = os.getenv("SENDER_PASSWORD", "your_app_password")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "your_email@gmail.com")

def send_price_alert(product_name: str, current_price: float, target_price: float, url: str, mock_mode: bool = True):
    """Sends an email alert when the target price is reached."""
    
    subject = f"🚨 Price Drop Alert: {product_name}!"
    body = f"""
    Great news! 
    
    The price for '{product_name}' has dropped below your target of ${target_price:.2f}.
    It is currently available for ${current_price:.2f}.
    
    Buy it here: {url}
    """
    
    if mock_mode:
        print("\n" + "="*40)
        print("[MOCK EMAIL SENT]")
        print(f"Subject: {subject}")
        print(f"Body: {body.strip()}")
        print("="*40 + "\n")
        return

    # Real Email Sending Logic
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECEIVER_EMAIL
        msg.set_content(body)
        
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            
        print(f"Email alert sent successfully for {product_name}!")
        
    except Exception as e:
        print(f"Failed to send email alert: {e}")