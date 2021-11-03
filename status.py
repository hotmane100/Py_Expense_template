
def show_status():
    users = []
    amount = 0
    f = open('users.csv', 'r').readlines()
    for elt in f:
        users.append(elt.strip())
    fd = open('expense_report.csv', 'r').readlines()
    fd.pop(0)
    for elt in fd:
        amount += int(elt.split(',')[0])
    debt = amount/(len(users))
    for user in users:
        print(user + ": " + str(debt) + "€")
    return