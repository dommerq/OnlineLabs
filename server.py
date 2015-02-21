import requests
import sys
import json
import const
from publicip import *

def as_server(json):
	server = Server()
	server.__dict__.update(json)
	server.public_ip = as_public_ip(json["public_ip"])
	return server

class Server(object):
	dynamic_ip_required = True
	name = ""
	modification_date = ""
	state_detail = ""
	hostname = ""
	creation_date = ""
	public_ip = PublicIp()
	state = ""
	private_ip = ""
	id = ""

	def actions(self):
		r = requests.get(const.api_base_url + "/servers/" + self.id +  "/action", headers = const.headers)
		print json.loads(r.text)["actions"]
		return json.loads(r.text)["actions"]

	def action(self, action):
		if action not in self.actions():
			raise ServerError(action + " is not a possible action for this server [" + self.name + "]")
		print "Executing " + action + " on server [" + self.name + "] w/id [" + self.id + "]"
		params = {'action': action}
		r = requests.post(const.api_base_url + "/servers/" + self.id +  "/action", data = json.dumps(params), headers = const.headers)
		print r.url

	def powerOn(self):
		self.action("powerOn")

	def powerOn(self):
		self.action("terminate")

	def powerOff(self):
		self.action("powerOff")

	def powerOff(self):
		self.action("reboot")


class ServerError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return str(self.value)
