# password = input("Enter a password to login: ")

# while password != "password123":
#     print("Wrong password")
#     password = input("Try again: ")
# print("Welcome to your account")


# cost = int(input("Enter the cost of an item (0 to end): "))
# total = 0

# while cost != 0:
#     total += cost
#     cost = int(input("Enter the cost of an item (0 to end): "))
# print("Grand Total: ", total)
# total = total * 0.50
# print("Total price with discount: ", total)


# Using counter to track
# test_answer = input("Enter a, b, c or d: ")
# tries = 1

# while test_answer != "c":
#     tries += 1
#     print("Wrong answer")
#     test_answer = input("Please now be careful when you answer: ")
# print("It took you", tries, "tries to get the answer")


# Quiz
# Create a mini bolt that accepts message
# The loop only breaks/end once the word 'done' is entered
# Every time the loop runs we got your message

# message = input("Enter a message (type done to end): ")

# while message != "done":
#     print("We got your message")
#     message = input("Enter a message (type done to end): ")
# print("Thank you, We go your message")


# Quiz 2
# Create an account login
# The user has 2 passwords, either one can entered to gain access
# Once the user enters the correct password, great them with 'Welcome to your account'

password1 = input("Enter your first password to get access in admin panel: ")

while password1 != "12345" and password1 != "123456":
    password1 = input("try another password to get access: ")
print("Welcome to your account")
