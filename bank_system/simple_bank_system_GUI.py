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

    def setup_login_ui(self):
        header = tk.Frame(self.login_frame, bg="blue")
        header.place(x=20, y=20)
        tk.Label(header, text="SBS", font=("Arial", 40, "bold"), fg="white", bg="blue").pack(anchor="w")
        tk.Label(header, text="Simple Bank System", font=("Arial", 16), fg="white", bg="blue").pack(anchor="w")

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
        if self.current_role == "customer":
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
            acc_no = self.entry_user.get()
            pin = self.entry_pin.get()
            account = self.bank.get_account(acc_no, pin)

            if account:
                self.current_account = account
                if hasattr(account, "get_balance"):
                    self.show_customer_dashboard()
                else:
                    self.show_manager_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid credentials.")

    def show_customer_dashboard(self):
        self.clear_frame(self.customer_frame)
        tk.Label(self.customer_frame, text=f"Welcome, {self.current_account._account_holder}",
                 font=("Arial", 24), fg="white", bg="blue").pack(pady=10)
        tk.Label(self.customer_frame, text=f"Balance: P{self.current_account.get_balance():.2f}",
                 font=("Arial", 16), fg="white", bg="blue").pack(pady=10)

        amount_entry = tk.Entry(self.customer_frame, font=("Arial", 14))
        amount_entry.pack(pady=10)

        tk.Button(self.customer_frame, text="Deposit", font=("Arial", 14), command=lambda: self.deposit_amount(amount_entry)).pack()
        tk.Button(self.customer_frame, text="Withdraw", font=("Arial", 14), command=lambda: self.withdraw_amount(amount_entry)).pack()
        tk.Button(self.customer_frame, text="Logout", font=("Arial", 14), command=lambda: self.show(self.login_frame)).pack(pady=20)
        self.show(self.customer_frame)

    def show_manager_dashboard(self):
        self.clear_frame(self.manager_frame)
        total_users = self.bank.get_total_users()
        total_balance = self.bank.get_total_balance()
        tk.Label(self.manager_frame, text=f"Total Users: {total_users}", font=("Arial", 20), fg="white", bg="blue").pack(pady=10)
        tk.Label(self.manager_frame, text=f"Total Holdings: P{total_balance:.2f}", font=("Arial", 20), fg="white", bg="blue").pack(pady=10)
        tk.Button(self.manager_frame, text="Logout", font=("Arial", 14), command=lambda: self.show(self.login_frame)).pack(pady=20)
        self.show(self.manager_frame)

    def deposit_amount(self, entry):
        try:
            amount = float(entry.get())
            self.current_account.deposit(amount)
            self.bank.save_data()
            messagebox.showinfo("Success", "Amount deposited.")
            self.show_customer_dashboard()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def withdraw_amount(self, entry):
        try:
            amount = float(entry.get())
            self.current_account.withdraw(amount)
            self.bank.save_data()
            messagebox.showinfo("Success", "Amount withdrawn.")
            self.show_customer_dashboard()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SBSGUI(root)
    root.mainloop()
