from pymongo import MongoClient
import json
client = MongoClient()
db = client.facebookSocialGraph
profiles = db.profileData
connections = db.friendConnection
jsonfile = open("final.json","w")
def main():
	final = {}
	final['nodes'] = []
	for profile in profiles.find():
		val = {}
		val['name'] = profile['name']
		val['url'] = profile['image_url']
		final['nodes'].append(val)
	final['links'] = []
	all_connections = connections.find()
	for connection in all_connections:
		source = profiles.find_one({'id':connection["id"]})['index']
		for friends in connection['friends']:
			final['links'].append({
									"source":source,
									"target":profiles.find_one({'id': friends})['index']
								})

	jsonfile.write(json.dumps(final,jsonfile,indent =4))
	jsonfile.close()
if __name__ == '__main__':
	main()