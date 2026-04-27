from ATM_Project.logic import ATMSession

def main():
    atm = ATMSession()  # Create an instance of our ATM logic
    
    while True:
        print("\n--- ATM MENU ---")
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Statement")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            print(f"Current Balance: {atm.get_balance()}")
            
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            success, message = atm.withdraw(amt)
            print(message)
            
        elif choice == '3':
            amt = float(input("Enter amount to deposit: "))
            success, message = atm.deposit(amt)
            print(message)
            
        elif choice == '4':
            print("\n--- Transaction History ---")
            for record in atm.get_statement():
                print(record)
                
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()