import random
class Student:
    def __init__(self, name: object) -> object:
        self.name = name
        self.gladness = 10
        self.progress = 0
        self.maney = 400
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 6
        self.maney += 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 6
        self.maney -= 4
    def to_chill(self):
        print("Rest time")
        self.gladness += 6
        self.progress -= 0.01
        self.maney -= 5
    def to_job(self):
        print("Time to job")
        self.maney += 1
        self.progress +=0.05
        self.gladness -=0.09

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress >= 19:
            print("Passed externally…")
            self.alive = False
        elif  self.maney <= 0:
            print("died of hunger")
            self.alive = False


    def end_of_day(self) -> object:

        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")
        print(f"Maney  = {self.maney}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_job()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
     break
    nick.live(day)
