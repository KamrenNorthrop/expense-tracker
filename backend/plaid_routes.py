from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from plaid_services import client
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from dependencies import verify_token 
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from database import supabase
from uuid import uuid4
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

plaid_router = APIRouter(prefix='/plaid', tags=['Plaid'])

class PublicTokenExchange(BaseModel):
    public_token: str

@plaid_router.post('/create-link-token')
def get_link_token(current_user=Depends(verify_token)):
    request = LinkTokenCreateRequest(user = LinkTokenCreateRequestUser(client_user_id = current_user.user.id),
                                     client_name='Expense Tracker',
                                     products=[Products('transactions')],
                                     country_codes=[CountryCode('US')],
                                     language='en'
    )

    response = client.link_token_create(request)
    return response.to_dict()

@plaid_router.post('/exchange-token')
def get_exchange_token(public_token : PublicTokenExchange, current_user=Depends(verify_token)):
    exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token.public_token)
    exchange_response = client.item_public_token_exchange(exchange_request)
    access_token = exchange_response.to_dict()['access_token']
    
    data={
        'id' : str(uuid4()),
        'user_id' : current_user.user.id,
        'access_token' : access_token,
        'institution_id' : exchange_response.to_dict()['item_id'],
        'created_at' : datetime.now().isoformat(),
        'is_active' : True

    }
    supabase.table('plaid_connections').insert(data).execute()
    return data

## Plaid - Sandbox Post
@plaid_router.post('/sandbox/create-public-token')
def create_sandbox_token(current_user=Depends(verify_token)):
    request = SandboxPublicTokenCreateRequest(institution_id='ins_109508', initial_products=[Products('transactions')])
    response = client.sandbox_public_token_create(request)
    return response.to_dict()


## TODO: Map transaction types to enum values after connection
@plaid_router.get('/transactions/get')
def get_transactions(current_user=Depends(verify_token)):
    try:
        access_token = supabase.table('plaid_connections').select('access_token').eq("user_id", current_user.user.id).execute().data

        request = TransactionsGetRequest(
            access_token = access_token[0]['access_token'],
            start_date = (datetime.now() - relativedelta(months=24)).date(), 
            end_date = datetime.now().date(),
        )

        response = client.transactions_get(request)
        transactions = response.to_dict()['transactions']
        total_transactions = response.to_dict()['total_transactions']

        #Offset parameters to paginate per docs
        #Retrieve all available data
        while len(transactions) < total_transactions:
            request = TransactionsGetRequest(
                access_token = access_token[0]['access_token'], 
                start_date = (datetime.now() - relativedelta(months=24)).date(), 
                end_date = datetime.now().date(), 
                options=TransactionsGetRequestOptions(
                    offset=len(transactions)
                    )
            )
            response = client.transactions_get(request)
            transactions += response.to_dict()['transactions']

        for transaction in transactions:
            data = {
                'transaction_id' : transaction['transaction_id'],
                'user_id' : current_user.user.id,
                'merchant' : transaction['merchant_name'] or 'Unknown',
                'amount' : transaction['amount'],
                'transaction_date' : transaction['authorized_date'].isoformat() if transaction['authorized_date'] else None,
                'transaction_category' : transaction['category'] or 'Uncategorized',
                'transaction_type' : transaction['transaction_type'] or 'debit',
                'transaction_description' : transaction['name'] or 'No description',
                'source' : transaction['payment_channel'] or 'Unknown',
            }

            supabase.table('transactions').upsert(data, on_conflict='transaction_id').execute()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return len(transactions) > 0