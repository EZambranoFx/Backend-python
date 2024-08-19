import hashlib

def login():
    # Get input from the user
    id = input("Enter ID (must be 10 digits): ")
    password = input("Enter Password: ")
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    
    # Read user data from file
    with open("accounts.txt", "r") as file:
        for line in file:
            stored_id, stored_hash_value, stored_profession = line.strip().split(",")
            print(stored_hash_value)
            print(hash_value)
            if stored_id == id and stored_hash_value == hash_value:
                print(f"Login successful! Welcome, user ID: {id}")
                return 1# Exit the function after successful login
            else:
                print("Invalid ID or password.")  # ID not found or password mismatch
                return 0
    return 0

def create_account():
    while True:
        id = input("Enter new ID (must be 10 digits): ")
        if len(id) == 10 and id.isdigit():
            password = input("Enter new Password: ")
            hash_value = hashlib.sha256(password.encode()).hexdigest()
            profession = input("Enter Profession: ")
            break
        else:
            print("Invalid ID. Please enter 10 digits.")
        
    with open("accounts.txt", "a") as file:  # Append to the file
        file.write(f"{id},{hash_value},{profession}\n")
    return

# Call the login function
choice = input("Do you want to login or create an account? (login/create): ")
if choice.lower() == "login":
    if login() == 1:
        print(f"Login successful! Welcome")
    else:
        print("Login failed due to invalid ID.")
elif choice.lower() == "create":
    user_data = create_account()
    #id, hashed_password, profession = user_data
    print(f"Account created successfully!")
else:
    print("Invalid choice.")
  
  
  
