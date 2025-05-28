
import random
from models import Token
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def generate_mock_data():
    """Generate mock cryptocurrency data"""
    try:
        # Clear existing data
        Token.clear_all()
        
        # Sample cryptocurrency data
        crypto_data = [
            ('BTC', 'Bitcoin', 45000),
            ('ETH', 'Ethereum', 3200),
            ('USDT', 'Tether', 1.00),
            ('BNB', 'Binance Coin', 420),
            ('ADA', 'Cardano', 1.25),
            ('XRP', 'Ripple', 0.85),
            ('SOL', 'Solana', 125),
            ('DOT', 'Polkadot', 35),
            ('DOGE', 'Dogecoin', 0.15),
            ('AVAX', 'Avalanche', 85)
        ]
        
        for symbol, name, base_price in crypto_data:
            # Add some randomness to the base price
            price = base_price * random.uniform(0.8, 1.2)
            Token(
                symbol=symbol,
                name=name,
                price=price,
                market_cap=price * random.uniform(1e6, 1e9),
                volume_24h=random.uniform(1e6, 1e10),
                change_24h=random.uniform(-10, 10)
            )

        logger.info("Mock data generated successfully")
    except Exception as e:
        logger.error(f"Error generating mock data: {str(e)}")
        raise

def get_tokens(search_query=None):
    """Get tokens with optional search"""
    try:
        if search_query:
            return Token.search(search_query)
        return Token.get_all()
    except Exception as e:
        logger.error(f"Error fetching tokens: {str(e)}")
        raise

def get_token_by_symbol(symbol):
    """Get a specific token by symbol"""
    try:
        return Token.find_by_symbol(symbol)
    except Exception as e:
        logger.error(f"Error fetching token by symbol: {str(e)}")
        raise

def update_token_data():
    """Simulate real-time price updates"""
    try:
        tokens = Token.get_all()
        for token in tokens:
            # Update price_5m if it's been more than 5 minutes (simulate this for demo)
            if token.created_at < datetime.utcnow() - timedelta(minutes=5):
                token.price_5m = token.price

            # Simulate price change (-5% to +5%)
            price_change = random.uniform(-0.05, 0.05)
            token.price *= (1 + price_change)
            
            # Update market cap based on new price
            token.market_cap = token.price * random.uniform(1e6, 1e9)
            
            # Update 24h volume
            token.volume_24h *= random.uniform(0.9, 1.1)
            
            # Update 24h change
            token.change_24h = price_change * 100

        logger.info("Token data updated successfully")
    except Exception as e:
        logger.error(f"Error updating token data: {str(e)}")
        raise

def get_updated_tokens():
    """Get all tokens as dictionaries"""
    try:
        return [token.to_dict() for token in Token.get_all()]
    except Exception as e:
        logger.error(f"Error fetching updated tokens: {str(e)}")
        raise
