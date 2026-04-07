class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    #create 2 objects of the class Car
car1 = Car("Toyota","Red")
car2 = Car("Lambo","green")

print('Car 1 brand:', car1.brand)
print('Car 1 color:', car1.color)
print('Car 2 brand:', car2.brand)
print('Car 2 color:', car2.color)