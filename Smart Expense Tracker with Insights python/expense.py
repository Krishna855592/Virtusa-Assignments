from datetime import datetime

class Expense:
    def __init__(self,date_input,category,amount,description):

        if isinstance(date_input,str):
            self.date=date_input
        else:
            #coming from user input
            self.date=date_input.strftime("%Y-%m-%d")  # storing date as yyyy-mm-dd format
        
        self.category = category.strip().title()
        self.amount = amount
        self.description = description
    def get_month(self):
        return int(self.date[5:7])
    def get_year(self):
        return int(self.date[:4])
    

    def to_list(self):
        return [self.date,self.category,str(self.amount),self.description]