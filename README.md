## Expense Tracker
A passive expense tracking app for people who hate budgeting. Connect your bank, pay as normal, and get real-time insights into your spending habits that utilizes budgeting tools and reminders to help you change them.

## Tech Stack (Relative to what has been completed currently)
        
        Back-end: FastAPI (API framework), Uvicorn (Server)
        Database: PostgreSQL via Supabase
        Auth: Supabase Auth (JWT based)

## Folder Hierarchy (Relative to what has been completed currently)

        -expense-tracker
                -backend
                        -main.py                # API routes and entry points
                        -auth.py                # Registration and login endpoints
                        -database.py            # Connection to Supabase PostgreSQL database
                        -dependencies.py        # JWT token verification
                        -requirements.txt       # Python dependencies for this project
                        -.env                   # Secret keys (Not commited)
                -.gitignore
                -README.md

## API Endpoints

### Auth

**POST /auth/register**

        - Creates a new user account
        - No auth required
        - Request body: {"email": str, "password": str}
        - Returns a user object

**POST /auth/login**

        - Authenticates a user and returns a JWT token
        - No auth required
        - Request body: {"email": str, "password": str}
        - Returns a session object with access_token

### Transactions

**GET /transactions**
        
        - Returns all transactions for the logged in user
        - Auth required
        - Returns an array of transaction objects

**POST /transactions**

        - Manually creates a new transaction
        - Auth required
        - Request body: {"merchant": str, "amount": float, "transaction_date": datetime, "transaction_category": str | None = None, "transaction_type": "credit" | "debit" | "cash", "transaction_description": str | None = None, "source": str}
        - Returns a created transaction object

### Plaid

**POST /plaid/create-link-token**

        - Creates a link token for the logged in user
        - Auth required
        - returns a link token object

**POST /plaid/exchange-token**

        - Requests a public -> access token exchange
        - Auth required
        - Request body: {"public_token": str}
        - Stores the access token into the PostgresSQL database
        - Returns a data dictionary

**GET /plaid/transactions/get**

        - Pulls the last 24 months of transaction data for the logged in user
        - Auth required
        - Stores transactions into PostgreSQL database
        - Returns a boolean (TRUE/FALSE) 

**POST /plaid/sandbox/create-public-token**

        - Creates a fake public token for sandbox testing
        - Development only - will not be available in production
        - Auth required
        - Returns a sandbox public token
                
## Development Status

### Completed
        - FastAPI backend with PostgreSQL database
        - User registration and login
        - JWT authentication
        - User isolated transaction storage and retrieval (GET/POST)
        - Plaid bank integration

### In Progress
        - Analytics endpoints
        - IOS mobile app (React Native / Expo)

### SET UP
## **1. To Clone**
        - Run: git clone https://github.com/KamrenNorthrop/expense-tracker.git
        - Run: cd expense-tracker/backend

## **2. Create Virtual Environment**
        - Run: python3 -m venv venv
        - Run activate script
            - Windows: venv\Scripts\activate
            - Mac/Linux: source venv/bin/activate

## **3. Install Project Dependencies**
        - Run: pip install -r requirements.txt

## **4. Create .env File In /backend With The Following:**
        - Variable: SUPABASE_URL=your_supabase_project_url
        - Variable: SUPABASE_API_KEY=your_supabase_anon_key

## **5. Start uvicorn**
       -Run: uvicorn main:app --reload
