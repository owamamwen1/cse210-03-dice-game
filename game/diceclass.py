import random

# The file content one class an two methods


class dice_c:
    # The different number of spots on each of its six sides.
    def __init__(self):
        # Constructs a new instance

        self.value = 0
        self.points = 0

    def roll_dice(self):
        # Generates a new random value.

        self.value = random.randint(1, 6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0
