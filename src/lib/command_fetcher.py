import abc, six

@six.add_metaclass(abc.ABCMeta)
class CommandFetcher():

    @abc.abstractmethod
    def getCommand():
        pass


class FileMode(CommandFetcher):
    """
    FileMode users commands are in stored in file.
    """
    def getCommand(self):
        """Get All commands from FileMode."""
        import sys
        file_name = sys.argv[1]
        file = open(file_name, 'r')
        line = file.readline()
        while line:
            yield line
            line = file.readline()


class InteractiveMode(CommandFetcher):
    """
    InteractiveMode in which user input command in Std Input.
    """

    def getCommand(self):
        """Get All commands from InteractiveMode."""
        while True:
            yield raw_input()


def getCommandMode(args_len):
    """
    Return mode of input.

    @args args_len len of arguments
    @returns Objects of FileMode or InteractiveMode
    """
    if args_len == 1:
        return InteractiveMode()
    elif args_len == 2:
        return FileMode()
    else:
        raise Exception("Unknown Mode")
