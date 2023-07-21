import pytest
from unittest.mock import Mock

# Helper function to create a mock cursor with the desired behavior
def create_mock_cursor(result=None):
    cursor = Mock()
    cursor.fetchone.return_value = result
    return cursor

# Create a mock connection with a mock cursor
def test_connection():
    connection = Mock()
    cursor = create_mock_cursor()
    connection.cursor.return_value = cursor

if __name__ == "__main__":
    pytest.main()
