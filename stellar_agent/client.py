"""Stellar blockchain client for payment operations."""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset, Operation
from typing import Dict, Any
from .config import config

class StellarClient:
    """Client for interacting with Stellar blockchain."""
    
    def __init__(self):
        self.server = Server(config.horizon_url)
    
    def get_account_info(self, account_id: str) -> Dict[str, Any]:
        """
        Fetch account information from Horizon.
        
        Args:
            account_id: Public key of the account
            
        Returns:
            Account information dictionary
        """
        response = self.server.accounts().account_id(account_id).call()
        return response
    
    def send_payment(
        self, 
        source_secret: str, 
        destination_public: str, 
        amount: float
    ) -> Dict[str, Any]:
        """
        Send XLM payment to a destination address.
        
        Args:
            source_secret: Secret key of the source account
            destination_public: Public key of the destination account
            amount: Amount of XLM to send
            
        Returns:
            Transaction response dictionary
        """
        source_keypair = Keypair.from_secret(source_secret)
        source_account = self.server.load_account(source_keypair.public_key)

        transaction = (
            TransactionBuilder(
                source_account=source_account,
                network_passphrase=config.network_passphrase,
                base_fee=100,
            )
            .append_operation(
                Operation.payment({
                    "destination": destination_public,
                    "asset": Asset.native(),
                    "amount": str(amount)
                })
            )
            .set_timeout(30)
            .build()
        )

        transaction.sign(source_keypair)
        response = self.server.submit_transaction(transaction)
        return response
