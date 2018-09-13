import sys


class CommandGenerator():
    """
    retrun set of commands
    """

    def __init__(self):
        self.command_line = False
        if len(sys.argv) == 2:
            self.command_line = True
            self.file_name = sys.argv[1]

    def _get_command_from_file(self):
        file = open(self.file_name, 'r')
        line = file.readline()
        while line:
            yield line
            line = file.readline()

    def _get_command_from_interactive(self):
        while True:
            yield raw_input()

    def get_command(self):
        """
        Return Commands
        """
        if self.command_line:
            return self._get_command_from_file()
        return self._get_command_from_interactive()
