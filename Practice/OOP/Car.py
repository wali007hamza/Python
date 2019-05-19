from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

    number_of_tires = 4
    base_price = 34000

    def model_make_year(self):
        return "Model:{0}, Make:{1}, Year:{2}".format(self.model, self.make, self.year)

if __name__ == "__main__":
    ford_mustang = Car("Ford", "Mustang", "2017")
    ford_mustang.car_info()