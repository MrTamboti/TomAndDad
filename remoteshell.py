#import utils
import argparse
import winrm
import os
from pypsrp.client import Client
from subprocess import Popen, PIPE
from pypsrp.shell import Process, SignalCode, WinRS
from pypsrp.wsman import WSMan

# arguments
# Set description with string
usage = "Send remote ps command"

# Initialise argument parser | need to discuss

parser = argparse.ArgumentParser(
    epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter
)

# host address argument
parser.add_argument("-r", help="host address", dest="r")

# username argument
parser.add_argument("-u", help="username", dest="u")

# password argument
parser.add_argument("-p", help="password", dest="p")

# command argument
parser.add_argument("-c", help= "ps command", dest="c")

# port arugemnt ( shouldnt be needed as you should be able to pop it into host address)
parser.add_argument("-t", help= "port", dest="t")

# command argument
parser.add_argument("-i", help= "input command to run on remote host", dest="i")

# script dest argument
parser.add_argument("-s", help= "input script file path", dest="s")

# parsing arguments into connect_args for use with paramiko ssh connection
connect_args = parser.parse_args()

kwargs = {
    "server"    : connect_args.r,
    "username"  : connect_args.u,
    "password"  : connect_args.p,
    "port"      : connect_args.t,
    "ssl"       : False,
    "auth"      : "basic",
    "encryption": "never",
}

# remote host credentials 
if connect_args.t :
    hostname = "connect_args.r:connect_args.t"
    print (hostname)
else :
    hostname = connect_args.r
username = connect_args.u
pword = connect_args.p

# this takes in the same kwargs as the WSMan object
with Client(**kwargs) as client:

    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("connect_args.i")
    if stderr or rc !=0:
        print (stderr, rc)
    if stdout:
        print (stdout)