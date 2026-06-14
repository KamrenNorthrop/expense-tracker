import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

database_url = os.getenv("SUPABASE_URL")
print(database_url)
api_key = os.getenv("SUPABASE_API_KEY")
print(api_key[:20])
supabase: Client = create_client(database_url, api_key)