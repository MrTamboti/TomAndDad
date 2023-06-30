"""
Python script to report CPU and/or Mem

"""

# Import utils
import argparse
import sys
import psutil
import logging

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

# Set argument for Debug Logging using boolean, used to set logger level to debug
parser.add_argument("-d","--deb", help="enable debug level logging", action="store_true", dest="d")

# Set argument for Logging using boolean, used to enable logging
parser.add_argument("-l","--log", help="enable logging", action="store_true", dest="l")

# parse inputs into args
args = parser.parse_args()

"""
Setting logging settings
"""

# Set format of log (need to check what formats exists or what is std)
formatter = logging.Formatter('%(levelname)s: %(message)s')

# Set logging with default info logging unless argument D (debug) is called
logger = logging.Logger(__name__)
logger.level = logging.DEBUG if args.d else logging.INFO

# need the below explaining for streamhandler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logger.level)
stdout_handler.setFormatter(formatter)

# Get date and prepare as string for logging filename used later
from datetime import date
# Think I can pipe date.today () into formating but will ask
currentD = date.today()
formatD = currentD.strftime("%d%m%Y")

# Setup logging to file using date string (obtained earlier) in filename
# Not sure how yet but want to set if statement to change name to log or debug depending on argument used
log_file = ("/tmp/resource_l%s.log" % (formatD))
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logger.level)
file_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
if args.l:
    logger.addHandler(file_handler)

"""
Grabbing CPU and MEM details
"""
# defining main script function
def main():

    # Start of logging file
    logger.info("Log Start")
    logger.debug("Debug Enabled")

    # If log argument true, add cpu and mem state to log as info
    if args.l:
        logger.info("starting - cpu: %s,mem: %s" % (args.c,args.m))

    # try start for error 84 (if error, check line 84)
    # if statement to check if cpu arugment (args.c) is true
    try:
        if args.c:
                system_cpu = psutil.cpu_percent(interval=None, percpu=False)
                print("system_cpu: %s" % (system_cpu))
            
    except Exception as e1:
        _error = "Error 84 : %s" % e1
        logger.error(
            "ERROR ENCOUNTERED :: %s", _error
        )
    try:
        if args.m:
            system_memory = psutil.virtual_memory().total
            mbv = system_memory // 1000000
            print("system_memory: %sMB" % (mbv))
    except Exception as e3:
        _error = "Error 90 : %s" % e3
        logger.error(
            "ERROR ENCOUNTERED :: %s", _error
        )



if __name__ == "__main__":
    main()
