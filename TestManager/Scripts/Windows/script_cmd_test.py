import args
import platform as pf

# Originally for testing
print("Running Windows scripts")
if args.all_args.verbose:
    print(f"Version: {pf.system()} {pf.release()}")