import os
from dotenv import load_dotenv
import plaid
from plaid.api import plaid_api

load_dotenv()
env = os.getenv('PLAID_ENV').capitalize()

config = plaid.Configuration(
    host = getattr(plaid.Environment, env),
    api_key={
        'clientId': os.getenv('PLAID_CLIENT_ID'),
        'secret': os.getenv('PLAID_SECRET')
    }
)

api_client = plaid.ApiClient(config)
client = plaid_api.PlaidApi(api_client)