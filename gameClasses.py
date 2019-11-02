import random

class Game:
    # Defining the class variables
    possibleSigns = [
        "rock",
        "paper",
        "scissors"
    ]
    score = {
        "pc": 0,
        "player": 0
    }
    totalRounds = 0
    completedRounds = 0

    def __init__(self):
        self.score = {
            "pc": 0,
            "player": 0
        }
        self.totalRounds = 0
        self.completedRounds = 0

        return self

    def incrementScore(self, name):
        # normalizing the input
        name = name.strip().casefold()

        # validating the input
        if name in ["player", "pc"]:
            return ValueError("{} is not a valid argument for the incrementScore function.".format(name))

        currentScore = self.score[name]
        newScore = currentScore + 1

        self.score[name] = newScore
        self.completedRounds = self.completedRounds+1
    
    def generateSign(self):
        mySign = random.choice(self.possibleSigns)
        return mySign
    
    def evaluateResponse(self, pcSign, playerSign):
        pass

    def evaluateResponseInner(self, pcSign, playerSign):
        pass






    
    

