import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file if not exists
def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

# Add expense
def add_expense():
    date = datetime.now().strftime("%d-%m-%Y")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!\n")

# View expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

# Total expense
def total_expense():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"💵 Total Expense: {total}\n")

# Category-wise expense
def category_expense():
    category_total = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            category_total[category] = category_total.get(category, 0) + amount

    print("📊 Category-wise Expenses:")
    for cat, amt in category_total.items():
        print(f"{cat}: {amt}")
    print()

# Main menu
def main():
    create_file()
    while True:
        print("---- Expense Tracker ----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_expense()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice\n")

if __name__ == "__main__":
    main()
