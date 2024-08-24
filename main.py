import hashlib
import json
import datetime

def login():
    # Get input from the user
    id = input("Enter ID (must be 10 digits): ")
    password = input("Enter Password: ")
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    
    with open('schedule.json', 'r') as file:
        data = json.load(file)
        
    # Read user data from file
    for account in data['accounts']:
        if(id == account['id'] and hash_value == account['password']):
            print(f"Login successful! Welcome, user ID: {id}")
            return 1# Exit the function after successful login
        else:
            print("Invalid ID or password.")  # ID not found or password mismatch
            return 0

    return 0

def create_account():
    
    try:
        with open('schedule.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'accounts': []}  # Create an empty list if the file does not exist
    
    while True:
        id = input("Enter new ID (must be 10 digits): ")
        if len(id) == 10 and id.isdigit():
            password = input("Enter new Password: ")
            hash_value = hashlib.sha256(password.encode()).hexdigest()
            profession = input("Enter Profession: ")
            break
        
    # Read user data from file
    for account in data['accounts']:
        if(id == account['id'] or hash_value == account['password']):
            print("ID or password already used")
            return
        
    with open('schedule.json', 'w') as f:
        new_account = {'id': id, 'password': hash_value, 'profession': profession}
        data['accounts'].append(new_account)
        json.dump(data, f, indent=3)
    
    print(f"Account created successfully!")
    return


# Call the login function

def creating_date():
    print("Creating date")
    return


while True:
    year = int(input("Pick the year: "))
    month = int(input("Pick the month: "))
    day = int(input("Pick the day: "))
    hour = int(input("Pick the hour: "))
    minute = int(input("Pick the minute: "))
    beginDate = datetime.datetime(year, month, day, hour, minute)
    if(beginDate > datetime.datetime.today()):
        break
    else:
        print("date cannot be before today")
    endDate = dt + datetime.timedelta(hours = 2)
    date = [dt, endDate]
    for citas in date:
        print(citas)


choice = input("Do you want to login or create an account? (login/create): ")
if choice.lower() == "login":
    if login() == 1:
        while True:
            choice2 = input("Do you want to add date or exit? (date/exit): ")
            if choice2.lower() == "date":
                creating_date()
            elif choice2.lower() == "exit":
                break
            else:
                print("Invalid choice.")
elif choice.lower() == "create":
    create_account()
else:
    print("Invalid choice.")