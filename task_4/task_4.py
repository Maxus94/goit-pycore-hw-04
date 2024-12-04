def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return " "    

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except:
        return "Wrong data, must be \nName number"

def change_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "Wrong data, must be \nName number"
    if contacts.get(name):
        contacts[name] = phone
    else: 
        return "Contact doesn't exist"
    return "Contact Updated."

def show_contact(args, contacts):
    name = args[0]    
    try:
        resp = contacts[name] 
        return resp
    except:
        return "Contact doesn't exist"

def show_all(contacts):        
    resp = ""
    for contact in contacts:
        resp = resp + contact + " phone " + contacts[contact] + "\n"
    if resp == "":
        return "There is no any contact"
    return resp
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
