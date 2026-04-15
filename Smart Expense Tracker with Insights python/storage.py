import csv
import os
from expense import Expense

FILE_NAME="data.csv"

#creating a file if file doesn't exist and also adding header to the file

def initialize_file():
    #if file doesn't exist create with header
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Description"])
        return
    #if file exists but header is missing add it
    with open(FILE_NAME,mode='r') as file:
        first_line=file.readline().strip()
    
    if first_line!="Date,Category,Amount,Description":
        with open(FILE_NAME,'r') as file:
            data=file.readlines()
        with open(FILE_NAME, 'w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["Date","Category","Amount","Description"])

            for line in data:
                file.write(line)


def save_expense(expense):
    with open(FILE_NAME,mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(expense.to_list())

# now writing a method to get all the expenses from the file
def get_all_expenses():
    expenses=[]
    with open(FILE_NAME,mode='r') as file:
        reader=csv.reader(file)
        header=next(reader,None)

        if header and header[0]!="Date":
            if(len(header)==4):
                date,category,amount,description=header
                expense=Expense(date,category,float(amount),description)
                expenses.append(expense)
        for row in reader:
            if len(row)!=4:
                continue
            date,category,amount,description=row
            expense=Expense(date,category,float(amount),description)
            expenses.append(expense)
    return expenses

        

    # if not os.path.exists(FILE_NAME):
    #     return expenses
    # with open(FILE_NAME,mode='r') as file:
    #     reader=csv.reader(file)
    #     #now skipping the header which we have previously created
    #     next(reader) 

    #     try:
    #         next(reader)
    #     except StopIteration:
    #         return expenses

    #     for row in reader:
    #         if len(row)!=4:
    #             continue
    #         date,category,amount,description=row
    #         expense=Expense(date,category,float(amount),description)
    #         expenses.append(expense)
    # return expenses
        