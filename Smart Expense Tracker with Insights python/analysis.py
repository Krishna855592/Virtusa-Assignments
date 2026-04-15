''' 
    in this file we will calculate the monthly total expenses and category wise spending and 
    highest spending in a particular category and 
    pie chart visualization using matplotlib and spending insights
'''
from collections import defaultdict
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def monthly_summary(expenses,month=None,year=None):
    total=0
    for exp in expenses:
        if month is not None and exp.get_month()!=month:
            continue
        if year is not None and exp.get_year()!=year:
            continue
        total+=exp.amount
        # if exp.get_month()==target_month and exp.get_year()==target_year:
        #     total+=exp.amount
    return total


def category_breakdown(expenses,month=None,year=None):
    category_totals=defaultdict(float)

    for exp in expenses:
        if month is not None and exp.get_month()!=month:
            continue
        if year is not None and exp.get_year()!=year:
            continue
        category_totals[exp.category]+=exp.amount

    return category_totals

def highest_spending_category(expenses,month=None,year=None):
    filtered_expenses=[]

    for exp in expenses:
        if month is not None and exp.get_month()!=month:
            continue
        if year is not None and exp.get_year()!=year:
            continue
        filtered_expenses.append(exp)
    if not filtered_expenses:
        return None,0
    category_totals={}
    for exp in filtered_expenses:
        category_totals[exp.category]=category_totals.get(exp.category,0)+exp.amount
    # category_totals=category_breakdown(expenses,month,year)

    max_category=None
    max_amount=0

    for category,amount in category_totals.items():
        if amount>max_amount:
            max_amount=amount
            max_category=category
    return max_category,max_amount 

def show_pie_chart(expenses,month=None,year=None):

    category_totals=category_breakdown(expenses,month,year)

    if not category_totals:
        print("No Data to display")
        return
    
    labels=list(category_totals.keys())
    values=list(category_totals.values())

    plt.figure()
    plt.pie(values,labels=labels,autopct='%1.1f%%')

    #title should change according to user input
    if month is None and year is None:
        title="catergory wise expense distribution (all records)"
    elif month is not None and year is None:
        title=f"category wise expense distribution for month: {month} (considering all years)"
    elif month is None and year is not None:
        title=f"category wise expense distribution for year: {year}"
    else:
        title=f"category wise expense distribution for month: {month}/{year}"
    plt.title(title)

    plt.savefig("category_wise_breakdown.png")
    plt.close()

    print("Pie chart saved as category_wise_breakdown.png")



#spending insights:
def spending_insights(expenses):
    if not expenses:
        return "No data available for insights"
    
    breakdown=category_breakdown(expenses)

    total=sum(breakdown.values())

    insights=[]

    #finding the highest spend category
    max_category=max(breakdown,key=breakdown.get)
    max_amount=breakdown[max_category]
    percentage=(max_amount/total)*100

    insights.append(f"You spend the most on {max_category} ({percentage:.1f}% ).")

    if percentage>50:
        insights.append(f"⚠ High spending on {max_category}. Try reducing it.")
    
    #top 2 dominance
    sorted_categories=sorted(breakdown.values(),reverse=True)

    if len(sorted_categories)>=2:
        top_two=sorted_categories[0]+sorted_categories[1]
        percent_top_two=(top_two/total)*100

        if percent_top_two>70:
            insights.append(f"⚠ Your top 2 categories dominate your spending (>70%).")
        
    #monthly comparison (basic trend)
    monthly_totals=defaultdict(float)

    for exp in expenses:
        key=(exp.get_year(),exp.get_month())
        monthly_totals[key]+=exp.amount
    if len(monthly_totals)>=2:
        sorted_months=sorted(monthly_totals.keys())

        last=monthly_totals[sorted_months[-1]]
        prev=monthly_totals[sorted_months[-2]]

        if last>prev:
            insights.append(f"⚠ Your spending increased compared to last month.")
        elif last<prev:
            insights.append(f"📉 Good job! your spending decreased from last month")
    return insights



    
    
    
# this is just a simple spending analysis

    # breakdown=category_breakdown(expenses)

    # if not breakdown:
    #     return "No data available for insights"
    
    # #find the highest spending category
    # max_category=max(breakdown,key=breakdown.get)
    # max_amount=breakdown[max_category]

    # total=sum(breakdown.values())

    # percentage=(max_amount/total)*100

    # message =f"you spend the most on {max_category} ({percentage:.1f}% of total)."

    # if percentage>50:
    #     message+="consider reducing spending in this category"
    # else:
    #     message+="you spending is fairly balanced"
    # return message

    