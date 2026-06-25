import os

## Helper function
def get_env(key : str) -> str:
    value = os.getenv(key)

    if not value:
        raise ValueError(f"{key} environment variable is not set.")
    
    return value