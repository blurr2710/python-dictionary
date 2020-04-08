class Dictionary:
	map=dict()
	def initialize(self):
		self.map={"apple":"a_fruit","asgard":"thorr native place","a":"a letter","amigo":"friends"}
	def meaning(self,word):
		 if word in self.map.keys():
		 	return self.map[word]
		 return "NOT FOUND"
