import string
import sys

# This file is for declaring all the command-line arguments that the program will use

"""
This function checks if any of the passed arguments match any of the provided arguments (case-insensitive)
Specifically for boolean arguments
Use another function if the argument you are setting is not a bool
"""
def _check_bool_arg(*args) -> bool:
    return any(arg.casefold() in [a.casefold() for a in sys.argv[1:]] for arg in args)

# Verbose mode: If enabled, the program will print more detailed information about what it is doing
_VERBOSE = "-v"
_VERBOSE_LONG = "--verbose"
_VERBOSE_DESC = "Display extended information during execution"
_VERBOSE_ENABLED_MESSAGE = "Verbose mode enabled"
VERBOSE_MODE = True if (_check_bool_arg(_VERBOSE, _VERBOSE_LONG)) else False

"""
Declare other arguments here
All arguments should be constants
Give each argument a description in a comment as well as in the README.md file
Try to include a short and long version of the argument (e.g. -v for --verbose) if possible
Try to include a message that will be printed when the argument is enabled or used where applicable (e.g. "Verbose mode enabled")
Declare your arguments using constants (e.g. _VERBOSE_MODE) and add them to the _VALID_ARGS list at the end of this file
"""

_HELP = "-h"
_HELP_LONG = "--help"
_HELP_DESC = "Show all valid arguments, ignores all other arguments"
_HELP_MESSAGE = "List of valid arguments:\n" + \
                f"{_HELP}, {_HELP_LONG}:    {_HELP_DESC}\n" + \
                f"{_VERBOSE}, {_VERBOSE_LONG}: {_VERBOSE_DESC}"
HELP = True if (_check_bool_arg(_HELP, _HELP_LONG)) else False

def _arg_check(arg_list):
    if any(arg in [_HELP, _HELP_LONG] for arg in sys.argv[1:]):
        print(_HELP_MESSAGE)
        if len(sys.argv) != 2:
            print("Other arguments ignored")
        return

    for arg in sys.argv[1:]:
        if arg.startswith("-") and arg not in arg_list:
            print(f"Warning: Unrecognized argument '{arg}'")
            continue

        if arg in arg_list:
            if arg == _VERBOSE or arg == _VERBOSE_LONG:
                print(_VERBOSE_ENABLED_MESSAGE)
                continue

_VALID_ARGS = [
    _HELP, _HELP_LONG,
    _VERBOSE, _VERBOSE_LONG
    ]

_arg_check(_VALID_ARGS)