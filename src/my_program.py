#!/usr/bin/env python

import sys
from constant import (
    COMMAND_INPUT_PREFIX, COMMAND_OUTPUT_PREFIX,
    FILE_INPUT_PREFIX, FILE_OUTPUT_PREFIX,
    COMMANDS, STATUS_COMMAND, EXIT_COMMAND
)
from lib.commands import execute_command
from utils.command_map import COMMAND_MAP
from utils.command_generator import CommandGenerator


if __name__ == "__main__":
    command_generator = CommandGenerator()
    commands = command_generator.get_command()
    for command in commands:
        command_words = map(lambda x: x.strip(), command.split(' '))
        if command_words[0] in COMMAND_MAP:
            concrete_command = COMMAND_MAP[command_words[0]]()
            concrete_command.execute(command_words[1:])
        elif command_words[0] == EXIT_COMMAND:
            break
        else:
            concrete_command = COMMAND_MAP["UNKNOWN"]()
            concrete_command.execute()
