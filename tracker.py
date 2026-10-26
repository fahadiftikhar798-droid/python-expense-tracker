# Project 2: Expense Tracker - DecodeLabs

def main():
    total = 0.0  # State initialized OUTSIDE the loop - important!
    count = 0

    print("=== Expense Tracker ===")
    print("Enter expense amounts (type 'quit' to stop)\n")

    while True:
        user_input = input(f"Enter expense #{count+1} (or 'quit'): ").strip().lower()

        # THE KILL SWITCH - Sentinel Value
        if user_input == 'quit':
            break

        # Defense: Input validation
        try:
            expense = float(user_input)
            if expense < 0:
                print("Expense can't be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number or 'quit'.")
            continue

        # THE ACCUMULATOR PATTERN - Heartbeat of the ledger
        # State(new) = State(old) + Input
        total += expense
        count += 1
        print(f"Added: ${expense:.2f} | Total so far: ${total:.2f}\n")

    # Final truth
    print("\n-------------------------")
    print(f"Total transactions: {count}")
    print(f"Total Spent: ${total:.2f}")
    print("-------------------------")

if __name__ == "__main__":
    main()
