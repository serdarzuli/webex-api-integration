import aiohttp
from soar_core.actions.base_action import BaseApp
from soar_core.functions import initialize_logger

logger = initialize_logger()



class App(BaseApp):
    NAME = "Webex"
    is_token_expiring = False
    base_url = 'https://webexapis.com/v1/'
    
    async def _get_auth(self):
        config = self.get_config()
        token = config['token']
        auth = f"Bearer {token}"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': auth
            }
       
    

    async def create_room(self,payload):

        url = f'{self.base_url}/rooms'
        return await self.post_request(url,payload)

    async def get_room(self):
    
        url = f'{self.base_url}/rooms'
        return await self.send_request(url)


    async def get_room_details(self,payload):

        url = f'{self.base_url}/rooms/{payload}'
        return await self.send_request(url)





    
    async def create_team(self,payload):
        url = f'{self.base_url}/teams'
        return await self.post_request(url,payload)






   
    async def get_list_teams(self):
        url = f'{self.base_url}/teams?max=100'
        return await self.send_request(url)



    async def delete_team(self,payload):
        
        url = f'{self.base_url}/teams/{payload}'
        async with aiohttp.ClientSession() as session:
            async with session.delete(url=url, headers=self._get_auth) as response:
                return await response.json



    
    async def create_memberships(self,payload):
        url = f'{self.base_url}/team/memberships'
        return await self.post_request(url,payload)



    async def get_list_team_memberships(self,payload):

        url = f'{self.base_url}/team/memberships'
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url,headers=self._get_auth,params=payload) as response:
                return await response.json



    async def get_team_membership_details(self,payload):
        url = f'{self.base_url}/team/memberships/{payload}'
        return await self.send_request(url)




    async def send_message(self,payload):
        url = f'{self.base_url}/messages'
        return await self.post_request(url,payload)








    async def post_request(self,url,payload):
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url,headers=self._get_auth,params=payload) as response:
                return await response.json



    async def send_request(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url,headers=self._get_auth) as response:
                return await response.json
        
