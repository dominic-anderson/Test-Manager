import args
import platform as pf

# Originally for testing
print("Running Windows scripts")
if args.VERBOSE_MODE:
    print(f"Version: {pf.system()} {pf.release()}")