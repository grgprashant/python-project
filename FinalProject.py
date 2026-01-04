#To check the strength of a password
def check_password_strength(password):
    length =len(password)

    has_upper=False
    has_lower=False
    has_digit=False
    has_symbol=False


    symbols="!@#$%^&*()_=+-<>?"
    for ch in password:
        if ch.isupper():
         has_upper=True
        elif ch.islower():
         has_lower=True
        elif ch.isdigit():
            has_digit=True      
        elif ch in symbols:
            has_symbol=True     
        score=0
    if length>=8:
     score +=1
    if has_upper:
        score +=1       
    if has_lower:
        score +=1
    if has_digit:
        score +=1   
    if has_symbol:
        score +=1   
    if score==5:
        print("Very Strong")
    elif score==4:
        print("Strong")                
    elif score==3:    
        print("Moderate")
    elif score==2:          
        print("Weak")
    else:       
        print("Very Weak") 

password=input("Enter your password: ")    
check_password_strength(password)

#To simulate a secure login system
def login():
   print("\n-Create Account-")
   username = input("Create username: ")
   password = input("Create password: ")

   print("\n Account Created Successfully!")
   print("\n-Login-")
   u = input("Enter username: ")
   p = input("Enter password: ")
   if u==username and p==password:
         print("Login Successful")
   else:
         print("Login Failed")
    
while True:
    print("\n--- Main Menu ---")
    print("1. Check Password Strength")
    print("2. Secure Login System")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        pwd = input("Enter your password: ")
        check_password_strength(pwd)
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    

