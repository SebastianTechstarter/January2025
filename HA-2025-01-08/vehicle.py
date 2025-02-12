import math

class Vehicles:
    def __init__(self, vehicle_brand_name, vehicle_model_name, average_consumption_in_l, tank_size):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank_size = tank_size

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

        return 

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven
    
    def max_distance(self):

        return ((self.tank_size / self.consumption) * 100)

    def fill_ins(self):
        return math.ceil(self.km_driven / self.max_distance())


my_vehicle = Vehicles("VW", "Golf", 10, 45)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
print(f"Wir müssen bei {my_vehicle.km_driven} gefahrenen km {my_vehicle.fill_ins()} mal tanken.")