"""
Master constants for FinChat seed data.
"""

# ==========================================================
# TRANSACTION CATEGORIES
# ==========================================================

CATEGORIES = [
    "Food",
    "Groceries",
    "Shopping",
    "Travel",
    "Bills",
    "Entertainment",
    "Healthcare",
    "Investment",
    "Salary",
    "Transfer"
]

# ==========================================================
# ACCOUNTS
# ==========================================================

ACCOUNTS = [
    {
        "account_name": "Salary Account",
        "bank_name": "ICICI Bank",
        "account_type": "Savings"
    },
    {
        "account_name": "Primary Savings",
        "bank_name": "HDFC Bank",
        "account_type": "Savings"
    },
    {
        "account_name": "Amazon ICICI Card",
        "bank_name": "ICICI Bank",
        "account_type": "Credit Card"
    }
]

# ==========================================================
# MERCHANTS
# ==========================================================

MERCHANTS = {

    "Food": [

        ("Swiggy", "Food Delivery"),
        ("Zomato", "Food Delivery"),
        ("Domino's", "Restaurant"),
        ("McDonald's", "Restaurant"),
        ("Subway", "Restaurant"),
        ("Burger King", "Restaurant"),
        ("Starbucks", "Restaurant")

    ],

    "Groceries": [

        ("DMart", "Supermarket"),
        ("BigBasket", "Supermarket"),
        ("Blinkit", "Quick Commerce"),
        ("Zepto", "Quick Commerce")

    ],

    "Shopping": [

        ("Amazon", "E-Commerce"),
        ("Flipkart", "E-Commerce"),
        ("Myntra", "E-Commerce"),
        ("Ajio", "E-Commerce")

    ],

    "Travel": [

        ("Uber", "Ride Sharing"),
        ("Ola", "Ride Sharing"),
        ("IRCTC", "Travel Booking"),
        ("MakeMyTrip", "Travel Booking")

    ],

    "Bills": [

        ("Airtel", "Utility"),
        ("Jio", "Utility"),
        ("Adani Electricity", "Utility"),
        ("Tata Power", "Utility")

    ],

    "Entertainment": [

        ("Netflix", "Subscription"),
        ("Spotify", "Subscription"),
        ("BookMyShow", "Entertainment")

    ],

    "Healthcare": [

        ("Apollo Pharmacy", "Healthcare"),
        ("1mg", "Healthcare"),
        ("MedPlus", "Healthcare")

    ],

    "Investment": [

        ("Groww", "Investment Platform"),
        ("Zerodha", "Investment Platform"),
        ("Angel One", "Investment Platform")

    ],

    "Salary": [

        ("Company Salary", "Salary")

    ],

    "Transfer": [

        ("Bank Transfer", "Transfer")

    ]
}

# ==========================================================
# PAYMENT MODES
# ==========================================================

PAYMENT_MODES = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash",
    "Auto Debit"
]

# ==========================================================
# DEFAULT MONTHLY BUDGETS
# ==========================================================

DEFAULT_BUDGETS = {

    "Food": 15000,
    "Groceries": 8000,
    "Shopping": 10000,
    "Travel": 7000,
    "Bills": 6000,
    "Entertainment": 3000,
    "Healthcare": 5000,
    "Investment": 20000
}