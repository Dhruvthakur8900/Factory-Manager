import sys
import os

if getattr(sys, "frozen", False):
    ROOT = os.path.dirname(sys.executable)
else:
    ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import customtkinter as ctk
from database import setup_db
from config import APP_NAME, VERSION, BLUE
from gui.dashboard import DashboardPage
from gui.inventory import InventoryPage
from gui.sales     import SalesPage
from gui.billing   import BillingPage
from gui.deliver   import DeliverPage
from gui.reports   import ReportsPage

# ── Setup ─────────────────────────────────────────────────────
setup_db()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class FactoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"{APP_NAME}  v{VERSION}")

        # ── Responsive: 85% of screen size ───────────────────
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w  = int(sw * 0.85)
        h  = int(sh * 0.85)
        x  = (sw - w) // 2
        y  = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.minsize(900, 600)

        self._build_ui()

    def _build_ui(self):
        # ── Root layout ───────────────────────────────────────
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ── Sidebar ───────────────────────────────────────────
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0,
                               fg_color=("gray93", "#0f1420"))
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(10, weight=1)
        sidebar.grid_propagate(False)

        # Logo
        ctk.CTkLabel(sidebar, text="🏭",
                     font=ctk.CTkFont(size=40)).grid(row=0, column=0, pady=(28,4), padx=20)
        ctk.CTkLabel(sidebar, text=APP_NAME,
                     font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=0, pady=(0,2))
        ctk.CTkLabel(sidebar, text=f"v{VERSION}",
                     font=ctk.CTkFont(size=10), text_color="gray").grid(row=2, column=0, pady=(0,16))

        ctk.CTkFrame(sidebar, height=1, fg_color=("gray80","gray30")).grid(
            row=3, column=0, sticky="ew", padx=14, pady=(0,10))

        # Nav buttons
        nav_items = [
            ("🏠  Dashboard",      "dashboard"),
            ("📦  Inventory",      "inventory"),
            ("🛍️  Sales",          "sales"),
            ("🧾  Billing",        "billing"),
            ("🚚  Ready to Deliver","deliver"),
            ("📊  Reports",        "reports"),
        ]

        self.nav_buttons = {}
        for i, (label, key) in enumerate(nav_items, start=4):
            btn = ctk.CTkButton(
                sidebar, text=label, anchor="w",
                font=ctk.CTkFont(size=12),
                fg_color="transparent",
                text_color=("gray20","gray80"),
                hover_color=("gray85","gray25"),
                corner_radius=8, height=40,
                command=lambda k=key: self._show_page(k)
            )
            btn.grid(row=i, column=0, padx=10, pady=2, sticky="ew")
            self.nav_buttons[key] = btn

        # Spacer + theme toggle at bottom
        ctk.CTkLabel(sidebar, text="🎨 Theme",
                     font=ctk.CTkFont(size=10), text_color="gray").grid(
                     row=11, column=0, pady=(0,4))
        self.theme_switch = ctk.CTkSwitch(
            sidebar, text="Light Mode",
            command=self._toggle_theme,
            font=ctk.CTkFont(size=11)
        )
        self.theme_switch.grid(row=12, column=0, pady=(0,20), padx=16)

        # ── Content area ──────────────────────────────────────
        self.content = ctk.CTkFrame(self, corner_radius=0, fg_color=("gray95","#0a0d14"))
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # Preload all pages
        self.pages = {
            "dashboard": DashboardPage(self.content),
            "inventory": InventoryPage(self.content),
            "sales":     SalesPage(self.content),
            "billing":   BillingPage(self.content),
            "deliver":   DeliverPage(self.content),
            "reports":   ReportsPage(self.content),
        }
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self._show_page("dashboard")

    def _show_page(self, key):
        # Highlight active nav button
        for k, btn in self.nav_buttons.items():
            if k == key:
                btn.configure(fg_color=BLUE, text_color="white")
            else:
                btn.configure(fg_color="transparent",
                              text_color=("gray20","gray80"))

        # Refresh and show selected page
        page = self.pages[key]
        if hasattr(page, "refresh"):
            page.refresh()
        page.tkraise()

    def _toggle_theme(self):
        if self.theme_switch.get():
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")


if __name__ == "__main__":
    app = FactoryApp()
    app.mainloop()
