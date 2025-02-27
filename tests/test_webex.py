import pytest
import asyncio
from app.services import WebexClient
from app.config import WEBEX_TOKEN

@pytest.mark.asyncio
async def test_create_room():
    client = WebexClient(WEBEX_TOKEN)
    response = await client.create_room("Test Room")
    assert "id" in response

@pytest.mark.asyncio
async def test_create_team():
    client = WebexClient(WEBEX_TOKEN)
    response = await client.create_team("Test Team")
    assert "id" in response
