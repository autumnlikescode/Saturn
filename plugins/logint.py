


from keyauth.keyauth import api
import os
import sys
import os.path
import platform
import hashlib
from time import sleep
from datetime import datetime

os.system('cls')
os.system('title Testing')

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest
keyauthapp = api(
	name = "autumn",
	ownerid = "vvgz0mGIka",
	secret = "48baf2c686749977d5ee9fb37e0e70c398c3e64107b65a37d686b09e468ea99d",
	version = "1.0",
	hash_to_check = getchecksum()
)

key = input('Enture your license: ')
keyauthapp.license(key)
print("\nUser data: ") 
print("Username: " + keyauthapp.user_data.username)
print("IP address: " + keyauthapp.user_data.ip)
print("Hardware-Id: " + keyauthapp.user_data.hwid)
print("Subcription: " + keyauthapp.user_data.subscription)
print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print(f"Current Session Validation Status: {keyauthapp.check()}")
print("Exiting in 10 secs....")
sleep(10)
exit(0)
