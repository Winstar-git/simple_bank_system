import tkinter as tk
from tkinter import messagebox
from bank import Bank
from manager_account import ManagerAccount
from savings_account import SavingsAccount

class SBSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank System")
        self.root.configure(bg="blue")
        self.root.geometry(self.center_window(800,600))
        self.root.resizable(False, False)

        self.bank = Bank()
        self.current_role = "Customer"
        self.current_account = None

        self.container = tk.Frame(root, bg="blue")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.setup_frames()
        self.show(self.splash_frame)
        self.start_splash()

    def center_window(self, w, h):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = int((screen_w - w) / 2)
        y = int((screen_h - h) / 2)
        return f"{w}x{h}+{x}+{y}"
    
    def setup_frames(self):
        self.splash_frame = tk.Frame(self.container, bg="blue")
        self.splash_frame.grid(row=0, column=0, sticky="nsew")
        tk.Label(self.splash_frame, text="SBS", font=("Arial", 48, "bold"), fg="white", bg="blue").pack(pady=(180, 10))
        tk.Label(self.splash_frame, text="Simple Bank System", font=("Arial", 20), fg="white", bg="blue").pack()
        self.loading_label = tk.Label(self.splash_frame, text="", font=("Arial", 40), fg="white", bg="blue")
        self.loading_label.pack()

        self.login_frame = tk.Frame(self.container, bg="blue")
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.setup_login_ui()

        self.customer_frame = tk.Frame(self.container, bg="blue")
        self.customer_frame.grid(row=0, column=0, sticky="nsew")

        self.manager_frame = tk.Frame(self.container, bg="blue")
        self.manager_frame.grid(row=0, column=0, sticky="nsew") 

        
