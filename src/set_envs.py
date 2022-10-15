import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_URL = os.getenv('API_ENDPOINT')
