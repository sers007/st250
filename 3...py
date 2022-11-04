import random

brands_of_car = {
 "BMW":{"fuel": 100," strength":100, "consumption": 6},
"Lada":{"fuel": 50, "strength":40, "consumption": 10},
 "Volvo":{"fuel" :70, "strength":150,  "consumption": 8},
 "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
}



class Human:
     def __init__(self, name="Human", job=None, home=None,
     car=None):
         self.name = name
         self.money = 100
         self.gladness = 50
         self.satiety = 50
         self.job = job
         self.car = car
         self.home = home





class Auto:
         def __init__(self, brand_list):
             self.brand = random.choice(list (brand_ list))
             self.fuel = brand_list[self.brand]["fuel"]
             self.strength = brand_list[self.brand] ["strength"]
             self.consumption = brand_list[self.brand]["consumption"]


def drive(self):
    if  self.strength > 0 andself.fuel  >=  self.consumption:
        self.fuel -= self.consumption
        self.strength -= 1
        return True
    else:
    print("The car cannot move")
    return False
