#!/usr/bin/python

import sys
from constant import (
    COMMAND_INPUT_PREFIX, COMMAND_OUTPUT_PREFIX,
    FILE_INPUT_PREFIX, FILE_OUTPUT_PREFIX,
    COMMANDS, STATUS_COMMAND
)
from lib.command_fetcher import getCommandMode

if __name__ == "__main__":
    args_len = len(sys.argv)
    command_mode = getCommandMode(args_len)
    for command in command_mode.getCommand():
        print command
