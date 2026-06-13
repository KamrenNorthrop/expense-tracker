## Expense Tracker
A mobile app that connects to your bank via Plaid, tracks spending automatically, and gives you real time analytics.


## SET UP
1. Create Directory Layout
   
       -Mkdir main project folder
       -Mkdir frontend, backend, etc

**3. Create Virtual Environment**

        -Run: python3 -m venv venv
        -Run activate script
            -Windows: venv\Scripts\activate
            -Mac/Linux: source venv/bin/activate

**5. Record project dependencies**
   
        (if setting up for the first time)
        -Install all needed packages
        -Run: pip freeze > requirements.txt

        (if setting up from existing version)
        -Run: pip install -r requirements.txt

**6. Start uvicorn**

       -Run: uvicorn main:app --reload
