
class User:
	def __init__(self):
		self.data = {}


	def FromDB(self, user_id, rl):
		self.email = user_id
		self.data = rl.GetUser(user_id)
		return self

	def IsExists(self):
		return self.data != None


	def GetPassword(self):
		return self.data["password"]
		

	def is_authenticated(self):
		return True


	def is_active(self):
		return True


	def is_anonymous(self):
		return False


	def get_id(self):
		return str(self.email)


	def GetEmail(self):
		return self.email
	def GetName(self):
		return self.data["name"]
	def GetRegDate(self):
		return self.data["registration_date"]
	def GetLevel(self):
		return self.data["level"]

	def IsInspector(self):
		return self.data["level"] == "1"