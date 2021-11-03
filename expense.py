from PyInquirer import prompt
import csv


lst = []

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": lst
    }

]

def fill_file(infos):
    f = open('expense_report.csv', 'r')
    nb_lines = 0
    while(f.readline()):
        nb_lines += 1
    with open('expense_report.csv', 'a+', newline='') as csvfile:
        fieldnames = ['amount', 'label', 'spender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if (nb_lines == 0) :
            print("pass here")
            writer.writeheader()
        writer.writerow(infos)

def new_expense(*args):
    f = open('users.csv', 'r').readlines()
    for elt in f:
        lst.append(elt.strip())
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    fill_file(infos)
    #adding infos to expense file
    
    print("Expense Added !")
    return True
