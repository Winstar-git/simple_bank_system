import tkinter as tk
from tkinter import messagebox
from bank import Bank
import bank
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
        # Center SBS and subtitle in splash frame
        splash_center = tk.Frame(self.splash_frame, bg="blue")
        splash_center.pack(expand=True)
        tk.Label(splash_center, text="SBS", font=("Arial", 48, "bold"), fg="white", bg="blue").pack(pady=(0, 10))
        tk.Label(splash_center, text="Simple Bank System", font=("Arial", 20), fg="white", bg="blue").pack()
        self.loading_label = tk.Label(splash_center, text="", font=("Arial", 40), fg="white", bg="blue")
        self.loading_label.pack()

        self.login_frame = tk.Frame(self.container, bg="blue")
        self.login_frame.grid(row=0, column=0, sticky="nsew")
        self.setup_login_ui()

        self.customer_frame = tk.Frame(self.container, bg="blue")
        self.customer_frame.grid(row=0, column=0, sticky="nsew")

        self.manager_frame = tk.Frame(self.container, bg="blue")
        self.manager_frame.grid(row=0, column=0, sticky="nsew") 

    def add_header(self, frame):
        header = tk.Frame(frame, bg="blue")
        header.pack(anchor="nw", padx=20, pady=20)
        tk.Label(header, text="SBS", font=("Arial", 40, "bold"), fg="white", bg="blue").pack(anchor="w")
        tk.Label(header, text="Simple Bank System", font=("Arial", 16), fg="white", bg="blue").pack(anchor="w")

    def setup_login_ui(self):
        self.add_header(self.login_frame)
        login_form = tk.Frame(self.login_frame, bg="blue")
        login_form.place(relx=0.5, rely=0.5, anchor="center")

        self.role_label = tk.Label(login_form, text="Customer Login", font=("Arial", 20, "bold"), bg="blue", fg="white")
        self.role_label.pack(pady=(0, 10))

        self.user_label = tk.Label(login_form, text="Account number", bg="blue", fg="white", font=("Arial", 14))
        self.user_label.pack()
        self.entry_user = tk.Entry(login_form, font=("Arial", 14), width=25, bg="white", fg="black")
        self.entry_user.pack(pady=(0, 10))

        self.pin_label = tk.Label(login_form, text="PIN", bg="blue", fg="white", font=("Arial", 14))
        self.pin_label.pack()
        self.entry_pin = tk.Entry(login_form, font=("Arial", 14), show="*", width=25, bg="white", fg="black")
        self.entry_pin.pack(pady=(0, 20))

        tk.Button(login_form, text="Login", font=("Arial", 14), width=20,
                bg="white", fg="blue", command=self.handle_login).pack()
        self.login_frame.bind_all("<F12>", self.toggle_role)

    def show(self, frame):
        frame.tkraise()

    def start_splash(self):
        symbols = ["◐", "◓", "◑", "◒"]
        def animate(index=0):
            self.loading_label.config(text=symbols[index % len(symbols)])
            self.root.after(200, animate, index + 1)
        animate()
        self.root.after(2000, lambda: self.show(self.login_frame))

    def toggle_role(self, event=None):
        if self.current_role.lower() == "customer":
            self.current_role = "manager"
            self.role_label.config(text="🛠 Manager Login")
            self.user_label.config(text="User")
            self.pin_label.config(text="Password")
        else:
            self.current_role = "customer"
            self.role_label.config(text="Customer Login")
            self.user_label.config(text="Account number")
            self.pin_label.config(text="PIN")

    def handle_login(self):
        acc_no = self.entry_user.get().strip()
        pin = self.entry_pin.get().strip()
        if not acc_no.isdigit() or not pin.isdigit():
            messagebox.showerror("Login Failed", "Account number and PIN must be numbers.")
            return
        print(f"Trying login with: {acc_no} / {pin}")
        account = self.bank.get_account(acc_no, pin)

        if account:
            print("Login successful!")
            self.current_account = account
            if hasattr(account, "get_balance"):
                self.show_customer_dashboard()
            else:
                self.show_manager_dashboard()
        else:
            print("Login failed.")
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def show_customer_dashboard(self):
        self.clear_frame(self.customer_frame)
        self.add_header(self.customer_frame)

        info_frame = tk.Frame(self.customer_frame, bg="blue")
        info_frame.pack(pady=20)

        tk.Label(info_frame, text=f"Account Number: {self.current_account._account_number}",
                 font=("Arial", 16), fg="white", bg="blue", anchor="w").pack(anchor="w")
        tk.Label(info_frame, text=f"Account Holder: {self.current_account._account_holder}",
                 font=("Arial", 16), fg="white", bg="blue", anchor="w").pack(anchor="w")
        tk.Label(info_frame, text=f"Balance: P{self.current_account.get_balance():.2f}",
                 font=("Arial", 16, "bold"), fg="white", bg="blue", anchor="w").pack(anchor="w", pady=(0, 10))

        action_frame = tk.Frame(self.customer_frame, bg="blue")
        action_frame.pack(pady=10)

        amount_entry = tk.Entry(action_frame, font=("Arial", 14))
        amount_entry.pack(pady=(0, 10))

        tk.Button(action_frame, text="Deposit", font=("Arial", 14), width=20,
                  command=lambda: self.deposit_amount(amount_entry)).pack(pady=2)
        tk.Button(action_frame, text="Withdraw", font=("Arial", 14), width=20,
                  command=lambda: self.withdraw_amount(amount_entry)).pack(pady=2)
        tk.Button(action_frame, text="View Transactions", font=("Arial", 14), width=20,
                  command=self.show_transactions).pack(pady=2)
        tk.Button(self.customer_frame, text="Logout", font=("Arial", 14), width=20,
                  command=lambda: self.show(self.login_frame)).pack(pady=20)

        self.show(self.customer_frame)

    def show_manager_dashboard(self):
        self.clear_frame(self.manager_frame)
        self.add_header(self.manager_frame)

        info_frame = tk.Frame(self.manager_frame, bg="blue")
        info_frame.pack(pady=20)

        tk.Label(info_frame, text=f"Total Users: {self.bank.get_total_users()}",
                 font=("Arial", 16), fg="white", bg="blue", anchor="w").pack(anchor="w")
        tk.Label(info_frame, text=f"Total Holdings: P{self.bank.get_total_balance():.2f}",
                 font=("Arial", 16, "bold"), fg="white", bg="blue", anchor="w").pack(anchor="w", pady=(0, 10))

        action_frame = tk.Frame(self.manager_frame, bg="blue")
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Create Customer", font=("Arial", 14), width=25,
                  command=self.create_user_ui).pack(pady=5)
        tk.Button(action_frame, text="Logout", font=("Arial", 14), width=25,
                  command=lambda: self.show(self.login_frame)).pack(pady=5)

        self.show(self.manager_frame)

    def create_user_ui(self):
        self.clear_frame(self.manager_frame)
        self.add_header(self.manager_frame)

        form_frame = tk.Frame(self.manager_frame, bg="blue")
        form_frame.pack(pady=30)

        tk.Label(form_frame, text="Create New Customer", font=("Arial", 20), fg="white", bg="blue").pack(pady=10)
        tk.Label(form_frame, text="Account Holder Name:", font=("Arial", 14), fg="white", bg="blue").pack()
        entry_name = tk.Entry(form_frame, font=("Arial", 14))
        entry_name.pack(pady=10)

        def do_create():
            name = entry_name.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Enter a name.")
                return
            result = self.current_account.create_account(name, self.bank)
            messagebox.showinfo("Account Created", f"Account Number: {result['account_number']}\nPIN: {result['pin']}")
            self.show_manager_dashboard()

        tk.Button(form_frame, text="Create Account", font=("Arial", 14), width=25, command=do_create).pack(pady=5)
        tk.Button(form_frame, text="Back", font=("Arial", 14), width=25, command=self.show_manager_dashboard).pack(pady=5)

    def deposit_amount(self, entry):
        amount_str = entry.get().strip()
        if not amount_str:
            messagebox.showwarning("Input Error", "Input deposit amount.")
            return
        try:
            amount = float(amount_str)
            self.current_account.deposit(amount)
            self.bank.save_data()
            messagebox.showinfo("Success", "Amount deposited.")
            self.show_customer_dashboard()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def withdraw_amount(self, entry):
        amount_str = entry.get().strip()
        if not amount_str:
            messagebox.showwarning("Input Error", "Input withdraw amount.")
            return
        try:
            amount = float(amount_str)
            self.current_account.withdraw(amount)
            self.bank.save_data()
            messagebox.showinfo("Success", "Amount withdrawn.")
            self.show_customer_dashboard()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def show_transactions(self):
        history = self.current_account.get_transactions()
        if not history:
            messagebox.showinfo("Transactions", "No transactions yet.")
            return
        history_text = "\n".join(history)
        messagebox.showinfo("Transaction History", history_text)


    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SBSGUI(root)
    root.mainloop()
