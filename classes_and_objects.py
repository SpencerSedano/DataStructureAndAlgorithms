class Robot:
    def __init__(self, name, color, weight, looking):
        self.name = name
        self.color = color
        self.weight = weight
        self.looking = looking

    #Self-Introduction
    def intro(self):
        print(f'Hello, this is {self.name}, and my favorite color is {self.color} and my weight is {self.weight}')


robot_one = Robot("Spencer", "blue", "75kg", "")
robot_two = Robot("Carlitos", "white", "10kg", "")

robot_one.looking = robot_two
robot_two.looking = robot_one

robot_one.intro()
robot_two.intro()