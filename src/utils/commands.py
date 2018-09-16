from .invoker import Command
from lib.commands import *

class StatusCommand(Command):
    """
    Status Command
    """
    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        status_parking_lot(command_words, parking_lot)


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
        create_parking_lot(command_words)

class ParkingCommand(Command):
    """
    Parking a car
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        park_a_car(command_words, parking_lot)


class LeaveCarCommand(Command):
    """
    Leave PArking
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        leave_parking_lot(command_words, parking_lot)


class RegCarWithColorCommand(Command):
    """
    registration_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        reg_car_with_color(command_words, parking_lot)


class SlotNumWithColorCommand(Command):
    """
    slot_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        slots_with_color(command_words, parking_lot)



class SlotNumWithRegNumCommand(Command):
    """
    slot_number_for_registration_number
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        parking_lot = ParkingLot()
        slots_with_reg_number(command_words, parking_lot)
