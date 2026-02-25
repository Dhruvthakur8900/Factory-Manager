# 🏭 Factory Manager Desktop App

## ▶️ Run the App

1. Open terminal/command prompt INSIDE the `factory_desktop` folder
2. Install dependencies (only once):
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
A real desktop window will open — no browser!

---

## 📦 Build as .exe (Windows)

To make a double-click .exe file:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Build the exe:
   ```
   pyinstaller --onefile --windowed --name "FactoryManager" app.py
   ```

3. Your .exe will be in the `dist/` folder
4. Copy `dist/FactoryManager.exe` anywhere and double-click to run!

---

## 📁 Project Structure

```
factory_desktop/
├── app.py              ← Run this (main window)
├── config.py           ← Settings
├── database.py         ← DB setup
├── requirements.txt
│
├── db/                 ← Database queries (one file per module)
│   ├── base.py
│   ├── inventory_db.py
│   ├── purchases_db.py
│   ├── sales_db.py
│   ├── billing_db.py
│   └── deliver_db.py
│
├── gui/                ← UI pages (one file per page)
│   ├── widgets.py      ← Reusable components
│   ├── dashboard.py
│   ├── inventory.py
│   ├── sales.py
│   ├── billing.py
│   ├── deliver.py
│   └── reports.py
│
└── utils/              ← Helpers
    ├── pdf.py          ← Invoice PDF
    └── excel.py        ← Excel export
```
