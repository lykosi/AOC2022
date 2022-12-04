class RockPaperScissors(object):
    def __init__(self, guide):
        self.parse(guide)


    def parse(self, guide):
        result = 0
        for rounds in guide.split("\n"):
            result += self.switch(rounds.split( ))
        print("The result of all rounds is:", result)
        return
        
    def switch(self, value):
        score = 0
        if value[0] == "A": #Rock
            score += self.switch_rock(value[1])
        elif value[0] == "B": #Paper
            score += self.switch_paper(value[1])
        elif value[0] == "C": #Scissors
            score += self.switch_scissors(value[1])
        return score

    def switch_scissors(self, value):
        if value == "Y": #Paper (2) - Draw
            return 6 #2
        elif value == "X": #Rock (1) - Lose
            return 2 #7
        elif value == "Z": #Scissors (3) - Win
            return 7 #6

    def switch_rock(self, value):
        if value == "Y": #Paper (2) - Draw
            return 4 #8
        elif value == "X": #Rock (1) - Lose
            return 3 #4
        elif value == "Z": #Scissors (3) - Win
            return 8 #3

    def switch_paper(self, value):
        if value == "Y": #Paper (2) - Draw
            return 5 #5
        elif value == "X": #Rock (1) - Lose
            return 1 #1
        elif value == "Z": #Scissors (3) - Win
            return 9 #9
        





