# from turtle import *

# # Create red turtle
# red_turtle = Turtle()
# red_turtle.color("red")
# red_turtle.forward(100)  # Move forward

# # Create purple turtle
# purple_turtle = Turtle()
# purple_turtle.color("purple")
# purple_turtle.penup()  # Lift pen so it doesn't draw
# purple_turtle.goto(-100, 0)  # Move to a different starting position
# purple_turtle.pendown()  # Put pen down to draw
# purple_turtle.forward(100)

# # Create orange turtle
# orange_turtle = Turtle()
# orange_turtle.color("orange")
# orange_turtle.penup()
# orange_turtle.goto(0, -100)  # Another different position
# orange_turtle.pendown()
# orange_turtle.circle(50)  # Draw a circle

# # Keeps the window open
# done()

name = input("Enter your name: ")
sex = input("Enter your sex: ")
profession = input("Enter your profession: ")


class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print("Name:", self.name, "Sex:", self.sex, "Profession:", self.profession)

    def work(self):
        print("Name:", self.name, "works as", self.profession)


# Create an instance of the Person class
# ibrahim = Person("Ibrahim", "male", "software engineer")
person = Person(name, sex, profession)

# Call the methods
person.show()
person.work()
