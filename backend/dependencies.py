from fastapi import Header, HTTPException
from database import supabase

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        auth = supabase.auth.get_user(token)

        if not auth:
            raise HTTPException(status_code=401, detail="Invalid Token")
        return auth
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Token")