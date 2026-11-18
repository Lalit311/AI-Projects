import random
import sqlite3
from pathlib import Path
from datetime import date, timedelta

from constants import (
    ACCOUNTS,
    CATEGORIES,
    DEFAULT_BUDGETS,
    MERCHANTS,
    PAYMENT_MODES,
)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "finance.db"


class SeedDatabase:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

        self.category_map = {}
        self.account_map = {}

    # -------------------------------------------------------
    # Categories
    # -------------------------------------------------------

    def insert_categories(self):

        for category in CATEGORIES:

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO categories(name)
                VALUES(?)
                """,
                (category,)
            )

        self.conn.commit()

        rows = self.cursor.execute(
            "SELECT id,name FROM categories"
        ).fetchall()

        self.category_map = {name: cid for cid, name in rows}

    # -------------------------------------------------------
    # Accounts
    # -------------------------------------------------------

    def insert_accounts(self):

        for account in ACCOUNTS:

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO accounts(
                    account_name,
                    bank_name,
                    account_type
                )
                VALUES(?,?,?)
                """,
                (
                    account["account_name"],
                    account["bank_name"],
                    account["account_type"],
                ),
            )

        self.conn.commit()

        rows = self.cursor.execute(
            """
            SELECT id,account_name
            FROM accounts
            """
        ).fetchall()

        self.account_map = {name: aid for aid, name in rows}

    # -------------------------------------------------------
    # Budgets
    # -------------------------------------------------------

    def insert_budgets(self):

        for category, budget in DEFAULT_BUDGETS.items():

            self.cursor.execute(
                """
                INSERT OR IGNORE INTO budgets(
                    category_id,
                    monthly_budget
                )
                VALUES(?,?)
                """,
                (
                    self.category_map[category],
                    budget,
                ),
            )

        self.conn.commit()

    # -------------------------------------------------------
    # Transactions
    # -------------------------------------------------------

    def generate_transactions(self):

        today = date.today()

        start = today - timedelta(days=365)

        current = start

        while current <= today:

            # Salary
            if current.day == 1:

                self.insert_transaction(
                    current,
                    "Company Salary",
                    "Salary",
                    "Salary",
                    140000,
                    "Credit",
                    "Net Banking",
                    "Salary Account",
                )

            # Netflix
            if current.day == 3:

                self.insert_transaction(
                    current,
                    "Netflix",
                    "Subscription",
                    "Entertainment",
                    649,
                    "Debit",
                    "Auto Debit",
                    "Primary Savings",
                )

            # SIP
            if current.day == 7:

                self.insert_transaction(
                    current,
                    "Groww",
                    "Investment Platform",
                    "Investment",
                    random.choice([5000,10000,15000]),
                    "Debit",
                    "Net Banking",
                    "Primary Savings",
                )

            # Grocery
            if current.weekday() in [5,6] and random.random() < 0.60:

                merchant = random.choice([
                    "DMart",
                    "Blinkit",
                    "Zepto",
                    "BigBasket"
                ])

                category = (
                    "Quick Commerce"
                    if merchant in ["Blinkit","Zepto"]
                    else "Supermarket"
                )

                self.insert_transaction(
                    current,
                    merchant,
                    category,
                    "Groceries",
                    random.randint(1000,4000),
                    "Debit",
                    random.choice(["UPI","Credit Card"]),
                    "Primary Savings",
                )

            # Food
            if random.random() < 0.80:

                for _ in range(random.randint(1,3)):

                    merchant = random.choice([
                        "Swiggy",
                        "Zomato",
                        "Domino's",
                        "McDonald's",
                        "Burger King",
                        "Starbucks"
                    ])

                    merchant_category = (
                        "Food Delivery"
                        if merchant in ["Swiggy","Zomato"]
                        else "Restaurant"
                    )

                    self.insert_transaction(
                        current,
                        merchant,
                        merchant_category,
                        "Food",
                        random.randint(150,900),
                        "Debit",
                        random.choice(["UPI","Credit Card"]),
                        "Primary Savings",
                    )

            # Uber/Ola
            if current.weekday() < 5 and random.random() < 0.50:

                for _ in range(random.randint(0,2)):

                    self.insert_transaction(
                        current,
                        random.choice(["Uber","Ola"]),
                        "Ride Sharing",
                        "Travel",
                        random.randint(120,450),
                        "Debit",
                        random.choice(["UPI","Credit Card"]),
                        "Primary Savings",
                    )

            # Shopping
            if random.random() < 0.15:

                merchant = random.choice([
                    "Amazon",
                    "Flipkart",
                    "Myntra"
                ])

                self.insert_transaction(
                    current,
                    merchant,
                    "E-Commerce",
                    "Shopping",
                    random.randint(700,7000),
                    "Debit",
                    "Credit Card",
                    "Amazon ICICI Card",
                )

            current += timedelta(days=1)

        self.conn.commit()

    # -------------------------------------------------------
    # Insert helper
    # -------------------------------------------------------

    def insert_transaction(
        self,
        transaction_date,
        merchant,
        merchant_category,
        category,
        amount,
        transaction_type,
        payment_mode,
        account_name,
    ):

        self.cursor.execute(
            """
            INSERT INTO transactions(
                transaction_date,
                merchant,
                merchant_category,
                category_id,
                amount,
                transaction_type,
                payment_mode,
                account_id
            )
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                transaction_date.isoformat(),
                merchant,
                merchant_category,
                self.category_map[category],
                amount,
                transaction_type,
                payment_mode,
                self.account_map[account_name],
            ),
        )

    # -------------------------------------------------------

    def close(self):

        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":

    db = SeedDatabase()

    db.insert_categories()
    db.insert_accounts()
    db.insert_budgets()
    db.generate_transactions()

    db.close()

    print("Database seeded successfully.")