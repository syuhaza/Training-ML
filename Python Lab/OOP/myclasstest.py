import random

class Pokemon:

    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self):
        print("Pokemon move")

    def doEat(self):
        print("Pokemon eat")


class Jigglepuff(Pokemon):

    def __init__(self, name, health, element, lungcapacity):
        super().__init__(name, health, element)
        self.lungcapacity = lungcapacity

    def doMove(self):
        super().doMove()
        print("Jigglypuff can float")

    def __str__(self):
        message = f"Name: {self.name}\n"
        message += f"Health: {self.health}\n"
        message += f"Element:  {self.element}"
        message += f"Capacity: {self.lungcapacity}"
        return message

class Pikachu(Pokemon):

    def __init__(self, name, health, element, electricity):
        super().__init__(name,health, element)
        self.electricity = electricity

class Game:
    
    def __init__(self):
        
        self.elements = ["Thunder", "fire","water","ghost","ice"]
        self.pokemons = {
        "Jigglepuff":[Jigglepuff(f"J{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements) -1)], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
        "Pikachu":[Pikachu(f"P{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements)-1)], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]


        }
    def __str__(self):
        message = ""
        for pokemonname, pokemonlist in self.pokemons.items():
            for pokemon in pokemonlist:
                message += pokemon.__str__() + "\n" + ("-"*20) + "\n"
        return message

        

pokemon = Jigglepuff("Wigglepuff", "Good", "Fairy","Big capacity")
pokemon.doMove()
print(pokemon)

game = Game()
print(game)