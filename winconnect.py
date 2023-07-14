#import utils
import paramiko
import logging
import psutil
import argparse
import sys

# argparse usage string for script description
usage = "Connect to Remote host, requires Host address (-r) local username (-u) and password (-p)"

# argparse initialization
parser = argparse.ArgumentParser(
	epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter
)

# arguments 


#parser.add_argument("-d", "--debug-logging", help="Enable debug logging", action="store_true", dest="d")

# host address argument
parser.add_argument("-r", help="host address", dest="r")

# username argument
parser.add_argument("-u", help="username", dest="u")

# password argument
parser.add_argument("-p", help="password", dest="p")

# password argument
parser.add_argument("-c", help="remote command", dest="c")

# parsing arguments into connect_args for use with paramiko ssh connection
connect_args = parser.parse_args()

# logging setup
formatter = logging.Formatter("%(levelname)s : %(message)s")
logger = logging.Logger(__name__)
logger.level = logging.ERROR

# stdout setup
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logger.level)
stdout_handler.setFormatter(formatter)

# setup logging handler
logger.addHandler(stdout_handler)

# remote host credentials 

hostname = connect_args.r
username = connect_args.u
password = connect_args.p

#set command from argument
cmd = "cmd.exe /c %s" % connect_args.c
print (cmd)
# 
# define main
#host = paramiko.SSHClient()
#host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#host.connect(hostname=hostname, username=username, password=password)
def main():
	
    # connect to host
    print ("host %s :: user %s :: pass %s" % ( connect_args.r,connect_args.u,connect_args.p))
    host = paramiko.SSHClient()
    host.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
	    host.connect(hostname=hostname, username=username, password=password)
    except paramiko.AuthenticationException:
	    _error = (
		    "Connection to remote host %s : authentication failed. " 
	        % (hostname)
        )
	    logger.error(
		    "%s", _error
        )
	    return
    except Exception as e:
	    _error = "connection to remote host : %s" % e
	    logger.error(
		    "%s", _error
        )
	    return

    stdin, stdout, stderr = host.exec_command(cmd)
    err = ''.join(stderr.readlines())
    out = ''.join(stdout.readlines())
    final_output = str(out)+str(err)

    # clear arguments
    connect_args.h = ""
    connect_args.u = ""
    connect_args.l = ""

    print(final_output)

if __name__ == "__main__":
	main()


    #close host connection
    #host.close