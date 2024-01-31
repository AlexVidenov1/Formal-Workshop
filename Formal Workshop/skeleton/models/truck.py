from vehicle import Vehicle
class Truck(Vehicle):
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file

    
    def __init__(self, make, model, price, weight):
        super().__init__(make, model, wheels=Truck.WHEELS_COUNT, price=price)
        self.weight = weight        

    def validate(self):
        super().validate()
        if self.weight < Truck.WEIGHT_CAP_MIN or self.weight > Truck.WEIGHT_CAP_MAX:
            raise ValueError(Truck.WEIGHT_CAP_ERR)
        
    