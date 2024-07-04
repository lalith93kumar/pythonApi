from ..libs import PropertyReader

class createPetEndpoint:
 	def __init__(self,request_body=None):
 		self.reqbody = request_body

 	def method(self):
 		return "post" 

 	def body(self):
 		return self.reqbody

 	def pathparameter(self):
 		return None

 	def url(self):
 		url = PropertyReader.getInstance().data['url']+ "/v2/pet"
 		print(PropertyReader.getInstance().data)
 		return url

 	def header(self):
 		return PropertyReader.getInstance().data['header']

def getInstance(request_body=None):
	return createPetEndpoint(request_body);