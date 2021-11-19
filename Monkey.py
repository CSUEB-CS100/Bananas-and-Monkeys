from Banana import Banana

class Monkey:
    def __init__(self):
        self.__name = "No Name"
        self.__energy = 500 # calories

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getEnergy(self):
        return self.__energy

    def swingFromTrees(self):
        self.__energy = self.__energy - 100

    def isHungry(self):
        return self.__energy < 250

    def eatBanana(self, banana):
        if banana.getColor() == 'yellow':
            self.__energy = self.__energy + banana.getCalories()

    def __str__(self):
        message = f"{self.__name} has {self.__energy} energy left"
        return message


if __name__ == '__main__':

    bobo = Monkey()
    bobo.setName('Bobo')
    print(bobo.getName())

    print(bobo.getEnergy())
    bobo.swingFromTrees()
    bobo.swingFromTrees()
    bobo.swingFromTrees()

    print(bobo)

    print(bobo.getEnergy())
    if bobo.isHungry():
        print("Bobo is hungry")
    else:
        print("He's fine")

    young_banana = Banana('green', 79)

    bobo.eatBanana(young_banana)

    if bobo.isHungry():
        print("Bobo is hungry")
    else:
        print("He's fine")

    young_banana.rippen()

    bobo.eatBanana(young_banana)

    if bobo.isHungry():
        print("Bobo is hungry")
    else:
        print("He's fine")

