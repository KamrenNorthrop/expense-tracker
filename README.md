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
                
## Development Status

### Completed
        - FastAPI backend with PostgreSQL database
        - User registration and login
        - JWT authentication
        - User isolated transaction storage and retrieval (GET/POST)

### In Progress
        - Plaid bank integration
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
