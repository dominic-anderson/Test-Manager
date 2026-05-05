import args
import platform as pf
import runpy
import sys

if __name__ == "__main__":

    # Originally for testing
    if args.HELP:
        sys.exit()
    elif pf.system() == "Windows": 
        print("Main function")
        runpy.run_path("scripts/windows/script_cmd_test.py")