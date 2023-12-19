class Vehicle():

    def __init__(self,company,model,year,color,type):
        self.company=company
        self.model=model
        self.year=year
        self.color=color
        self.type=type
    
    def move(self):
        print('The Vheicle {} is moved'.format(self.company))
    
    def stop(self):
        print('The Vheicle us stopped')

class Car(Vehicle):
    def display(slef):
        print('this is the car class')

Vcar=Car('Honda','Poile',2020,'Gray','SUV')

print(Vcar.color)
Vcar.move()
