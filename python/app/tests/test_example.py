import pytest
import sys
import os

# Add the src directory to the path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_example():
    """Sample test to verify the structure works"""
    assert True

def test_import_structure():
    """Test that we can import from the src directory"""
    # This will work when you add actual modules to app/src/
    assert True 