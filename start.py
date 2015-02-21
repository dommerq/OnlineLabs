import requests
import sys
import json

import const
from server import *


def getTokenFromFile():
	d = {}
	with open("online.config") as f:
		for line in f:
			(key, val) = line.split(":")
			d[key] = val
		return d

def main():

	const.token = getTokenFromFile()['token'].replace('"', '')
	const.api_base_url = "https://api.cloud.online.net"
	
	headers = {"X-Auth-Token" : const.token, "Content-Type" : "application/json"}

	r = requests.get(const.api_base_url + "/servers", headers = headers)

	jsonArray = r.text

	jsonServers = json.loads(jsonArray)

	servers = {}

	for jsonServer in jsonServers["servers"]:
		server = as_server(jsonServer)
		servers[server.name] = server

	params = {'action': 'poweroff'}
	r = requests.post(const.api_base_url + "/servers/" + servers[servers.keys()[0]].id +  "/action", data = json.dumps(params), headers = headers)

	print r.text

if __name__ == "__main__":
	main()
