import aiohttp
from app.config import BASE_URL, HEADERS

class WebexClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS
    
    
    async def create_room(self,payload):
        url = f'{self.base_url}/rooms'
        return await self._post_request(url,payload)


    async def get_room(self):
        url = f'{self.base_url}/rooms'
        return await self._send_request(url)

      
    async def create_team(self,payload):
        url = f'{self.base_url}/teams'
        return await self._post_request(url,payload)

   
    async def delete_team(self,payload):
        url = f'{self.base_url}/teams/{payload}'
        async with aiohttp.ClientSession() as session:
            async with session.delete(url=url, headers=self.headers) as response:
                return await response.json


    async def send_message(self,payload):
        url = f'{self.base_url}/messages'
        return await self._post_request(url, payload)


    async def _post_request(self,url,payload):
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=self.headers, params=payload) as response:
                return await response.json


    async def _send_request(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as response:
                return await response.json
        