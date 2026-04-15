from datetime import datetime

def show_menu():
    print("\n ==== smart expense tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Summary")
    print("4. Category Breakdown")
    print("5. Highest Spending Category")
    print("6. Show pie chart")
    print("7. spending insights")
    print("8. Exit")
    

def get_user_choice():
    choice=input("enter your choice: ")
    return choice.strip()

def get_valid_date():
    while True:
        date_str= input("enter date (yyyy-mm-dd): ").strip()
        try:
            date_obj=datetime.strptime(date_str,"%Y-%m-%d")
            return date_obj
        except ValueError:
            print("invalid date format. please enter in yyyy-mm-dd format")

def get_valid_amount():
    while True:
        try:
            amount=float(input("enter amount:"))
            if amount<=0:
                print("amount must be positive")
            else:
                return amount
        except ValueError:
            print("please enter a valid number")

def get_non_empty_input(message):
    while True:
        value=input(message).strip()
        if value == "":
            print("This field cannot be empty")
        else:
            return value

def get_expense_input():
    print("\n enter expense details: ")

    date_obj=get_valid_date()
    category=get_non_empty_input("category: Food, Travel, Bills, etc: ")
    amount=get_valid_amount()
    description=   get_non_empty_input("enter description: ")

    return date_obj,category,amount,description





    