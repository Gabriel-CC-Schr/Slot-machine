MAX_Lines = 3
MAX_Bet = 100
MIN_Bet = 1

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


main()