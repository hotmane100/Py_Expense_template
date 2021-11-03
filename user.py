from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    f = open('users.csv', 'a', newline='')
    f.write(infos['name']+'\n')
    return True