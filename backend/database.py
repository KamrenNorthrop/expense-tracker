import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

database_url = os.getenv("SUPABASE_URL")
api_key = os.getenv("SUPABASE_API_KEY")
supabase: Client = create_client(database_url, api_key)