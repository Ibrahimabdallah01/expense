# username = input("Enter your username: ")
# invald = "!@#';_=+()[{}]\/``.,"

# for letter in username:
#     if letter in invald:
#         print("This character is not allowed: ", letter)


# for i in range(5):
#     number = input("Enter a number: ")
#     print("Number added:", number)
# print("All 5 numbers added!")


# passenger = int(input("How many passenger? "))

# for i in range(passenger):
#     lastName = input("Enter last name: ")
#     print("Hello,", lastName)
# print("Passenger Manifest Updated")


# A user has 5 changes to login into an account
# Their username is 'admin' and their password is '12345'
# Print off how  many tries is took them to login in
# If they enter wrong 5 times, print off 'You are not Admin'

# username = input("Enter username: ")
# invald = "./,;'[=-+\|~!@#%$^&*()]"
 
# for letter in username:
#     if letter in invald:
#         print("This character is not allowed:", letter)


username = "admin"
password = 12345
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    input_username = input("Enter user name: ")
    input_password = input("Enter password: ")
    attempts += 1
    
    if input_username == username and input_password == password:
        print(f"Login successful. It took you {attempts} tries.")
        break
    else:
        print("Incorect Creadential try again")

if attempts == max_attempts and (input_username != username | input_password != password):
    print("Your Not Admin")