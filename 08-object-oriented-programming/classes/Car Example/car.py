class Car:
    def __init__(self, make, model, year,color,milage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage

    def car_name(self):
        return (f"You are driving {self.make}'s car ")

    def car_year(self):
        return (f"You are driving {self.year}'s car ")

    def car_color(self):
        return (f"You are driving {self.color}'s car ")

    def car_milage(self):
        return (f"You are driving {self.milage}'s car ")

