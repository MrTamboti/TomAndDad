#import utils
import argparse
import winrm
import os
from pypsrp.client import Client
from subprocess import Popen, PIPE

# arguments
# Set description with string
usage = "Report on Memory and/or CPU"

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

# parsing arguments into connect_args for use with paramiko ssh connection
connect_args = parser.parse_args()

# check if krb file exists
filename = ("/tmp/superkey")
if not os.path.exists(filename):
    print ("hell dog gone for walkies")

#set kerb paramaters
domain = "adh.local"
param = "%s@%s" % (connect_args.u, domain.upper())
ph = Popen(["kinit", "-c", filename, param], stdout=PIPE, stderr=PIPE, stdin=PIPE)

#handle password
password = connect_args.p

_stdout, _stderr = ph.communicate(bytes(password, "utf-8"), timeout=10)
rc = ph.returncode

if rc != 0:
    if _stderr:
        if type(_stderr) == bytes:
            _err = _stderr.decode("utf-8")
        else:
            _err = str(_stderr)
        print ("use logger next time %s" % _err)
    else:
        print ("use logger %s" % rc)
# remote host credentials 

os.environ ["KRB5CCNAME"] = filename

hostname = connect_args.r
username = "%s@ADH.LOCAL" % connect_args.u
pword = connect_args.p

# this takes in the same kwargs as the WSMan object
with Client(server=hostname, username=username, password=pword, ssl=False, auth="kerberos", encryption="never") as client:

    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("get-childitem")
    if stderr or rc !=0:
        print (stderr, rc)
    if stdout:
        print (stdout)