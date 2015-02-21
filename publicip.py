def as_public_ip(json):
	public_ip = PublicIp()
	if json is not None:
		public_ip.__dict__.update(json)
	return public_ip

class PublicIp(object):
	dynamic = True
	id = ""
	address = ""
