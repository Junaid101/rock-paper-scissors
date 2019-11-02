import random


class Game:
    # Defining the class variables
    playerNames = ["pc", "player"]

    possibleSigns = [
        "rock",
        "paper",
        "scissors"
    ]

    score = {playerName: 0 for playerName in playerNames}
    totalRounds = 0
    completedRounds = 0
    signHierarchy = {
        # In the format "A" sign beats ["B","C"] signs
        # Also make it possible to extend this for more number of signs
        # and other winner-loser relationships

        "rock": ["scissors"],
        "scissors": ["paper"],
        "paper": ["rock"]

        # Possible improvement, make each sign a class
    }

    def __init__(self, rounds=5):
        self.score = {
            "pc": 0,
            "player": 0
        }
        self.totalRounds = rounds
        self.completedRounds = 0
        print("Game Started")

    def incrementScore(self, name):
        # computing scores
        if name == "draw":
            # updating the completed round count without changing score
            self.completedRounds = self.completedRounds + 1
        else:
            # updating the completed round count and changing score        
            currentScore = self.score[name]
            newScore = currentScore + 1
            self.score[name] = newScore
            self.completedRounds = self.completedRounds + 1        
        return True

    def generateSign(self):
        mySign: str = random.choice(self.possibleSigns)
        return mySign

    # def getFirstTurn(self):
    #     return random.choice(self.playerNames)

    def evaluateRoundWinner(self, pcSign, playerSign):
        winner = self.signComparison(pcSign, playerSign)
        self.incrementScore(winner)
        return winner

    def signComparison(self, pcSign, playerSign):
        if playerSign == pcSign:
            return "draw"
        elif playerSign in self.signHierarchy[pcSign]:
            return "pc"
        else:
            return "player"

    def endGame(self):
        # say who the winner is

        # print closing statement
        print("Game Over")

    def prettyRepr(self):
        representation = [
            "A game of rock-paper-scissors" +
            "\n" +
            "{0} out of a total of {1} rounds have been completed".format(self.completedRounds, self.totalRounds) +
            "\n" +
            "The currect score is {}".format(str(self.score))
        ]
        return "".join(representation)
    
    def __repr__(self):
        representation = [
            "A game of rock-paper-scissors" +
            "The currect score is {}".format(str(self.score))
        ]
        return "".join(representation)


def main():
    print("\n\n Welcome to a game of rock papers scissors")
    print("We are going to start it with a default of 5 rounds")

    # Initiate a new game
    runningGame = Game()

    # First round is from the player
    print("First turn is yours")

    for _ in range(runningGame.totalRounds):
        try:

            while True:
                print("It is round {}".format(runningGame.completedRounds+1))
                print("Please choose from {}".format(runningGame.possibleSigns))
                playerSign = input().strip().casefold()
                if playerSign in runningGame.possibleSigns:
                    break                    
                print ("Invalid sign, restarting round.")
                
            pcSign = runningGame.generateSign()
            print(
                "Your AI opponent has generated the following response --> {}".format(pcSign))
            roundWinner = runningGame.evaluateRoundWinner(pcSign, playerSign)
            print("The winner of this round is {}".format(roundWinner))
        except Exception as e:
            e.__suppress_context__=False
            print("There was a problem\n{}".format(e))

while True:
    main()