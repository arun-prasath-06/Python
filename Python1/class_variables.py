class car:
    wheels=4

    def __init__(self,brand):
        self.brand=brand
car1 = car("Toyata")
car2 = car("Honda")

print(car1.wheels)
print(car2.wheels)