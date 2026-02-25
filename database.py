import sqlite3
import os
import sys


def get_db_path():
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "factory.db")


def setup_db():
    db_path = get_db_path()
    c = sqlite3.connect(db_path, check_same_thread=False)
    c.executescript("""
        CREATE TABLE IF NOT EXISTS inventory (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name           TEXT    NOT NULL,
            quantity            REAL    NOT NULL DEFAULT 0,
            unit                TEXT    NOT NULL,
            low_stock_threshold REAL    NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS purchases (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id       INTEGER REFERENCES inventory(id),
            quantity      REAL    NOT NULL,
            cost          REAL    NOT NULL,
            supplier_name TEXT    NOT NULL,
            date          TEXT    NOT NULL
        );
        CREATE TABLE IF NOT EXISTS sales (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name  TEXT NOT NULL,
            box_type       TEXT NOT NULL,
            quantity       REAL NOT NULL,
            price_per_unit REAL NOT NULL,
            total_amount   REAL NOT NULL,
            date           TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS billing (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_number TEXT NOT NULL,
            customer_name  TEXT NOT NULL,
            quantity       REAL NOT NULL,
            price          REAL NOT NULL,
            total_amount   REAL NOT NULL,
            date           TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS ready_to_deliver (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            status        TEXT NOT NULL,
            date          TEXT NOT NULL
        );
    """)
    c.commit()
    c.close()
