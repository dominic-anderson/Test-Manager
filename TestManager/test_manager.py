import args
import platform as pf
import runpy
import subprocess as sp
import sys

args.WORKFLOW = "main"

if __name__ == "__main__":

    # Originally for testing
    if args._parsed.show_help:
        args.print_help()
        sys.exit()
    if args.WORKFLOW != "": 
        sp.run(['node', 'scripts/javascript/run_workflow.js', args.VERBOSE, args.WORKFLOW])