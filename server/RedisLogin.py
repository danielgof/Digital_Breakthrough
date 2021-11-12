import redis

class RedisLogin:
	def __init__(self, host = "127.0.0.1", port = 6379, db = 0):
		self.host = host
		self.port = port
		self.db   = db

		self.hashName = "Users"

		self.client = redis.StrictRedis(host = host, port = port, db = db)
		

	def HashUser(self, userEmail):
		return (self.hashName + ":" + userEmail)
	
	
	def AddUser(self, userEmail, userData):
		self.client.hmset(self.HashUser(userEmail), userData)


	def GetUser(self, userEmail):
		if self.client.exists(self.HashUser(userEmail)) == 0:
			return None

		user = self.client.hgetall(self.HashUser(userEmail))
		res = {}
		for field in user:
			res.update({field.decode() : user[field].decode()})
		return res