from diceclass import dice_c


class dice_director:
    # the dice directs game.

    def __init__(self):
        # Constructs a new Director.

        self.dice = []
        self.playing = True
        self._score = 0
        self.total_score = 0

        for x in range(5):
            di = dice_c()
            self.dice.append(di)

    def initialize(self):
        # Starts the game by running the main game loop.

        while self.playing:
            self.dice_input()
            self.dice_update()
            self.dice_output()

    def dice_input(self):
        # The user if they want to roll.

        roll_dice = input("Roll dice? [y/n] ")
        self.playing = (roll_dice == "y")

    def dice_update(self):
        # Updates the player's score.

        if not self.playing:
            return

        for x in range(len(self.dice)):
            di = self.dice[x]
            di.roll_dice()
            self._score += di.points
        self.total_score += self._score

    def dice_output(self):
        # Displays the dice and the score.
        # The player if they want to roll dice again.

        if not self.playing:
            return

        values = ""
        for x in range(len(self.dice)):
            di = self.dice[x]
            values += f"{di.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.playing == (self._score > 0)
