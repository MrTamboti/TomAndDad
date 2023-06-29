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

parser = argparse.ArgumentParser
	(
    		epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter
	)

# Set argument for CPU using boolean
parser.add_argument("-c","--cpu", help="Report on system CPU", action="store_true", dest="c")

# Set argument for Mem using boolean
parser.add_argument("-m","--mem", help="Report on system Memory", action="store_true", dest="m")

# Set argument for CPU and Mem using boolean
parser.add_argument("-a","--all", help="Report on system CPU and Memory", action="store_true", dest="a")

# parse inputs into args
args = parser.parse_args()

# need to ask about this, defining main part of script for execution?
def Main():


psutil.cpu_times(percpu=False)
psutil.virtual_memory()