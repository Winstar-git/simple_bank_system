# Simple Bank System

Welcome to the **Simple Bank System**!  
This is a Python project with a modern Tkinter GUI that simulates a basic banking system. It allows customers to manage their savings accounts and managers to oversee the bank's operations. The project is designed as a practical demonstration of the **four pillars of Object-Oriented Programming (OOP)**: **Encapsulation, Inheritance, Polymorphism, and Abstraction**.

---

## Features

- **Customer Login**: Secure login using account number and PIN.
- **Account Management**: Deposit, withdraw, and view transaction history.
- **Manager Login**: Special login for managers to view total users, total holdings, and create new customer accounts.
- **Persistent Data**: All account data is stored in a JSON file for persistence.
- **User-Friendly GUI**: Clean, organized interface with clear feedback and error handling.

---

## How to Run

1. Make sure you have Python 3 installed.
2. Install Tkinter if not already included (`pip install tk` or use your Python distribution).
3. Place all `.py` files and `bank_data.json` in the correct folders as shown in the project structure.
4. Run the main GUI:
   ```
   python bank_system/simple_bank_system_GUI.py
   ```

---

## Project Structure

```
simple_bank_system/
│
├── bank_system/
│   ├── account.py
│   ├── savings_account.py
│   ├── manager_account.py
│   ├── bank.py
│   ├── simple_bank_system_GUI.py
│   └── bank_data.json
└── README.md
```

---

## The Four Pillars of OOP in This Project

### 1. **Encapsulation**
- **What:** Bundling data and methods that operate on that data within one unit (class), restricting direct access to some of the object's components.
- **How:**  
  - All account data (number, holder, pin, balance, transactions) are private or protected attributes (e.g., `_account_number`, `_balance`).
  - Access and modification are only possible through methods like `deposit`, `withdraw`, `get_balance`, and `verify_pin`.
  - The GUI interacts with accounts only through these public methods, never directly with the data.

### 2. **Inheritance**
- **What:** Mechanism where a new class inherits properties and behavior from an existing class.
- **How:**  
  - `Account` is an abstract base class.
  - `SavingsAccount` and `ManagerAccount` both inherit from `Account`, reusing and extending its functionality.
  - This allows for shared logic (like PIN verification and transaction history) and specialized behavior for each account type.

### 3. **Polymorphism**
- **What:** The ability to present the same interface for different underlying forms (data types).
- **How:**  
  - Both `SavingsAccount` and `ManagerAccount` implement the `deposit` and `withdraw` methods, but with different logic (or pass for manager).
  - The `Bank` and GUI code can treat all accounts as `Account` objects and call these methods without knowing the specific subclass.
  - The `get_account` method returns either a `SavingsAccount` or `ManagerAccount`, and the rest of the system works seamlessly.

### 4. **Abstraction**
- **What:** Hiding complex implementation details and showing only the necessary features of an object.
- **How:**  
  - The `Account` class is abstract and defines the required interface for all account types.
  - Users of the `Account` class (like the GUI or `Bank`) don't need to know how deposit/withdraw are implemented, just that they exist.
  - The GUI provides a simple interface for users, abstracting away the data storage and business logic.

---

## Example Accounts

You can use these credentials to log in as a customer or manager (see `bank_data.json`):

- **Customer:**  
  - Account Number: `100001`  
  - PIN: `1111`

- **Manager:**  
  - Account Number: `999999`  
  - PIN: `0000`


## Screenshots

![Loading Screen](simple_bank_system\screenshot\Loading_Screen.png)
![Login Screen](simple_bank_system\screenshot\User_login.png)
![Login Screen](simple_bank_system\screenshot\Manager_login.png)
![Customer Dashboard](simple_bank_system\screenshot\User_dashboard.png)
![Customer Transaction History](simple_bank_system\screenshot\Transaction_history.png)
![Manager Dashboard](simple_bank_system\screenshot\Manager_dashboard.png)
![Creating Account](simple_bank_system\screenshot\Creating_account.png)
```
## Why This Project is Interesting

- **Educational:** Demonstrates OOP principles in a real-world scenario.
- **Practical:** Shows how to build a GUI application with persistent data and user roles.
- **Extendable:** You can easily add new account types, features, or improve the interface.

