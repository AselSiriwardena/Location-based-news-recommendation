import feedparser
import json
import genericpath
import geograpy
from firebase import firebase
from geograpy.extraction import Extractor

# connect to firebase
# firebase=firebase.FirebaseApplication('https://console.firebase.google.com/u/0/project/trendingnews-ed7d3/database/trendingnews-ed7d3/data')
# result=firebase.get('/user',None)
# print(result)
# data = {'title': entry.title, 'description': entry.description}
# sent = json.dumps(data)
# result = firebase.post("/newsSummary", sent)
#----------------------------------------------------------------------------------------------------------------------------------------------

# Read data from the RSS FEED
NewsFeed = feedparser.parse("http://www.hirunews.lk/rss/english.xml")
NewsFeed2 = feedparser.parse("http://www.hirunews.lk/rss/english.xml")
NewsFeed3 = feedparser.parse("http://www.hirunews.lk/rss/english.xml")

print('Number of RSS posts :', len(NewsFeed.entries))

num = len(NewsFeed.entries)  # Get the rage of the news feed

for x in range(num):
    entry = NewsFeed.entries[x]
    print(entry.title)
    print(entry.description)

    e6 = Extractor(text=entry.description)  # Extract location
    e6.find_entities()
    print(e6.places)  # E6 is an array

    print("      ")
    print("------------------------------------------------")
    print("       ")

locationName = input("Enter your location : ")

for y in range(num):

    entry = NewsFeed.entries[y]
    e6 = Extractor(text=entry.description)  # Extract location
    e6.find_entities()

    for x in e6.places:

        if locationName == x :
            print(entry.title)
            print(entry.description)


