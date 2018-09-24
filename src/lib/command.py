import abc, six

from constant import (
    CREATE_SLOTS_COMMAND, PARK_COMMAND, LEAVE_COMMAND, STATUS_COMMAND,
    REG_CAR_WITH_COLOR, SLOTS_WITH_COLOR, SLOTS_WIH_REG_NUMBER,
    EXIT_COMMAND
)

@six.add_metaclass(abc.ABCMeta)
class Command():

    @abc.abstractmethod
    def execute():
        pass


class CreateParkingCommand(Command):

    def execute(self, *args):
        """
        """
        print "create parking."



class ParkCommand(Command):

    def execute(self, *args):
        """
        """
        print "park"



class LeaveCommand(Command):

    def execute(self, *args):
        """
        """
        print "leave"


class StatusCommand(Command):

    def execute(self, *args):
        """
        """
        print "status"


class RegCarWithColorCommand(Command):

    def execute(self, *args):
        """
        """
        print "registration_numbers_for_cars_with_colour"


class SlotWithColorCommand(Command):

    def execute(self, *args):
        """
        """
        print "slots with color"


class SlotWithRegNumberCommand(Command):

    def execute(self, *args):
        """
        """
        print "slot with reg number"


class ExitCommand(Command):

    def execute(self, *args):
        """
        """
        print "exit"


def generator(command):
    """Return correct Command based on command."""
    print command.strip()
    if command.strip() == CREATE_SLOTS_COMMAND:
        return CreateParkingCommand()
    elif command.strip() == PARK_COMMAND:
        return ParkCommand()
    elif command.strip() == LEAVE_COMMAND:
        return LeaveCommand()
    elif command.strip() == STATUS_COMMAND:
        return StatusCommand()
    elif command.strip() == REG_CAR_WITH_COLOR:
        return RegCarWithColorCommand()
    elif command.strip() == SLOTS_WITH_COLOR:
        return SlotWithColorCommand()
    elif command.strip() == SLOTS_WIH_REG_NUMBER:
        return SlotWithRegNumberCommand()
    elif command.strip() == EXIT_COMMAND:
        return ExitCommand()
    else:
        return None
