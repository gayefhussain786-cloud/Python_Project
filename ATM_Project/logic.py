class ATMSession:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.transactions = [f"Initial Balance: {initial_balance}"]

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False, "Insufficient funds!"
        if amount <= 0:
            return False, "Invalid amount!"
        
        self.balance -= amount  # Make sure this is exactly -=
        self.transactions.append(f"Withdrew: {amount}")
        return True, f"Successfully withdrew {amount}"

    def deposit(self, amount):
        if amount <= 0:
            return False, "Invalid deposit amount!"
        
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return True, f"Successfully deposited {amount}"

    def get_statement(self):
        return self.transactions 