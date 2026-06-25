import os
from dotenv import load_dotenv
import plaid
from plaid.api import plaid_api

load_dotenv()
env = os.getenv('PLAID_ENV')
client_id = os.getenv('PLAID_CLIENT_ID')
secret_key = os.getenv('PLAID_SECRET')

if not env:
    raise ValueError('PLAID_ENV environment variable is not set.')
env = env.capitalize()

## Check to make sure environment variables are a str and not none
if not client_id:
    raise ValueError('PLAID_CLIENT_ID environment variable is not set.')

if not secret_key:
    raise ValueError('PLAID_SECRET environment variable is not set.')

config = plaid.Configuration(
    host = getattr(plaid.Environment, env),
    api_key={
        'clientId': client_id,
        'secret': secret_key
    }
)

api_client = plaid.ApiClient(config)
client = plaid_api.PlaidApi(api_client)