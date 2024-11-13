# lastName = input("Enter the owner last name: ")
# city = input("Enter the city: ")
# print("The owner in ", city, "is ", lastName)

# username = input("Enter a user name: ")
# password = input("Enter a password to login: ")

# if password == "Ibrahim":
#     print("successful login")
# elif password == "ibrahim":
#     print("successful login")
# else:
#     print("please try another password to login")


# extra = int(input("Price of extra add-on: "))
# total = 1000 + extra
# print("Total price:", total)

# quiz 1
# Create 3 variable to collect info from user
# These variable are first name, Country & city
# print off their information -> ex ibrah live in dar tanzania

# print("'''''''''''''' enter your information''''''''''''''")
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# country = input("Enter your country: ")
# city = input("Enter your city: ")

# print(firstName, lastName, "live in", city, country)


# quiz 2
# Create 2 variable to gather user information
# 1 car rental price for one day, 1 number of days to rent
# Create a total variable to multiply these 2 variable together
# Print out their cost -> total car price: 550

# rental_car = int(input("Enter price of the car in one day: "))
# number_of_day = int(input("Enter number of days: "))

# total = rental_car * number_of_day
# print("The total price is: ", total)

# Create 3 variable for shipping packages
# A user can enter the weight of 3 packages
# Create a variable to add these 3 variable together
# Offer a 20% discount on shipping weight
# Print off total cost for shipment

# shipping_package = float(input("Enter a weight of first shipping package: "))
# shipping_package1 = int(input("Enter a weight of first shipping package1: "))
# shipping_package2 = int(input("Enter a weight of first shipping package2: "))

# total = (shipping_package + shipping_package1 + shipping_package2) * 0.8

# print("The total shipping package is: ", total)


# quiz 3
# create user ID
# Collect their name, age
# Their user ID number is 12345
# Convert everything to a string
# Print off their information

# user_id = 12345
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Your Information is: ")
# print("Your name: ", name)
# print("Your Age ", age)
# print("Your user ID is: ", user_id)


# Quiz 4
# Create an expense tracker
# Collect the Income from the user
# Collect expenses for food, rent other income from user
# Get the total amount left after expenses
# Print off the remaining total

userName = input("Enter your full name: ")
country = input("Enter your country: ")
city = input("Enter your city: ")
food = int(input("Enter food price: "))
rent = int(input("Enter rent price: "))
electricity = int(input("Enter electricity price: "))
water = int(input("Enter water price: "))

total = food + rent + electricity + water
print("Name: ", userName)
print("Country: ", country)
print("City: ", city)
print("Your total price per month:", total)
