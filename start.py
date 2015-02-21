import requests
import sys
import json
import const
import os

from server import *


def getTokenFromFile():
	d = {}
	with open("online.config") as f:
		for line in f:
			(key, val) = line.split(":")
			d[key] = val
		return d


def getServers():
	r = requests.get(const.api_base_url + "/servers", headers = const.headers)
	print r.url

	jsonArray = r.text

	jsonServers = json.loads(jsonArray)

	servers = {}

	for jsonServer in jsonServers["servers"]:
		server = as_server(jsonServer)
		servers[server.name] = server

	return servers

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))



def main():

	const.token = getTokenFromFile()['token'].replace('"', '')
	const.api_base_url = "https://api.cloud.online.net"
	
	const.headers = {"X-Auth-Token" : const.token, "Content-Type" : "application/json"}

	servers = getServers()

	# servers[servers.keys()[0]].powerOn()
	# servers["TestServer"].powerOn()

	# servers[servers.keys()[0]].powerOff()
	# servers["TestServer"].powerOff()

if __name__ == "__main__":
	main()
