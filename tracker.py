💸 Python Expense Tracker

A lightweight, efficient command-line / graphical tool developed during my internship at Decode Labs (Project 02). This application allows users to seamlessly track, categorize, and analyze their daily expenses to manage their personal finances effectively.

✨ Features

• Expense Logging: Quickly add daily expenses with details like amount, category, and date.
• Smart Categorization: Group expenses into clear categories (e.g., Food, Transport, Entertainment, Bills).
• Summary & Insights: View total spending over custom timeframes (daily, weekly, or monthly summaries).
• Data Persistence: Automatically saves your financial records to a local file (JSON or CSV), ensuring your data is kept safe between sessions.
• Clean Interface: Designed with a user-friendly CLI (Command Line Interface) / GUI for effortless data entry.

🚀 Tech Stack

• Language: Python 3.x
• Data Storage: JSON / CSV modules
• Libraries Used: Standard libraries (or mention packages like Pandas / Tkinter / Matplotlib if used)

🛠️ Setup & Installation

1. Clone the repository:bash
git clone https://github.com
cd python-expense-tracker
Use code with caution.
2. Run the application:bash
python expense_tracker.py
Use code with caution.

📂 Project Structure

text
python-expense-tracker/
│
├── expense_tracker.py     # Main application logic
├── expenses.json          # Data storage file (generated automatically)
└── README.md              # Project documentation
Use code with caution.

🤝 Acknowledgments

Special thanks to Decode Labs for the mentorship, guidance, and structured learning path during this internship program.

📄 License

This project is open-source and available under the MIT License.
If you want me to update this file to look exactly like your code, let me know:
• Is your project a CLI (Command Line) app, or did you build a GUI (like Tkinter)?
• Does it generate visual graphs or charts using libraries like Matplotlib?
• Where does it save data (JSON, CSV, or a Database like SQLite)?





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
