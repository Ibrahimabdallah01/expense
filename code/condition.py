# Simple expressions

# available_tickets = int(input("Enter availabe ticket: "))
# sold_ticket = int(input("Enter available ticket: "))
# enough = available_tickets > sold_ticket
# print(enough)

# available_ticket = int(input("Number of available tickets: "))
# buy_more = available_ticket < 75 or available_ticket > 500
# print(f"Ticket warning: {buy_more}")

# genre = input("Enter music game: ")
# if genre == "rock":
#     print("AC/DC")
# else:
#     print("Eminem")


# password = input("Enter a password to login again: ")

# if password != "12345":
#     print("Incorect password")
# else:
#     print("welcom back to your account")


# Quiz 
# Create a discount program
# Ask the user which type of trip they are taking
# Ask the user for an expected trip cost
# If the trip is a business trip and the price is 1200 or over return True
# Print i the customer get a discount or not (True or false)

# type_of_trip = input("Enter type of trip (business/personal): ")
# trip_cost = float(input("Enter a trip cost: "))

# discount = type_of_trip == "business" and trip_cost >= 1200

# print(f"Discount trip is: {discount}")



# Quiz 
# Create a program that recommendeds a type of trip
# Gather the trip cost from user
# If the cost is less than 350, tell them to go on stay-cation
# If the cost is over/equal to 350 and less than 1000, tell them to go on road trip
# If the cost is over 1000, tell them to catch a flight to the beach
# NOTE no matter the answer, print have fun! at the end of the program

trip_cost = int(input("Enter trip cost: "))

if trip_cost <= 350:
    print("Stay-cation")
elif 350 <= trip_cost < 1000:
    print("go on road trip")
else:
    print("catch a flight")