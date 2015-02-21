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