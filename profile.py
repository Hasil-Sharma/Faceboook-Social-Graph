from selenium import webdriver
from pymongo import MongoClient

client = MongoClient()
db = client.facebookSocialGraph
collection = db.profilelinks

base_url = "https://www.facebook.com/"
def main():
	browser = webdriver.Chrome('./chromedriver')
	browser.get(base_url)
	a = raw_input("Press enter to start scraping: ")
	friends = browser.find_elements_by_class_name('_698')
	for friend in friends:
		element = friend.find_element_by_tag_name('a')
		url = element.get_attribute('href')
		username = getUsername(url)
		data = {'username' : username, 'url':url}
		inserted = collection.insert(data)
		print inserted
		print url,username

def getUsername(url):
	url = url.replace(base_url,"")
	username = url.split("?")[0]
	return username

if __name__ == '__main__':
	main()