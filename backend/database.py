import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

database_url = os.getenv("SUPABASE_URL")
api_key = os.getenv("SUPABASE_API_KEY")

## Check to make sure environment variables are a str and not none
if not database_url:
    raise ValueError("SUPABASE_URL environment variable is not set.")

if not api_key:
    raise ValueError("SUPABASE_API_KEY environment variable is not set.")

supabase: Client = create_client(database_url, api_key)