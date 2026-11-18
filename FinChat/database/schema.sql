-- ==========================================================
-- FINCHAT AI DATABASE SCHEMA
-- ==========================================================

PRAGMA foreign_keys = ON;

-------------------------------------------------------------
-- ACCOUNTS
-------------------------------------------------------------
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT NOT NULL,
    bank_name TEXT NOT NULL,
    account_type TEXT NOT NULL
        CHECK (account_type IN ('Savings', 'Current', 'Credit Card', 'Wallet')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-------------------------------------------------------------
-- CATEGORIES
-------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-------------------------------------------------------------
-- TRANSACTIONS
-------------------------------------------------------------
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_date DATE NOT NULL,

    merchant TEXT NOT NULL,

    merchant_category TEXT NOT NULL
        CHECK (merchant_category IN ('Food Delivery','Restaurant','Supermarket','Quick Commerce','Ride Sharing',
        'Subscription','Utility','Investment Platform','Salary','Transfer','E-Commerce','Healthcare')),

    category_id INTEGER NOT NULL,

    amount REAL NOT NULL,

    transaction_type TEXT NOT NULL
        CHECK(transaction_type IN ('Debit', 'Credit')),

    payment_mode TEXT NOT NULL
        CHECK (payment_mode IN ('UPI', 'Credit Card', 'Debit Card', 'Net Banking', 'Cash', 'Auto Debit')),

    account_id INTEGER NOT NULL,

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(category_id)
        REFERENCES categories(id),

    FOREIGN KEY(account_id)
        REFERENCES accounts(id)
);

-------------------------------------------------------------
-- BUDGETS
-------------------------------------------------------------
CREATE TABLE IF NOT EXISTS budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    category_id INTEGER NOT NULL UNIQUE,

    monthly_budget REAL NOT NULL,

    FOREIGN KEY(category_id)
        REFERENCES categories(id)
);

-------------------------------------------------------------
-- INDEXES
-------------------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_transactions_date
ON transactions(transaction_date);

CREATE INDEX IF NOT EXISTS idx_transactions_merchant
ON transactions(merchant);

CREATE INDEX IF NOT EXISTS idx_transactions_category
ON transactions(category_id);

CREATE INDEX IF NOT EXISTS idx_transactions_account
ON transactions(account_id);

CREATE INDEX IF NOT EXISTS idx_transactions_type
ON transactions(transaction_type);