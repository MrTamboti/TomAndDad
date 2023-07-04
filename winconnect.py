#import wmi
import paramiko
import logging
import psutil

# remote host credentials 

hostname = ""
username = ""
password = ""

# connect to host

host = paramiko.SSHClient()
host.set_missing_host_key_policy(paramiko.AutoAddPolicy())
it()
try:
	host.connect(hostname=hostname, username=username, password=password)
except Exception as connect_error:
	_error = "connection to remote host : %s" % connect_error
	logger.error(
		"%s", _error
    )

#close host connection
host.close