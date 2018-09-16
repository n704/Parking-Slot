import six
from car import Car

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

@six.add_metaclass(Singleton)
class ParkingLot(object):
    """
    ParkingLot class which gives all the
    """
    def __init__(self):
        self.size = 0
        self.slots = []

    def _find_free_slot(self):
        for i in range(self.size):
            if self.slots[i] == None:
                return i
        return -1

    def create_slot(self, size):
        try:
            size = int(size)
        except ValueError as e:
            raise Exception("Size need to be Integer: {0}".format(size))
        self.slots = [None for i in range(size)]
        self.size = size
        print "Created a parking lot with {0} slots".format(size)


    def park_a_car(self, registration_number, color):
        free_slot = self._find_free_slot()
        if free_slot == -1:
            return "Sorry, parking lot is full"
        if not (len(registration_number) and len(color)):
            raise Exception("vehicale information cannot be empty.\n")
        oCar = Car(registration_number.strip(), color.strip())
        self.slots[free_slot] = oCar
        return "Allocated slot number: {0}".format(free_slot+1)

    def car_is_leaving(self, slot_number):
        """
        Car is leaving from slot.

        @slot_number Allocated slot of the car.
        """
        try:
            slot_number = int(slot_number)
        except ValueError as e:
            raise Exception("Slot number should be Integer.\n")
        if slot_number <= 0:
            raise Exception("Slot number should be greater than zero.\n")
        elif slot_number > len(self.slots):
            raise Exception("Slot number does not exist in parking lot.\n")
        self.slots[slot_number - 1] = None
        return "Slot number {0} is free".format(slot_number)

    def status_of_parking_lot(self):
        """
        Display all car in parking lot
        """
        header = "Slot No.    Registration No    Colour"
        data = [header]
        for i in range(self.size):
            if self.slots[i]:
                data.append("{0}           {1}      {2}".format(
                    i+1,
                    self.slots[i].registration_number.strip(),
                    self.slots[i].color.strip()))
        output_string = "\n".join(data)
        return output_string

    def registration_numbers_for_cars_with_colour(self, color):
        """
        Display all car in parking slots with color
        """
        cars_with_color = [car.registration_number for car in self.slots if car and car.color.lower().strip() == color.lower().strip()]
        if cars_with_color:
            return ', '.join(cars_with_color)
        return "Not found"

    def slot_numbers_for_cars_with_colour(self, color):
        """
        Return slot number of cars with color
        """
        slot_of_cars = [ str(i+1) for i in range(self.size) if self.slots[i] and self.slots[i].color.lower().strip() == color.lower().strip()]
        if slot_of_cars:
            return ', '.join(slot_of_cars)
        return "Not found"

    def slot_number_for_registration_number(self, registration_number):
        """
        Return Slot of car with registration_number
        """
        slot = [i + 1 for i in range(self.size) if self.slots[i] and self.slots[i].registration_number.strip() == registration_number.strip()]
        if slot:
            return str(slot[0])
        return "Not found"
