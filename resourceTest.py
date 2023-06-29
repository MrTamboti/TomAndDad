"""
Python script to report CPU and/or Mem

"""

# Import utils
import argparse
import psutil


"""
Setting Arguments
"""
# Set description with string
usage = "Report on Memory and/or CPU"

# Initialise argument parser | need to discuss

parser = argparse.ArgumentParser(
    epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter
)

# Set argument for CPU using boolean
parser.add_argument("-c","--cpu", help="Report on system CPU", action="store_true", dest="c")

# Set argument for Mem using boolean
parser.add_argument("-m","--mem", help="Report on system Memory", action="store_true", dest="m")

# parse inputs into args
args = parser.parse_args()

# need to ask about this, defining main part of script for execution?
def main():
    print("starting - cpu: %s,mem: %s" % (args.c,args.m))
    if args.c:
        print("true")
        system_cpu = psutil.cpu_percent(interval=None, percpu=False)
        print("system_cpu: %s" % (system_cpu))
    if args.m:
        system_memory = psutil.virtual_memory().total
        print("system_memory: %s" % (system_memory))

if __name__ == "__main__":
    main()
