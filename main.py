import argparse
import json
import time
import calendar
import pprint
import datetime

parser = argparse.ArgumentParser(description="Example CLI using argparse")
parser.add_argument('-add', type=str, help="add an expense")
parser.add_argument('-list', type=str, help="Show a list of expenses")
parser.add_argument('-summary', type=str, help="Show a list the total amount of expenses")
parser.add_argument('-delete', type=int, help="delete an expense")
parser.add_argument('--description', type=str, help="add a description")
parser.add_argument('--amount', type=float, help="add an amount")
expense = parser.parse_args()

# Open the file ----------------------------------------------------------------------------------------------------------------------------
def return_file():
    try:
        with open("expenses.json", "r") as task_file:
            content = task_file.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: invalid JSON format")
        return []
# ------------------------------------------------------------------------------------------------------------------------------------------

def expenseAdd():
    try:
        data = return_file()
        lines = len(data)
        for i in data:
            if data[i]["ID"] == lines:
                lines +=1
        if lines == 0:
            lines = 1    
        expenseDict = {
            "Expense{ID}".format(ID = lines):
            {
            "ID": lines,
            "Description": expense.description,
            "Amount": expense.amount,
            "Date": time.strftime("%D %T")
            }
        }
        ExpenseOutput = data | expenseDict
        with open("expenses.json", "w") as outfile:
            json.dump(ExpenseOutput, outfile, indent=4)
            outfile.close()
        
        print(F"Expense added successfully (ID: {lines})")
    except: 
        print("an error occurred")

def expenseDelete():
    try:
        data = return_file()
        for i in data:
            
            if data[i]["ID"] == expense.delete:
                dataToDelete = i
        data.pop(dataToDelete)
        with open("expenses.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
            outfile.close()
    except: 
        print("Error while deleting an expense")

def expenseList():
    try:
        data = return_file()
        print("\n".join("{}\t{}".format(k, v) for k, v in data.items()))
    except: 
        print("An error occurred")

def expenseSummary():
    try:
        data=return_file()
        totalExpenses = 0.0
        if(expense.month):
            print("test")
        else:
            for i in data:
                totalExpenses += data[i]["Amount"]
            print(F" Total expenses: ${totalExpenses}")
    except: 
        print("An error occurred")



if(expense.add):
    expenseAdd()
if(expense.delete):
    expenseDelete()
if(expense.list):
    expenseList()
if(expense.summary):
    expenseSummary()


def testFunction():
    data = return_file()
    month = data["Expense3"]["Date"]
    date = datetime(month)
    print(date)

testFunction()