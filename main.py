def login():
    # Get input from the user
    id = input("Enter ID (must be 10 digits): ")
    # Check if the ID is exactly 10 digits and consists of only digits
    if len(id) == 10 and id.isdigit():
        password = input("Enter Password: ")
        hash_value = hash(password)
        profession = input("Enter Profession: ")
        return id, hash_value, profession
    else:
        print("Invalid ID. Please enter 10 digits.")

def create_account():
  while True:
    id = input("Enter new ID (must be 10 digits): ")
    if len(id) == 10 and id.isdigit():
        break
    else:
        print("Invalid ID. Please enter 10 digits.")
        
    password = input("Enter new Password: ")
    hash_value = hash(password)
    profession = input("Enter Profession: ")
  return id, hash_value, profession

# Call the login function
"""
Asks the user if they want to login or create an account.
"""
choice = input("Do you want to login or create an account? (login/create): ")
if choice.lower() == "login":
    user_data = login()
    if user_data is not None:
        id, hashed_password, profession = user_data
        print(f"Login successful! Welcome, user ID: {id}")
    else:
        print("Login failed due to invalid ID.")
elif choice.lower() == "create":
    user_data = create_account()
    id, hashed_password, profession = user_data
    print(f"Account created successfully! User ID: {id}")
else:
    print("Invalid choice.")
  
  
  
