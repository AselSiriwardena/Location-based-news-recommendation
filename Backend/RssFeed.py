import feedparser
import json
import genericpath
import geograpy
from firebase import firebase
from geograpy.extraction import Extractor

#connect to firebase
firebase=firebase.FirebaseApplication('https://console.firebase.google.com/u/0/project/trendingnews-ed7d3/database/trendingnews-ed7d3/data')
result=firebase.get('/user',None)
print(result)


#Read data from the RSS FEED
NewsFeed = feedparser.parse("http://www.hirunews.lk/rss/english.xml")
print ('Number of RSS posts :', len(NewsFeed.entries))

num=len(NewsFeed.entries)

for x in range(num):
    entry = NewsFeed.entries[x]
    print(entry.title)
    print(entry.description)
    e6 = Extractor(text=entry.description)
    e6.find_entities()

    print(e6.places)

   # data = {'title': entry.title, 'description': entry.description}
    #sent = json.dumps(data)
   # result = firebase.post("/newsSummary", sent)

    print("      ")
    print("------------------------------------------------")
    print("       ")























