from PyInquirer import prompt
import csv

lst = []
lst2 = []

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
    },
    {
        'type': 'checkbox',
        'name': 'involved',
        'message': 'People involved in the expense',
        'choices': lst2,
        'validate': lambda answer: 'You must choose at least one person.' \
            if len(answer) == 0 else True
    }
]

def fill_file(infos):
    f = open('expense_report.csv', 'r')
    nb_lines = 0
    while(f.readline()):
        nb_lines += 1
    with open('expense_report.csv', 'a+', newline='') as csvfile:
        fieldnames = ['amount', 'label', 'spender', 'involved']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if (nb_lines == 0) :
            writer.writeheader()
        writer.writerow(infos)

def new_expense(*args):
    f = open('users.csv', 'r').readlines()
    for elt in f:
        lst.append(elt.strip())
        lst2.append({'name': elt.strip(), 'checked': True})
    infos = prompt(expense_questions)
    print(infos)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    fill_file(infos)
    #adding infos to expense file
    
    print("Expense Added !")
    return True
