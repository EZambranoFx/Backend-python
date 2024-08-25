import hashlib
import json
import datetime
from _overlapped import NULL

user = NULL

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
            return account['id'] 
        else:
            print("Invalid ID or password.")  # ID not found or password mismatch
            return NULL

    return NULL

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
        new_account = {'id': id, 'password': hash_value, 'profession': profession, 'freeDates': [], 'scheduledDates': []}
        data['accounts'].append(new_account)
        json.dump(data, f, indent=3)
    
    print(f"Account created successfully!")
    return


# Call the login function

def creating_date(id):
    with open('schedule.json', 'r') as file:
        data = json.load(file)
        
    for account in data['accounts']:
        if(id == account['id']):
            #year = int(input("Pick the year: "))
            #month = int(input("Pick the month: "))
            #day = int(input("Pick the day: "))
            hour = int(input("Pick the hour: "))
            minute = int(input("Pick the minute: "))
            beginDate = datetime.datetime(2024, 8, 25, hour, minute)
            if(beginDate > datetime.datetime.today()):
                endDate = beginDate + datetime.timedelta(hours = 2)
                sBeginTime = beginDate.strftime('%Y-%m-%d %H:%M:%S')
                sEndTime = endDate.strftime('%Y-%m-%d %H:%M:%S')
                date = [sBeginTime, sEndTime]
                if (no_colliding_dates(date, account['freeDates']) == 1):
                    print("date creation succeded")
                    account['freeDates'].append(date)
                else:
                    print("failed")
                    return
            else:
                print("date creation failed")
                
    for a in data['accounts']:
        print(a)
               
    with open('schedule.json', 'w') as file:
        json.dump(data, file, indent=3)
    
    print("date creation succeded")
    
    return

def no_colliding_dates(date, occupied):
    for d in date:
        for pares in occupied:
            if (pares[0] <= d and d <= pares[1]):
                print(pares[0], " <= ", d, " <= ", pares[1])
                print("Overlapping dates")
                return 0
    return 1

choice = input("Do you want to login or create an account? (login/create): ")
if choice.lower() == "login":
    user = login()
    if (user != NULL):
        print(user)
        while True:
            choice2 = input("Do you want to add date or exit? (date/exit): ")
            if choice2.lower() == "date":
                creating_date(user)
            elif choice2.lower() == "exit":
                break
            else:
                print("Invalid choice.")
elif choice.lower() == "create":
    create_account()
else:
    print("Invalid choice.")