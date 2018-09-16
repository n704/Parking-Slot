from .invoker import Command
from lib.parking_lot import ParkingLot

class StatusCommand(Command):
    """
    Status Command
    """
    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.status_of_parking_lot()


class UNKNOWNCommand(Command):
    """
    Status Command
    """
    def execute(self):
        """
        Execute Command
        """
        print "UNKNOWN"

class CreateParkingCommand(Command):
    """
    Create PArking
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        parking_lot.create_slot(*command_words)

class ParkingCommand(Command):
    """
    Parking a car
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.park_a_car(*command_words)


class LeaveCarCommand(Command):
    """
    Leave PArking
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.car_is_leaving(*command_words)


class RegCarWithColorCommand(Command):
    """
    registration_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.registration_numbers_for_cars_with_colour(*command_words)


class SlotNumWithColorCommand(Command):
    """
    slot_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.slot_numbers_for_cars_with_colour(*command_words)



class SlotNumWithRegNumCommand(Command):
    """
    slot_number_for_registration_number
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        print parking_lot.slot_number_for_registration_number(*command_words)
