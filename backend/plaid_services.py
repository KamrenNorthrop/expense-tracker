from utils import get_env
from dotenv import load_dotenv
import plaid
from plaid.api import plaid_api

load_dotenv()

## Helper function make sure environment variables are a str and not none
env = get_env('PLAID_ENV').capitalize()
client_id = get_env('PLAID_CLIENT_ID')
secret_key = get_env('PLAID_SECRET')

config = plaid.Configuration(
    host = getattr(plaid.Environment, env),
    api_key={
        'clientId': client_id,
        'secret': secret_key
    }
)

api_client = plaid.ApiClient(config)
client = plaid_api.PlaidApi(api_client)