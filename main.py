import random

MIN_BET = 1
MAX_BET = 100
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

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


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    n_rows = len(columns[0])
    for row in range(n_rows):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()  


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

    slots = get_slot_machine_spin(rows=ROWS, cols=COLS, symbols=symbol_count)
    print_slot_machine(slots)


if __name__ == "__main__":
    main()
