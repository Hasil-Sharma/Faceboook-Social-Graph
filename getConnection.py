import requests
from pymongo import MongoClient

client = MongoClient()
db = client.facebookSocialGraph
collection = db.profileData
post = db.friendConnection

def getSource():
	id = {}
	all_profiles = collection.find()
	for profile in all_profiles:
		print profile
		id[profile["id"]] = []
	return id

source = getSource()

def final(key,value):
	val = {}
	val['id'] = key
	val['friends'] = value[1]
	val_id = post.insert(val)
	print val_id

def mapfn(key,value):
	yield key,source.keys()

def reducefn(key,value):
	nodea = key
	nodes = value[0]
	friends = []
	token = 'CAACEdEose0cBAPpcRZAUNAZCtXXSxagyPOmbzR06ZAHzZCzwgZAcdkZCUCJNZC5V9EOk4eN755ZCPDNJFChdZCrKYtQwzewwzOCZALAI7RQfeFBWo4czKssxtStWQU5xXPpKnZAYqMCJukE5bSZBbWkITVBievyfcs2eYFoLfVNkpvPb2P3g4abZC9j4aEnUasfMstmhM9kBczII2iuIrWL87l2Ca'
	for node in nodes:
		base_url = 'https://graph.facebook.com/%s/friends/%s'%(nodea,node)
		response = requests.get(base_url,params={'access_token':token})
		if response.status_code == 200:
			if len(response.json()['data']) == 1:
				friends.append(node)
	return key,friends