from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from uuid import uuid4
from database import supabase

app = FastAPI()

## Enum class for transaction type - there will always be a type
class TransactionTypeEnum(str, Enum):
    credit = 'credit'
    debit = 'debit'
    cash = 'cash'

## Pydantic model for transactions
class TransactionInput(BaseModel):
    user_id: str
    merchant: str
    amount: float
    transaction_date: datetime
    transaction_category: str | None = None
    transaction_type: TransactionTypeEnum
    transaction_description: str | None = None
    source: str

## Create a unique id using uuid4
class Transaction(TransactionInput):
      transaction_id: str = Field(default_factory=lambda: str(uuid4()))

## GET
@app.get("/transactions")
def get_transactions():
    transaction_query = supabase.table("transactions").select("*").execute()
    return transaction_query.data

## POST
@app.post("/transactions")
def post_transaction(transaction_info: TransactionInput):
    #Create object that includes transaction_id
    #use that object and model dump it, mode = json
    #insert into database, return dictionary
    transaction_info = Transaction(**transaction_info.model_dump())
    data = transaction_info.model_dump(mode='json')
    supabase.table("transactions").insert(data).execute()
    return data