from abc import ABC, abstractmethod # lib for interface

class Vehicle(ABC): # "OOP Interface"
    def __init__(self) -> None:
        super().__init__()
    def start_engine(self): # all vehicles have the same, choose for all and we do not define them separately
        return "turned with key"
    @abstractmethod
    def move(self):
        return
    @abstractmethod
    def sound(self):
        return


class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    def move(self):
        return "pedal treaded"
    def sound(self):
        return "wrummmm"

class Boat(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    def move(self):
        return "waveeeee"
    def sound(self):
        return "suuummmm"
    
class MotorBike(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    def move(self):
        return "turned with hand"
    def sound(self):
        return "wrm wrm"

my_car = Car()
my_boat = Boat()
my_motor_bike = MotorBike()
all_vehicles = [my_car, my_boat, my_motor_bike]
interface_functions = ["start_engine", "move", "sound"] # all classes have
for one in all_vehicles:
    for one2 in interface_functions:
        func = getattr(one, one2) # get function with name
        print(func())