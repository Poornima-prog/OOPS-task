# class: Vehicle
class Vehicle:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate

    def calculate_rental(self, duration):
        return self.rate * duration


# Car
class Car(Vehicle):
    def __init__(self, model, rate, car_type):
        super().__init__(model, rate)
        self.car_type = car_type

    def calculate_rental(self, duration):
        return super().calculate_rental(duration) * 1.2  # Cars have a 20% additional charge


# Bike
class Bike(Vehicle):
    def __init__(self, model, rate, bike_type):
        super().__init__(model, rate)
        self.bike_type = bike_type

    def calculate_rental(self, duration):
        return super().calculate_rental(duration)  # No additional charge for bikes


# Truck
class Truck(Vehicle):
    def __init__(self, model, rate, load_capacity):
        super().__init__(model, rate)
        self.load_capacity = load_capacity

    def calculate_rental(self, duration):
        return super().calculate_rental(duration) * 1.5  # Trucks have a 50% additional charge


car = Car("Sedan", 100, "Luxury")
bike = Bike("Mountain Bike", 20, "Sport")
truck = Truck("Pickup", 150, 1000)

print(f"Car Rental for 3 days: {car.calculate_rental(3)}")
print(f"Bike Rental for 3 days: {bike.calculate_rental(3)}")
print(f"Truck Rental for 3 days: {truck.calculate_rental(3)}")
