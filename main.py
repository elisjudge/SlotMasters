MIN_BET = 1
MAX_BET = 100
MAX_LINES = 3

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")
    
    return amount


def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line (${MIN_BET} - ${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet amount must be at least the minimum bet and no greater than the maximum bet.")
        else:
            print("Please enter a valid amount.")
    
    return bet


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds to place this bet, your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} over {lines} lines. Your total bet is ${bet * lines}.")


if __name__ == "__main__":
    main()
