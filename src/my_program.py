#!/usr/bin/python

import sys
from constant import (
    COMMAND_INPUT_PREFIX, COMMAND_OUTPUT_PREFIX,
    FILE_INPUT_PREFIX, FILE_OUTPUT_PREFIX,
    COMMANDS, STATUS_COMMAND
)
from lib.command_fetcher import getCommandMode
from lib.command import generator

if __name__ == "__main__":
    args_len = len(sys.argv)
    command_mode = getCommandMode(args_len)
    for command in command_mode.getCommand():
        words = command.split(' ')
        command_executer = generator(words[0])
        if command_executer:
            command_executer.execute()
        else:
            raise Exception("Unknown Command")
