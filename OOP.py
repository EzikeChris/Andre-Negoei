# //////   OBJECT OREINTED PROGRAMMING ////


# //// OOP MEANING and  WHAT IT ENTAILS /////


# ////  A PARADIGM OOP MEANS A WAY FOR US TO STRUCTURE OUR CODE

# ////  ONCE WORKS GET BIGGER WE CAN STRUCTURE OUR CODE OR ORGANISE OUR CODE SO IT DOSENT BECOME CHAOS OR CUMBERSOME                       #

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('cindy', 50)
player4 = PlayerCharacter('Jonatham', 60)
player4.indomie = 30


print(player1.name)
print(player4.name, 30)


class KeyBoard:
    def __init__(self, type,):
        self.type = type

    def run(self):
        print('run')


samsung = KeyBoard('compact')

print(samsung.type)
