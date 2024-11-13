# password = input("Enter your password to login: ")

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
# print("Enter price with discount: ", total)


# Using a counter to track

# test_answer = input("Enter a, b, c or d: ")
# tryi = 1
# while test_answer != 'c':
#     tryi += 1
#     print("Wrong answer")
#     test_answer = input("Try again: ")
# print(f"It took you {tryi} triesto get an answer")


# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b


# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


# word = ['ibrah', 'ibrahim', 'abdallah']

# for w in word:
#     print(w, len(w))


# def codeblock(x):
#     if x < 0:
#         print('it is negative')
#     elif x == 0:
#         print("it equal to 0")
#     elif x < 5:
#         print("postive but small than 5")
#     else:
#         print("postive larger than 5")
        
# codeblock(10)


# This loop iterates over the numbers from 2 to 9 (inclusive).
for num in range(2, 10):
    # The modulo operator (%) is used to find the remainder of the division of 'num' by 2.
    # If the remainder is 0, the number is even.
    if num % 2 == 0:
        print(f"Found an even number {num}")
    # If the remainder is not 0, the number is odd.
    else:
        print(f"Found an odd number {num}")