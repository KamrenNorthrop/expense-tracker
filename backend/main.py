from fastapi import FastAPI
app = FastAPI()

@app.get("/transactions")
def get_transactions():
    return [
        {"merchant": "Dominos", "amount": 7.99},
        {"merchant": "Loyal Legion", "amount": 30.00}
    ]