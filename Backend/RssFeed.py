import feedparser
import json
import genericpath

import firebase_admin
import geograpy

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
from firebase_admin import credentials,firestore
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
print('Number of RSS posts :', len(NewsFeed.entries))
cred = credentials.Certificate("C:/Users/Peshala/PycharmProjects/Location-based-news-reccomendation/DjangoBackend/DjangoBackendOne/news/newsapp-54f7c-firebase-adminsdk-wzja4-dc085fad0b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
num = len(NewsFeed.entries)  # Get the rage of the news feed
class News:
    # category = ''
    # title = ''
    # description = ''
    # locations = []
    # link = ''
    # summery = ''
    # date_time= ''

    def __init__(self,title, description,summery,link,category,date_time):
        self.category = category
        self.title = title
        self.description = description
        self.summery = summery
        self.link = link
        self.date_time = date_time


    def print_test(self):
        print(self.title)

    def add_locations(self,locations):
        self.locations = locations
#
# for x in range(num):
#     entry = NewsFeed.entries[x]
#     print(entry.title)
#     print(entry.description)
#
#     e6 = Extractor(text=entry.description)  # Extract location
#     e6.find_entities()
#     print(e6.places)  # E6 is an array
#
#     print("      ")
#     print("------------------------------------------------")
#     print("       ")
#
# locationName = input("Enter your location : ")
#
# for y in range(num):
#
#     entry = NewsFeed.entries[y]
#     e6 = Extractor(text=entry.description)  # Extract location
#     e6.find_entities()
#
#     for x in e6.places:
#
#         if locationName == x :
#             print(entry.title)
#             print(entry.description)
#
#

news_in_db=[]
def retrive_news_from_firebase():
    print('running retrive_news_from_firebase')
    global db
    docs = db.collection(u'news').get()
    for doc in docs:

        obj= News(doc._data['title'],doc._data['description'],doc._data['summary'],doc._data['link'],doc._data['category'],doc._data['date_time'])
        obj.add_locations(doc._data['locations'])
        news_in_db.append(obj)
    print(' retrive_news_from_firebase  complete')
def is_news_already_exist_in_db(title):
    i=0
    print('running is_news_already_exist_in_db')
    for news in news_in_db:

        print(news.title)

retrive_news_from_firebase()
is_news_already_exist_in_db('kk')