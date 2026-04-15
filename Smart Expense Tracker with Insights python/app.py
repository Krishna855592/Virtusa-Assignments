import streamlit as st
from storage import initialize_file,save_expense,get_all_expenses
from expense import Expense
from analysis import monthly_summary,category_breakdown,highest_spending_category,spending_insights
import matplotlib.pyplot as plt
import calendar
import pandas as pd

initialize_file()

st.title("Smart Expense Tracker with Insights")

#creating a sidebar navigation menu
menu= st.sidebar.selectbox(
    "Menu",[
        "Add Expense",
        "View Expenses",
        "Monthly Summary",
        "Category Breakdown",
        "Highest Spending Category",
        "Show Pie Chart",
        "Smart Insights"

    ]
)




#now creating the interface for add expense
if menu=="Add Expense":
    st.header("Add Expense")

    date=st.date_input("Select Date")
    category=st.text_input("Enter Category (e.g., Food, Travel, Bills, etc.)")
    amount=st.number_input("Amount",min_value=0.0)
    description=st.text_input("Description")

    if st.button("Add"):
        expense=Expense(date,category,amount,description)
        save_expense(expense)
        st.success("Expense added successfully!")


#now creating the interface for view expenses
elif menu=="View Expenses":
    st.header("All Expenses")
    expenses=get_all_expenses()

    if not expenses:
        st.info("No expenses found.")
    else:
        #convert data in table format
        data=[]
        for exp in expenses:
            data.append(
                {
                    "Date":exp.date,
                    "Category":exp.category,
                    "Amount":exp.amount,
                    "Description":exp.description
                }
            )
        df=pd.DataFrame(data)

        #show table
        st.dataframe(df,use_container_width=True)

        #optional show total spending
        total=df["Amount"].sum()
        st.success(f"Total Spending: {total}")

        # for exp in expenses:
        #     st.write(f"Date: {exp.date}, Category: {exp.category}, Amount: {exp.amount}, Description: {exp.description}")


#now creating the interface for monthly summary
elif menu=="Monthly Summary":
    st.header("Monthly Summary")

    month=st.selectbox("Select Month",list(range(1,13)))
    year=st.number_input("Enter Year (optional)",step=1)

    expenses=get_all_expenses()

    if st.button("Calculate"):
        year_val=int(year) if year!=0 else None
        total=monthly_summary(expenses,month,year_val)

        if total==0:
            st.warning("No data found")
        else:
            if year_val:
                st.success(f"Total for {calendar.month_name[month]} {year_val}: {total}")
            else:
                st.success(f"Total for {calendar.month_name[month]} (All years): {total}")

#now creating the interface for category breakdown
elif menu=="Category Breakdown":
    st.header("Category Breakdown")

    month=st.text_input("Month (optional)")
    year=st.text_input("Year (optional)")

    month=int(month) if month else None
    year=int(year) if year else None

    expenses=get_all_expenses()
    breakdown=category_breakdown(expenses,month,year)

    if not breakdown:
        st.warning("No data found")
    else:
        for category,amount in breakdown.items():
            st.write(f"{category}: {amount}")

#now creating the interface for highest spending category
elif menu=="Highest Spending Category":
    st.header("Highest Spending Category")

    month=st.text_input("Month (optional)")
    year=st.text_input("Year (optional)")

    month=int(month) if month else None
    year=int(year) if year else None

    expenses=get_all_expenses()
    category,amount=highest_spending_category(expenses,month,year)

    if category is None:
        st.warning("No data Available")
    else:
        st.success(f"Highest Spending Category: {category} ({amount})")

#now creating the interface for pie chart
elif menu=="Show Pie Chart":
    st.header("Expense pie chart")

    month=st.text_input("Month (optional)")
    year=st.text_input("Year (optional)")

    month=int(month) if month else None
    year=int(year) if year else None

    expenses=get_all_expenses()
    breakdown=category_breakdown(expenses,month,year)

    if not breakdown:
        st.warning("No data to display")
    else:
        lables=list(breakdown.keys())
        values=list(breakdown.values())

        fig,ax=plt.subplots()
        ax.pie(values,labels=lables,autopct='%1.1f%%')

        if month and year:
            ax.set_title(f"{calendar.month_name[month]} {year} Expense Distribution")
        elif month:
            ax.set_title(f"{calendar.month_name[month]} (All years) Expense Distribution")
        else:
            ax.set_title("Expense Distribution (All records)")
        st.pyplot(fig)

#now creating the interface for smart insights
elif menu=="Smart Insights":
    st.header("smart spending insights")
    expenses=get_all_expenses()
    insights=spending_insights(expenses)

    if not insights:
        st.info("no data available")
    else:
        for insight in insights:
            st.markdown(f"- {insight}")

    st.info("🔍 tip:Try reducing your top category by 10-20% to save more")

    

