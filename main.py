class Car:
    def __init__(self, make, model, generation, vin_number):
        self.make = make
        self.model = model
        self.generation = generation
        self.vin_number = vin_number

    def check_model_vin(self, number):
        if self.vin_number == number:
            print(f'Твой VIN номер {number} валидный')
        else:
            print(f'Твой VIN номер {number} не валидный')

car = Car( 'Renault', 'Espace', 'V', '390218310938')

car.check_model_vin('390218310938')
