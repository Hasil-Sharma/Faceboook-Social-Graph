from pymongo import MongoClient
import requests

client = MongoClient()
db = client.facebookSocialGraph
collection = db.profilelinks
post = db.profileData
base_url = "https://graph.facebook.com/"
token = 'CAACEdEose0cBAPpcRZAUNAZCtXXSxagyPOmbzR06ZAHzZCzwgZAcdkZCUCJNZC5V9EOk4eN755ZCPDNJFChdZCrKYtQwzewwzOCZALAI7RQfeFBWo4czKssxtStWQU5xXPpKnZAYqMCJukE5bSZBbWkITVBievyfcs2eYFoLfVNkpvPb2P3g4abZC9j4aEnUasfMstmhM9kBczII2iuIrWL87l2Ca'
index = 0

def insert(username):
	response = requests.get(base_url+username,params = {'access_token': token,'fields':'picture,name'})
	if response.status_code != 200:
		return
	response = response.json()
	val = {}
	val['image_url'] = response['picture']['data']['url']
	val['id'] = response['id']
	val['name'] = response['name']
	val['index'] = globals()['index']
	print val
	data = post.insert(val)
	print data
	globals()['index'] += 1

def main():
	count = 0
	all_profilelinks = collection.find()
	for profile in all_profilelinks:
		if count < 10:
			count += 1
			username = profile['username']
			insert(username)
	insert('me')

	
if __name__ == '__main__':
	main()