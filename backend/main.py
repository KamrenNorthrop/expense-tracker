from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from uuid import uuid4

app = FastAPI()

class TransactionTypeEnum(str, Enum):
    credit = 'credit'
    debit = 'debit'
    cash = 'cash'

class TransactionInput(BaseModel):
    user_id: str
    merchant: str
    amount: float
    transaction_date: datetime
    transaction_category: str | None = None
    transaction_type: TransactionTypeEnum
    transaction_description: str | None = None
    source: str

class Transaction(TransactionInput):
      transaction_id: str = Field(default_factory=lambda: str(uuid4()))


@app.get("/transactions")
def get_transactions():
    return [
        {"merchant": "Dominos", "amount": 7.99},
        {"merchant": "Loyal Legion", "amount": 30.00}
    ]

@app.post("/transactions")
def post_transaction(transaction_info: TransactionInput):
    transaction_info = Transaction(**transaction_info.model_dump())
    return transaction_info