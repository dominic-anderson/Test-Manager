import args
import platform as pf
import runpy
import subprocess as sp
import sys

if __name__ == "__main__":

    # Originally for testing
    # if args.HELP:
    #     sys.exit()
    if pf.system() == "Windows": 
        print("Main function")
        runpy.run_path("scripts/windows/script_cmd_test.py", run_name="__main__")
        # runpy.run_path("scripts/windows/script_cmd_test.py")
        # result = sp.run(['node', 'scripts/javascript/workflow_main.js'])
        # print(result)