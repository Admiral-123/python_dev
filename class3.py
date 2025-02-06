class Food:
    def __init__(self, name, calorie, fat, carbs, protein):
        self.name = name
        self.calorie = calorie
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def isHealthy(self):
        if self.fat > 20 or self.carbs > 50:
            return False
        else:
            return True
    


Pizza = Food("pizza", 840, 40, 100, 33)
apple = Food("pizza", 50, 10, 15, 2)

val = Pizza.isHealthy()
print(val)

print(apple.isHealthy())

        
    
