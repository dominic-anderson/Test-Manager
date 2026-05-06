import argparse
import sys

"""
Argument definitions for Test Manager.

Exports:
  HELP (bool)       - True if -h/--help was passed
  VERBOSE (bool)    - True if -v/--verbose was passed
  WORKFLOW (str)    - Value passed to -w/--workflow or empty string
"""

parser = argparse.ArgumentParser(prog="TestManager", add_help=False,
                                 description="Test Manager command line arguments")

# Custom help flag (module imports won't auto-exit; main script can check args.HELP)
parser.add_argument("-h", "--help", action="store_true", dest="show_help",
                    help="Show all valid arguments and ignore other arguments")

parser.add_argument("-v", "--verbose", action="store_true", dest="verbose",
                    help="Display extended information during execution")

parser.add_argument("-w", "--workflow", metavar="WORKFLOW", type=str, dest="workflow",
                    default="", help="Specify the workflow to run (e.g. 'build', 'test', 'deploy')")

_parsed = parser.parse_args()

# Module-level constants for compatibility with existing code
HELP = _parsed.show_help
VERBOSE = _parsed.verbose
WORKFLOW = _parsed.workflow

# If user wants help, provide the help text for external callers that check HELP
def print_help():
    """Print the argument help text (useful when `HELP` is True)."""
    parser.print_help(file=sys.stdout)


__all__ = ["HELP", "VERBOSE", "WORKFLOW", "print_help"]