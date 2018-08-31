#!/usr/bin/python

import sys
from constant import (
    COMMAND_INPUT_PREFIX, COMMAND_OUTPUT_PREFIX,
    FILE_INPUT_PREFIX, FILE_OUTPUT_PREFIX,
    COMMANDS, STATUS_COMMAND
)

if __name__ == "__main__":
    is_command_line = False
    if len(sys.argv) == 2:
        is_command_line = True
    if is_command_line:
        file = open(sys.argv[1], 'r')
        func_to_execute = file.readline
    else:
        def func_to_execute():
            return raw_input(COMMAND_INPUT_PREFIX)
    line = func_to_execute()
    parking_lot = None
    while line:
        commands = line.split(' ')
        if commands[0].strip() in COMMANDS:
            print line
        else:
            print "Unknown Command"
        line = func_to_execute()
