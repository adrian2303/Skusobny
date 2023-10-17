class Auto:
    def __init__(self, weight, brand):
        self.weight = weight
        self.brand = brand

    def print(self):
        print("Auto vazi {0} kilogramov a je to auto znacky {1}".format(self.weight, self.brand))


auto1 = Auto(1500, "BMW")
auto2 = Auto(1850, "Mercedes")
auto1.print()
auto2.print()