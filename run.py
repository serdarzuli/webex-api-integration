import asyncio
from app.services import WebexClient
from app.config import WEBEX_TOKEN


async def main():
    client = WebexClient(WEBEX_TOKEN)

    # Create Room
    room_response = await client.create_room({"title": "ZL Room"})
    print("Room Created:", room_response)

    # Create Team
    team_response = await client.create_team({"name": "ZL Team"})
    print("Team Created:", team_response)

asyncio.run(main())
