import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Die:
    """
    A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
    value (int): The number of spots on the side facing up.
    points (int): The number of points the die is worth.
    """
# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """
        Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        """
        Generates a new random value and calculates the points.
                
        Args:
            self (Die): An instance of Die.
            """
        self.value = random.randint(1, 6)
        if self.value == 5:
            self.points = 50
        elif self.value == 1:
            self.points = 100
        else:
            self.points = 0

        print(f'points: {self.points}')