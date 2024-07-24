import random

MAX_Lines = 3
MAX_Bet = 100
MIN_Bet = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 10,
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        columns = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(value)

        columns.append(columns)
    
    return columns

def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(columns[row], end="")

        print()



def desposit():
    while True: 
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(" Amount must be greater than 0")
        else:
            print("Please enter a valid amount")

    return amount

def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_Lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_Lines:
                break
            else:
                print("Enter a number between 1 and " + str(MAX_Lines))
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True: 
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_Bet <= amount <= MAX_Bet:
                break
            else:
                print(f"A bet must be between ${MIN_Bet} - ${MAX_Bet}.")
        else:
            print("Please enter a valid amount")

    return amount



def main():
    balance = desposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to make that bet. You have ${balance} left.")
        else:
            break

    print(f"You are bettinh ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine_spin(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"You won ${winnings}!")
    print(f"You won on line", *winnings_lines)

main()