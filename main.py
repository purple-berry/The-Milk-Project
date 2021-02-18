import time
import random
import start
from start import inventory, run
# Most important
# import json

class cat():

    valid_food = ["cooked chicken", "cooked beef", "cooked pork", "cat food"]
    valid_drinks = ["milk", "water", "cat juice"]

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 100
        self.thirst = 100
        self.energy = 100
        self.alive = True

    def alert(self):
        if self.hunger <= 15:
            print(f"Your cat is so hungry, it's almost {100 - self.hunger}% hungry.")
        if self.thirst <= 15:
            print(f"Your cat is so thirsty, it's almost {100 - self.thirst}% thirsty.")
        if self.energy <= 15:
            print(f"Your cat is so weak and has no energy. {100 - self.energy}% is left.")

    def speak(self):
        speak_time = random.randint(2, 600)
        time.sleep(speak_time)
        print(f"{self.name}: Meow!")

    def hungry(self):
        number = random.randint(1, 2000000000000000000000000)
        reducer = random.randint(1, 15)
        if number == 2:
            self.hunger -= reducer

    def thirsty(self):
        number = random.randint(1, 2000000000000000000000000)
        reducer = random.randint(1, 15)
        if number == 2:
            self.thirst -= reducer

    def feed(self, food):
        if food in __class__.valid_food:
            if food in inventory:
                self.hunger = 100
                self.thirst += random.randint(0, 10)
                self.energy += random.randint(5, 45)
                print("It ate it and burped a bit...")
            else:
                print("It seems that you don't have enough to feed.")
        else:
            print("Are you serious on giving this as food to your cat?")

    def drink(self, drink):
        if drink in __class__.valid_drinks:
            if drink in inventory:
                self.thirst = 100
                self.energy += random.randint(3, 15)
                print("It just drank it and it's feeling better...")
            else:
                print("You don't have it though, buy it first.")
        else:
            print("It can't drink that!")

    def play(self, game):
        if game == "jump n run":
            game_type = 10
            start.score += 15
        elif game == "ring the cat":
            game_type = 23
            start.score += 30
        elif game == "pointer me":
            game_type = 39
            start.score += 40
        elif game == "swim in water":
            game_type = 80
            start.score += 100

        self.energy -= game_type

    def is_dead(self):
        if self.hunger <= 0:
            print("Ohhh, noooo, Your cat died due to hunger. You could have fed it properly!")
        elif self.thirst <= 0:
            print("Oh no! Your cat died due to thirsty, why, why didn't you make it drink. Huh?")
        elif self.energy <= 0:
            print("Noooooo!!! Your, your cat died, due o lack of energy. Nooooooooo, nooo noon no no no no no!!!!!...")

my_cat = cat(start.cat_name)
run = True

def start_the_cat():
    while run:
        # my_cat.speak()
        my_cat.hungry()
        my_cat.thirsty()
        my_cat.alert()
        my_cat.is_dead()

start_the_cat()
