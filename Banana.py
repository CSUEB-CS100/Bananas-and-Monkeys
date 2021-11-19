CALS_PER_GRAM = 1.2


class Banana:
    def __init__(self, color, weight):
        self.__color = color
        self.__weight = weight    #grams

    def getColor(self):
        return self.__color

    def getWeight(self):
        return self.__weight

    def getCalories(self):
        calories = self.__weight * CALS_PER_GRAM
        return calories

    def rippen(self):
        if (self.__color == 'green'):
            self.__color = 'yellow'
        elif (self.__color == 'yellow'):
            self.__color = 'brown'
        elif (self.__color == 'brown'):
            self.__color = 'brown'



if __name__ == '__main__':
    ripe_banana = Banana('yellow', 75)

    print(ripe_banana.getColor())
    print(ripe_banana.getWeight())

    young_banana = Banana('green', 50)

    print(young_banana.getColor())
    print(young_banana.getWeight())

    bad_banana = Banana('brown', 80)

    print(bad_banana.getColor())
    print(bad_banana.getWeight())

    print("rippen yellow banana ")
    ripe_banana.rippen()
    print(ripe_banana.getColor())