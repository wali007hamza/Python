from abc import ABCMeta, abstractmethod

class Vehicle(object):
    __metaclass__ = ABCMeta

    base_price = 0
    number_of_tires = 0

    def car_info(self):
        print(self.model_make_year(), "{0}, {1}".format(self.base_price, self.number_of_tires))

    @abstractmethod
    def model_make_year(self):
        pass