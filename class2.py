from queue import Full


class Cricket:
    def __init__(self, wickets, runs, overs, innings, target):
        self.wickets = wickets
        self.runs = runs
        self.overs = overs
        self.innings = innings
        self.target = target

    def currentScore(self):
        print(self.runs, "-", self.wickets)
        print("overs - ", self.overs)
        if(self.innings == 1):
            print("innings - ",self.innings)
            print("")
        else:
            print("innings - ",self.innings)
            print(self.target)
    
    
game1 = Cricket(3, 167, 29.4, 1, Full)  # Full means pass
game2 = Cricket(5, 210, 48.4, 2, 229)

game1.currentScore()
game2.currentScore()