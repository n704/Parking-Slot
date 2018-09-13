from .invoker import Command


class StatusCommand(Command):
    """
    Status Command
    """
    def execute(self, command_words):
        """
        Execute Command
        """
        print "Status", command_words

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
        print ' '.join(command_words)

class ParkingCommand(Command):
    """
    Parking a car
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        print ' '.join(command_words)


class LeaveCarCommand(Command):
    """
    Leave PArking
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        print ' '.join(command_words)


class RegCarWithColorCommand(Command):
    """
    registration_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        print ' '.join(command_words)

class SlotNumWithColorCommand(Command):
    """
    slot_numbers_for_cars_with_colour
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        print ' '.join(command_words)



class SlotNumWithRegNumCommand(Command):
    """
    slot_number_for_registration_number
    """

    def execute(self, command_words):
        """
        Execute Command
        """
        print ' '.join(command_words)
