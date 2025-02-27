import os
from dotenv import load_dotenv

#.env load file
load_dotenv()

WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
BASE_URL = "https://webexapis.com/v1/"
HEADERS = {
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json',
           'Authorization': WEBEX_TOKEN
           }
