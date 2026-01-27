"""Tests for validation utilities."""
import pytest
from stellar_agent.utils.validators import is_valid_stellar_address, is_valid_amount

class TestValidators:
    """Test validation functions."""
    
    def test_valid_stellar_address(self):
        """Test valid Stellar address format."""
        valid_address = "GBRPYHIL2CI3FNQ4BXLFMNDLFJUNPU2HY3ZMFSHONUCEOASW7QC7OX2H"
        assert is_valid_stellar_address(valid_address) is True
    
    def test_invalid_stellar_address_wrong_prefix(self):
        """Test address with wrong prefix."""
        invalid_address = "ABRPYHIL2CI3FNQ4BXLFMNDLFJUNPU2HY3ZMFSHONUCEOASW7QC7OX2H"
        assert is_valid_stellar_address(invalid_address) is False
    
    def test_invalid_stellar_address_wrong_length(self):
        """Test address with wrong length."""
        invalid_address = "GBRPYHIL2CI3FNQ4BXLFMNDLFJUNPU2HY3ZMFSHONUCEOASW7QC7OX"
        assert is_valid_stellar_address(invalid_address) is False
    
    def test_empty_address(self):
        """Test empty address."""
        assert is_valid_stellar_address("") is False
    
    def test_valid_amount(self):
        """Test valid payment amount."""
        assert is_valid_amount(10.5) is True
        assert is_valid_amount(0.0000001) is True
    
    def test_invalid_amount(self):
        """Test invalid payment amounts."""
        assert is_valid_amount(0) is False
        assert is_valid_amount(-10) is False
