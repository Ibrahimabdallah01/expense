# def person_info(name, age, nationality):
#     print("Welcome:", name)
#     print("Your age:", age)
#     print("Your nationality:", nationality)


# # number = int(input("Amount: "))
# for i in range(1):
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     nationality = input("Enter your nationality: ")
#     person_info(name, age, nationality)


# def total_point(game_score):
#     points = 0

#     while game_score != 0:
#         if game_score >= 5 and game_score <= 10:
#             points += 2
#         if game_score >= 10 and game_score <= 20:
#             points += 3
#         game_score = int(input("Enter the game score: "))
#     return points


# score = int(input("Enter the score: "))
# game_points = total_point, score
# print(game_points)


def good_deal(cost):
    if cost >= 50 and cost < 150:
        response = "this is a good deal"
    elif cost >= 150:
        response = "overprice"
    else:
        response = "Cheap, Buy now"
    return response


store = input("Enter Store Name: ")
cost = float(input("Item Cost: "))

res = good_deal(cost)
print(store, "_", res)

if res == "This is a good deal":
    print("Buy before it's too late")
