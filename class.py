class Player:
    def __init__(self, name, age, stats):
        self.name = name
        self.age = age
        self.stats = stats

    def statsPrint(self):
        print(self.stats)
    
    def namePrint(self):
        print(self.name)
    
    def agePrint(self):
        print(self.age)
        

o1 = Player("vk", 36, 47.16)

o1.agePrint()

o1.namePrint()

o1.statsPrint()