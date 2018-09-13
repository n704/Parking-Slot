import abc, six

class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        while self._commands:
            command = self._commands.pop()
            command.execute()


@six.add_metaclass(abc.ABCMeta)
class Command():
    """
    Declare an interface for executing an operation.
    """

    @abc.abstractmethod
    def execute(self):
        pass




class HelloWorldCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        print "HEllo"
