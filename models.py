
from datetime import datetime
import random

class Token:
    """Simple in-memory token class for mock data"""
    
    # Class variable to store all tokens
    _tokens = []
    _next_id = 1
    
    def __init__(self, symbol, name, price, market_cap=None, volume_24h=None, change_24h=None):
        self.id = Token._next_id
        Token._next_id += 1
        self.symbol = symbol
        self.name = name
        self.price = price
        self.price_5m = price  # Initialize with current price
        self.market_cap = market_cap or random.uniform(1e6, 1e12)
        self.volume_24h = volume_24h or random.uniform(1e6, 1e10)
        self.change_24h = change_24h or random.uniform(-10, 10)
        self.created_at = datetime.utcnow()
        
        # Add to class storage
        Token._tokens.append(self)
    
    def to_dict(self):
        change_5m = ((self.price - self.price_5m) / self.price_5m) * 100 if self.price_5m else 0
        return {
            'id': self.id,
            'symbol': self.symbol,
            'name': self.name,
            'price': self.price,
            'price_5m': self.price_5m,
            'change_5m': round(change_5m, 2),
            'market_cap': self.market_cap,
            'volume_24h': self.volume_24h,
            'change_24h': self.change_24h,
            'age': (datetime.utcnow() - self.created_at).days
        }
    
    @classmethod
    def get_all(cls):
        """Get all tokens"""
        return cls._tokens
    
    @classmethod
    def find_by_symbol(cls, symbol):
        """Find token by symbol"""
        for token in cls._tokens:
            if token.symbol.lower() == symbol.lower():
                return token
        return None
    
    @classmethod
    def search(cls, query):
        """Search tokens by symbol or name"""
        if not query:
            return cls._tokens
        
        query = query.lower()
        results = []
        for token in cls._tokens:
            if query in token.symbol.lower() or query in token.name.lower():
                results.append(token)
        return results
    
    @classmethod
    def clear_all(cls):
        """Clear all tokens (useful for testing)"""
        cls._tokens = []
        cls._next_id = 1
