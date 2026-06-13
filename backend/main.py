from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    merchant: str
    amount: float


@app.get("/transactions")
def get_transactions():
    return [
        {"merchant": "Dominos", "amount": 7.99},
        {"merchant": "Loyal Legion", "amount": 30.00}
    ]

@app.post("/transactions")
def post_transaction(transaction_info: Transaction):
    return transaction_info