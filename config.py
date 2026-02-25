import os
import sys

def get_base_dir():
    # When running as .exe (PyInstaller), use the exe's directory
    # When running as .py, use the script's directory
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR  = get_base_dir()
DB_PATH   = os.path.join(BASE_DIR, "factory.db")
APP_NAME  = "Factory Manager"
CURRENCY  = "₹"
STATUSES  = ["Ready", "Dispatched", "Delivered"]
VERSION   = "2.0"

# Colors
BLUE      = "#3b82f6"
GREEN     = "#22c55e"
RED       = "#ef4444"
ORANGE    = "#f59e0b"
