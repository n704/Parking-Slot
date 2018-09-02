#!/usr/bin/env python

import sys
from constant import (
    COMMAND_INPUT_PREFIX, COMMAND_OUTPUT_PREFIX,
    FILE_INPUT_PREFIX, FILE_OUTPUT_PREFIX,
    COMMANDS, STATUS_COMMAND, EXIT_COMMAND
)
from lib.commands import execute_command

if __name__ == "__main__":
    is_command_line = False
    if len(sys.argv) == 2:
        is_command_line = True
    if is_command_line:
        file = open(sys.argv[1], 'r')
        func_to_execute = file.readline
    else:
        def func_to_execute():
            print "\n"
            return raw_input()
    line = func_to_execute()
    parking_lot = None
    while line:
        commands = line.split(' ')
        if commands[0].strip() in COMMANDS:
            parking_lot = execute_command(commands, parking_lot)
        elif commands[0].strip() == EXIT_COMMAND:
            break
        else:
            print "Unknown Command"
        line = func_to_execute()
