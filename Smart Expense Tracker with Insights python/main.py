from storage import initialize_file,save_expense,get_all_expenses
from expense import Expense
from utils import show_menu,get_user_choice,get_expense_input
from analysis import monthly_summary,category_breakdown,highest_spending_category,show_pie_chart,spending_insights

def main():
    initialize_file()

    while True:
        show_menu()
        choice=get_user_choice()

        if choice=="1":
            #adding expenses of user
            date_obj,category,amount,description=get_expense_input()
            expense=Expense(date_obj,category,amount,description)
            save_expense(expense)
        elif choice=="2":
            #view all expenses
            expenses=get_all_expenses()
            print("debug:",expenses)
            if not expenses:
                print("no expenses found")
            else:
                print("all expenses: ")
                for exp in expenses:
                    print(exp.date,"|",exp.category,"|",exp.amount,"|",exp.description)
        elif choice=="3":
            #Monthly summary

            expenses=get_all_expenses()

            #month must be entered
            while True:
                month_input=input("enter month (1-12): ").strip()

                if not month_input:
                    print("month is required! please enter a value")
                    continue
                if not month_input.isdigit() :
                    print("invalid month. please enter numbers only")
                    continue
                month=int(month_input)

                if 1<=month<=12:
                    break
                else:
                    print("month value should be between 1 and 12.")

            #year can be optional
            year_input=input("enter year (e.g., 2026) or press enter to skip: ").strip()
            if year_input:
                if year_input.isdigit():
                    year=int(year_input)
                else:
                    print("invalid year input. skipping year filter.")
                    year=None
            else:
                year=None
            

            total=monthly_summary(expenses,month,year)
            if(total==0):
                print("no data found")
            else:
                if year is not None:
                    print(f"Total expenses for month {month}/{year}: {total}")
                else:
                    print(f"Total expenses for month {month}/(all years): {total}")


            
        elif choice=="4":
            #category wise breakdown
            expenses=get_all_expenses()
            month=input("enter month for breakdown (1-12) or press enter to skip: ").strip()
            year=input("enter year for breakdown (e.g., 2026) or press enter to skip: ").strip()
            month=int(month) if month else None
            year=int(year) if year else None
            breakdown=category_breakdown(expenses,month,year)

            print("\ncategory wise spending: ")
            if month is None and year is None:
                print("Showing data for all records")
            elif month is not None and year is None:
                print(f"Showing data for month: {month} (considering all years)")
            elif month is None and year is not None:
                print(f"Showing data for year: {year}")
            else:
                print(f"Showing data for month: {month}/{year}")
            if not breakdown:
                print("no data found")
            
            for category,amount in breakdown.items():
                print(category,":",amount)

        elif choice=="5":
            #highest spending category
            expenses=get_all_expenses()
            month=input("enter month for highest spending category (1-12) or press enter to skip: ").strip()
            year=input("enter year for highest spending category (e.g.2026) or press enter to skip: ").strip()

            month=int(month) if month else None
            year=int(year) if year else None
            

            category,amount=highest_spending_category(expenses,month,year)

            if month is None and year is None:
                print("Showing result for all records")
            elif month is not None and year is None:
                print(f"Showing result for month: {month} (considering all years)")
            elif month is None and year is not None:
                print(f"Showing result for year: {year}")
            else:
                print(f"Showing result for month: {month}/{year}")

            if category is None:
                print("No data available")
            else:
                print(f"Highest spending category: {category} ({amount})")
        
        elif choice=="6":
            #showing pie chart
            expenses=get_all_expenses()
            month=input("enter month for pie chart (1-12) or press enter to skip: ").strip()
            year=input("enter year for pie chart (e.g.2026) or press enter to skip: ").strip()
            month=int(month) if month else None
            year=int(year) if year else None

            #now adding necessary supporting print statements for different filter combinations
            if month is None and year is None:
                print("Showing pie chart for all records")
            elif month is not None and year is None:
                print(f"Showing pie chart for month: {month} (considering all years)")
            elif month is None and year is not None:
                print(f"Showing pie chart for year: {year}")
            else:
                print(f"Showing pie chart for month: {month}/{year}")
            show_pie_chart(expenses,month,year)
        elif choice=="7":
            expenses=get_all_expenses()
            insight=spending_insights(expenses)
            print("\n Smart Insights:")
            for msg in insight:
                print("-",msg)
        
        elif choice=="8":
            print("exiting... goodbye!")
            break
        
        else:
            print("invalid choice. please try again.")
        


if __name__=="__main__":
    main()



    












    

# #temporialy adding
# from storage import initialize_file, save_expense, get_all_expenses
# from expense import Expense

# initialize_file()

# e = Expense("2026-04-08", "Food", 200, "Dinner")
# save_expense(e)

# all_expenses = get_all_expenses()

# for exp in all_expenses:
#     print(exp.date, exp.category, exp.amount, exp.description)

# from analysis import monthly_summary, category_breakdown, highest_spending_category
# from storage import get_all_expenses

# expenses = get_all_expenses()

# print("Total April:", monthly_summary(expenses, "04"))

# print("Category Breakdown:")
# print(category_breakdown(expenses))

# print("Highest Spending:")
# print(highest_spending_category(expenses))