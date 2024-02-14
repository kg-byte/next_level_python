import pytest
from unittest.mock import patch
from solution import retrieve_data


@pytest.mark.asyncio
async def test_fetch_data():
    urls = [
        
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]
    expected_data = [f"Data from {url}" for url in urls]

    # Use patch to mock the asyncio.sleep function
    with patch("solution.asyncio.sleep") as mock_sleep:

        mock_sleep.return_value = None

        # Call the asynchronous function
        result = await retrieve_data(urls)
        assert result == expected_data
