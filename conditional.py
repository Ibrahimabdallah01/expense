# available_tickets = int(input("Number of available ticket: "))
# sold_tickets = int(input("Ticket sold: "))

# total = available_tickets % sold_tickets
# print(total)


# music = input("Enter type of music: ")

# if music == "bongo flavor":
#     print("tanzania music")
# else:
#     print("Unknown music")


# password = input("Enter your password: ")

# if password != "12345":
#     print("Incorrect password try again")
# else:
#     print("Welcome back to your account")


# Quiz 1
# Create a discount program
# Ask the user which type of trip they taking
# Ask the user for an expected trip cost
# If the trip is business trip and price is 1200 or over return True
# Print if the customer get a discount or not (True or False)

# trip_type = input("Is your trip Business/Leisure or Person? ").lower()
# price = int(input("Expected trip cost: "))

# discount = trip_type == "business" and price >= 2000

# print("Customer receives a discount", discount)


# Quiz 2
# Allow a user to enter a special discount code
# If the discount code is equal to winter23 then give 20% discount
# Otherwise say code is not valid

# code = input("Enter your code here: ")

# if code == "winter23":
#     print("You get 20% discount")
# else:
#     print("Your code is invald")


# Quiz 3
# Create a program that recommends a type of trip
# Gather the trip cost from user
# If the cost is less than 350, tell them to go on a stay-cation
# If the cost is over/equal to 350 and less than 1000 tell them to go on a road trip
# If the cost is over 1000, tell them to catch a flight to the beach
# NOTE no matter the answer, print Have Fun! at the end of your program

# cost = int(input("Enter your trip funds: "))

# if cost < 350:
#     print("Go on stay-cation")
# if cost >= 350 and cost < 1000:
#     print("Go on road trip")
# if cost > 1000:
#     print("Catch a flight to beach")

# print("Have fun")


# Quiz 2
# Create a program that gather bag weight in kg and also either domestic/international from user

# If the weight is less than or equal to 18 kg then the price is 2500
# otherwise the price is 750

# Then check if the destination is domestic or international
# If it's domestic, add 300 to the price
# Otherwise add 7500 to the price
# Print off the estimated cost

# NOTE what is the price variable?

bag_weight = int(input("Enter the bag weight: "))
destination = input("Enter a destination is domestic or international?: ")

if bag_weight <= 18:
    price = 2500
else:
    price = 750

if destination == "domestic":
    price = price + 300
elif destination == "international":
    price += 750
else:
    print("Spelling error")

print("Ticket price: ", price)
