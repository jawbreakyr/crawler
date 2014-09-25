from urllib import urlopen
from bs4 import BeautifulSoup
import requests 

# target site
SITE_URL = "https://www.google.com.ph/search?q=random+pictures&biw=1366&bih=635&source=lnms&tbm=isch&sa=X&ei=qociVKGQLeOJjALP7oFo&sqi=2&ved=0CAYQ_AUoAQ#tbm=isch&q=recursion&spell=1"


# set an empty string for temporary container
# CONTAINER = ""
#set and empty list to cantain the seeked url
# COLLECTIONS = []

# iterate thru the data and increment each data to the empty string var
# for word in urlopen(SITE_URL).readlines():
# 	CONTAINER += word
COLLECTIONS = []

r = requests.get(SITE_URL)

soup = BeautifulSoup(r.text)

for x in soup.find_all('img'):
	COLLECTIONS.append(x['src'])

# exit()
# set a marker to seek
# marker = CONTAINER.find("<a href")
# # set the start of the search
# ent_marker = CONTAINER.find('"', marker)
# # set the end of the search
# end_marker = CONTAINER.find('"', ent_marker + 1)

# # take the url
# url = CONTAINER[ent_marker + 1 : end_marker]
# # append the url to the empty list var
# COLLECTIONS.append(url)


# # open the file add write & read opt set as a variable write the 
# # data inside the COLLECTIONS and closes it as built in to with-as
with open("target.txt", "wr+") as target:
	target.write(str(COLLECTIONS))
