from Game_Project import game_logic

def main():
    while True:
        print("\n--- Stone-Paper-Scissors ---")
        print("1. Play Round")
        print("2. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            user_move = input("Enter Stone, Paper, or Scissors: ").capitalize()
            if user_move not in ['Stone', 'Paper', 'Scissors']:
                print("Invalid input!")
                continue
                
            comp_move = game_logic.get_computer_choice()
            print(f"Computer chose: {comp_move}")
            
            result = game_logic.determine_winner(user_move, comp_move)
            print(result)
            
        elif choice == '2':
            break

if __name__ == "__main__":
    main()