"""Command-line interface for Stellar Agent."""
from .client import StellarClient
from .config import config
from .utils.validators import is_valid_stellar_address, is_valid_amount

def prompt_and_send():
    """Interactive CLI for sending Stellar payments."""
    client = StellarClient()
    
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("Please set SOURCE_SECRET in your environment variables or .env file")
        return
    
    while True:
        print("\n--- Stellar Agent ---")
        destination = input("Enter destination public key (or type 'exit' to quit): ").strip()
        
        if destination.lower() == "exit":
            break
        
        # Validate destination address
        if not is_valid_stellar_address(destination):
            print("❌ Invalid Stellar address. Must start with 'G' and be 56 characters long.")
            continue
        
        amount_str = input("Enter amount to send (in XLM): ").strip()
        
        try:
            amount = float(amount_str)
            if not is_valid_amount(amount):
                print("❌ Amount must be positive.")
                continue
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
            continue
        
        print(f"Sending {amount} XLM to {destination}...")
        try:
            response = client.send_payment(config.source_secret, destination, amount)
            print("✅ Transaction Successful!")
            print("Transaction Hash:", response['hash'])
        except Exception as e:
            print("❌ Transaction Failed:", str(e))

def run():
    """Entry point for the CLI."""
    prompt_and_send()
