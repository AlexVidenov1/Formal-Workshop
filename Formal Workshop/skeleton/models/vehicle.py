from typing import Any


class Vehicle:
    VEHICLE_MAKE_LEN_MIN = 2
    VEHICLE_MAKE_LEN_MAX = 15
    VEHICLE_MAKE_ERR = f'Make must be between {VEHICLE_MAKE_LEN_MIN} and {VEHICLE_MAKE_LEN_MAX} characters long!'

    VEHICLE_MODEL_LEN_MIN = 1
    VEHICLE_MODEL_LEN_MAX = 15
    VEHICLE_MODEL_LEN_ERR = f'Model must be between {VEHICLE_MODEL_LEN_MIN} and {VEHICLE_MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'


    
    def __init__(self, make, model, wheels, price):

        self.make = make
        self.model = model
        self.price = price
        self.wheels = wheels
        self.comments = []

    def validate(self):
        if not (Vehicle.VEHICLE_MAKE_LEN_MIN <= len(self.make) <= Vehicle.VEHICLE_MAKE_LEN_MAX):
            raise ValueError(Vehicle.VEHICLE_MAKE_ERR)

        if not (Vehicle.VEHICLE_MODEL_LEN_MIN <= len(self.model) <= Vehicle.VEHICLE_MODEL_LEN_MAX):
            raise ValueError(Vehicle.VEHICLE_MODEL_ERR)

        if not (Vehicle.PRICE_MIN <= self.price <= Vehicle.PRICE_MAX):
            raise ValueError(Vehicle.PRICE_ERR)
        
        
        
    
