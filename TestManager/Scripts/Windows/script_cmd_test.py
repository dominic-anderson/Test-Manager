import args
import platform as pf

# Originally for testing
print("Running Windows scripts")
if args.VERBOSE:
    print(f"Version: {pf.system()} {pf.release()}")