import requests
import json
import logging
import sys

class HandlerFrame:

	logger = logging.getLogger()
	logger.setLevel(logging.INFO)

	@staticmethod
	def request_handler(obj):
		res = None
		if(obj.method()=='post'):
			HandlerFrame.logger.info("URL : "+obj.url())
			HandlerFrame.logger.info("DATA : "+json.dumps(obj.body()))
			HandlerFrame.logger.info("METHOD : POST")
			res = requests.post(url=obj.url(),data=json.dumps(obj.body()),headers=obj.header())
		if(obj.method()=='get'):
			HandlerFrame.logger.info("URL : "+obj.url())
			HandlerFrame.logger.info("METHOD : GET")
			res =  requests.get(url=obj.url(),headers=obj.header())
		if(obj.method()=='put'):
			HandlerFrame.logger.info("URL : "+obj.url())
			HandlerFrame.logger.info("DATA : "+json.dumps(obj.body()))
			HandlerFrame.logger.info("METHOD : PUT")
			res =  requests.get(url=obj.url(),data=json.dumps(obj.body()),headers=obj.header())
		HandlerFrame.logger.info("Response Body : "+str(res.json()))
		return res

def getInstance():
	return HandlerFrame;

