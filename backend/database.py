from dotenv import load_dotenv
from supabase import create_client, Client
from utils import get_env

load_dotenv()

## Helper function make sure environment variables are a str and not none
database_url = get_env("SUPABASE_URL")
api_key = get_env("SUPABASE_API_KEY")

supabase: Client = create_client(database_url, api_key)