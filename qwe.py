import random

class Hero:
    def __init__(self):
        self.__power = 25
        print("Перс на месте")

    def buff(self,value):
        self.__power += value

    def power(self):
        return self.__power

class Artefact:
    def __init__(self):
        self.__power = random.randint(10,80)
        print("Здесь артефакт с силой", self.__power)

    def power(self):
        return self.__power

class Monster:
    def __init__(self):
        self.__power = random.randint(5,100)
        print("в комнате монстр")
    
    def power(self):
        return self.__power

hero = Hero()
artefact = Artefact()
monster = Monster()
levels = [random.randint(0,1) for i in range(10)]
rand=random.randint(0,1)

for i in range(10):
    rand=random.randint(0,1)
    door=int(input('в какую дверь вы войдете'))
    if rand==1:
        hero.buff(artefact.power())
        print('вы нашли артефакт, удача на ващей стороне')
    else:
        if hero.power() >= monster.power():
            print('в непредсказуемой схватке вы стали победителем')
        else:
            print('увы, вы проиграли')
            exit()
print('вы победили')