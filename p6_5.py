class BuldingError(Exception):
    def __str__(self):
        return f"Wifh so much material the house cannot built!"


def check_material(material1,limit):
    if material1 >= limit:
        print("Go")
    else:
        raise BuldingError()


material = 400
limits = 450

check_material(material,limits)