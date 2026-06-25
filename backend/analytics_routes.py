from fastapi import APIRouter, Depends
from dependencies import verify_token 
from database import supabase
from datetime import datetime
from dateutil.relativedelta import relativedelta

analytics_router = APIRouter(prefix='/analytics')

def get_month_range():
    today = datetime.now()
    start_of_month = datetime(today.year, today.month, 1)
    end_of_month = start_of_month + relativedelta(months=1, days=-1)
    return start_of_month, end_of_month

@analytics_router.get('/summary')
def get_analytics_summary(current_user=Depends(verify_token)):
    start_of_month, end_of_month = get_month_range()
    data = supabase.table('transactions').select('*').eq('user_id', current_user.user.id).gte('transaction_date', start_of_month).lte('transaction_date', end_of_month).execute()
    expenses = 0
    inflow = 0

    for transaction in data.data:
        if transaction['amount'] > 0:
            expenses += transaction['amount'] 
        else:
            inflow += transaction['amount'] 

    return {'income': abs(round(inflow, 2)), 'expenses': round(expenses, 2), 'saved': round((abs(inflow) - expenses ), 2)}

@analytics_router.get('/categories')
def get_categories(current_user=Depends(verify_token)):
    start_of_month, end_of_month = get_month_range()
    category_breakdown = {}
    data = supabase.table('transactions').select('*').eq('user_id', current_user.user.id).gte('transaction_date', start_of_month).lte('transaction_date', end_of_month).execute()


    for transaction in data.data:
        if transaction['transaction_category'] not in category_breakdown:
            category_breakdown[transaction['transaction_category']] = 0
        category_breakdown[transaction['transaction_category']] += transaction['amount']

        rounded_category_breakdown = {k: round(v, 2) for k,v in category_breakdown.items()}

    return rounded_category_breakdown

@analytics_router.get('/average')
def get_average(current_user=Depends(verify_token)):
    start_of_month, end_of_month = get_month_range()
    data = supabase.table('transactions').select('*').eq('user_id', current_user.user.id).gte('transaction_date', start_of_month).lte('transaction_date', end_of_month).execute()

    ## EDGE CASE: if there is no data
    if not len(data.data):
        return 0
    
    transactions = 0
    count = 0

    for transaction in data.data:
        if transaction['amount'] > 0:
            transactions += transaction['amount']
            count += 1

    ## EDGE CASE: None of the transactions are expenses
    if transactions == 0:
        return 0

    return (round(transactions / count, 2))

