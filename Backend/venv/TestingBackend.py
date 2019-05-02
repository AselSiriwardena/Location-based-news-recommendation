# Create your views here.
import feedparser

import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
import os
import csv
import threading, time
from geograpy.extraction import Extractor

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:/Users/Peshala/PycharmProjects/Location-based-news-reccomendation/DjangoBackend/DjangoBackendOne/news/newsapp-54f7c-firebase-adminsdk-wzja4-dc085fad0b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

jar = 'C:/Users/Peshala/PycharmProjects/Location-based-news-reccomendation/DjangoBackend/DjangoBackendOne/stanford-postagger-2018-10-16/stanford-postagger.jar'
model = 'C:/Users/Peshala/PycharmProjects/Location-based-news-reccomendation/DjangoBackend/DjangoBackendOne/stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path = "C:/Program Files/Java/jdk1.8.0_101/bin/java.exe"

os.environ['JAVAHOME'] = java_path
nltk.internals.config_java('C:/Program Files/Java/jdk1.8.0_101/bin/java.exe')
pos_tagger = StanfordPOSTagger(model, jar)
pos_tagger.java_options = '-mx4096m'

import pyrebase

config = {
    "apiKey": "AIzaSyBJumddViT3Y70F6vmEdP_1VMGXqEFaqgg",
    "authDomain": "newsapp-54f7c.firebaseapp.com",
    "databaseURL": "https://newsapp-54f7c.firebaseio.com",
    "projectId": "newsapp-54f7c",
    "storageBucket": "newsapp-54f7c.appspot.com",
    "messagingSenderId": "841850292385"
}

# firebase = pyrebase.initialize_app(config)

newsObjects = []
entityCount = 0

nouns = []
adj = []

sportKeyWords = []
polKeyWords = []
busKeyWords = []
eduKeyWords = []
healthKeyWords = []
entKeyWords = []


class News:
    # category = ''
    # title = ''
    # description = ''
    # locations = []
    # link = ''
    # summery = ''
    # date_time= ''

    def __init__(self, title, description, summery, link, category, date_time,id):
        self.category = category
        self.title = title
        self.description = description
        self.summery = summery
        self.link = link
        self.date_time = date_time
        self.news_id=id

    def print_test(self):
        print(self.title)

    def add_locations(self, locations):
        self.locations = locations


with open('C:/Users/Peshala/PycharmProjects/Location-based-news-reccomendation/DjangoBackend/DjangoBackendOne/news/ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

            # checks the data in dataset are strings or null values
            # check the row 0 : business keywords
            if row[0].isdigit() or row[0] == '':
                row[0]

            else:
                busKeyWords.append(row[0])

            # check the row 1 : sport keywords
            if row[1].isdigit() or row[1] == '':
                row[1]

            else:
                sportKeyWords.append(row[1])

            # check the row 2 : politics keywords
            if row[2].isdigit() or row[2] == '':
                row[2]

            else:
                polKeyWords.append(row[2])

            # check the row 3 : education keywords
            if row[3].isdigit() or row[3] == '':
                row[3]

            else:
                eduKeyWords.append(row[3])

            # check the row 4 : helth keywords
            if row[4].isdigit() or row[4] == '':
                row[4]

            else:
                healthKeyWords.append(row[4])

            # check the row 5 : entertainment keywords
            if row[5].isdigit() or row[5] == '':
                row[5]

            else:
                entKeyWords.append(row[5])

            # busKeyWords.append(row[0])
            # polKeyWords.append(row[2])

            line_count += 1
    print(f'Processed {line_count} lines.')


class Counter:
    counterName = None
    counterValue = None


def check_with_sport_data():
    global nouns
    sportCount = 0
    for n in nouns:
        for s in sportKeyWords:
            if n == s:
                sportCount += 1

    countObj = Counter()

    countObj.counterName = 'sports'
    countObj.counterValue = sportCount
    return countObj


def check_with_pol_data():
    global nouns
    polCount = 0
    for n in nouns:
        for s in polKeyWords:
            if n == s:
                polCount += 1

    countObj = Counter()

    countObj.counterName = 'political'
    countObj.counterValue = polCount
    return countObj


def check_with_bus_data():
    global nouns
    busCount = 0
    for n in nouns:
        for s in busKeyWords:
            if n == s:
                busCount += 1

    countObj = Counter()

    countObj.counterName = 'business'
    countObj.counterValue = busCount
    return countObj


def check_with_edu_data():
    global nouns
    eduCount = 0
    for n in nouns:
        for s in eduKeyWords:
            if n == s:
                eduCount += 1

    countObj = Counter()

    countObj.counterName = 'education'
    countObj.counterValue = eduCount
    return countObj


def check_with_ent_data():
    global nouns
    entCount = 0
    for n in nouns:
        for s in entKeyWords:
            if n == s:
                entCount += 1

    countObj = Counter()

    countObj.counterName = 'entertainment'
    countObj.counterValue = entCount
    return countObj


def check_with_health_data():
    global nouns
    helCount = 0
    for n in nouns:
        for s in healthKeyWords:
            if n == s:
                helCount += 1

    countObj = Counter()

    countObj.counterName = 'health'
    countObj.counterValue = helCount
    return countObj


counterObjArray = []
categoryName = ''


def classify_news(news):
    text = pos_tagger.tag(word_tokenize(news))
    print(text)

    global nouns
    global adj
    for i in text:
        if i[1][0] == "N":
            nouns += [i[0]]
        elif i[1][0] == "J":
            adj += [i[0]]

    # for i in nouns:
    #     print(i)

    global counterObjArray
    global categoryName
    counterObjArray.append(check_with_sport_data())
    counterObjArray.append(check_with_pol_data())
    counterObjArray.append(check_with_bus_data())
    counterObjArray.append(check_with_edu_data())
    counterObjArray.append(check_with_ent_data())
    counterObjArray.append(check_with_health_data())

    maxValue = counterObjArray[0].counterValue
    categoryName = counterObjArray[0].counterName

    for i in counterObjArray:

        if i.counterValue > maxValue:
            print('test counter details ', i.counterName, ' value ', i.counterValue)
            maxValue = i.counterValue
            categoryName = i.counterName

    print('nouns test1 ', nouns)
    nouns.clear()
    print('nouns test ', nouns)
    return categoryName

news_in_db=[]
def retrive_news_from_firebase():
    print('running retrive_news_from_firebase')
    global db
    docs = db.collection(u'news').get()


    try:
        for doc in docs:

            obj= News(doc._data['title'],doc._data['description'],doc._data['summary'],doc._data['link'],doc._data['category'],doc._data['date_time'],doc._data['news_id'])
            obj.add_locations(doc._data['locations'])
            news_in_db.append(obj)
        print(' retrive_news_from_firebase  complete')
    except:
        print('retrive_news_from_firebase() Error')
def is_news_already_exist_in_db(title):
    print('running is_news_already_exist_in_db')
    global news_in_db
    for news in news_in_db:
        if news.title== title:
            print('True')
            return True


#retrive the maximum news id and set it to entityCount
def set_entityCount():
    global news_in_db
    max_entityCount=news_in_db[0].news_id
    for news in news_in_db:
        if max_entityCount< news.news_id:
            max_entityCount=news.news_id
    global entityCount
    entityCount=max_entityCount
    print('current index',entityCount)


def collect_news():
    print('Running collecting news')
    retrive_news_from_firebase()

    url = ["http://www.adaderana.lk/rss.php",
           "http://www.hirunews.lk/rss/english.xml",
           "https://www.news.lk/news?format=feed",
           "https://srilankamirror.com/news?format=feed&type=rss",
           "http://www.thesundayleader.lk/feed/",
           "https://www.newsfirst.lk/feed/"
           ]
    for url in url:
        # print(url)

        # read the rss feeds from urls
        feedParsed = feedparser.parse(url)
        # print(feedParsed)
        # check whether the rss reading success or not
        if feedParsed.feed != {}:
            global news_in_db
            global entityCount
            for post in feedParsed.entries:

                if is_news_already_exist_in_db(post.title)!= True:

                    category = classify_news(post.title)

                    set_entityCount()
                    newsObj = News(post.title, post.description, post.summary, post.link, category, post.published,entityCount)
                    newsObjects.append(newsObj)

                    locations = Extractor(text=post.description)  # Extract location
                    locations.find_entities()
                    # print(locations.places)  # locations is an array

                    newsObj.add_locations(locations.places)

                    # data = {
                    #     "title": newsObj.title,
                    #     "id":entityCount,
                    #     "description": newsObj.description,
                    #     "summary": newsObj.summery,
                    #     "link": newsObj.link,
                    #     "category": newsObj.category,
                    #     "locations": newsObj.locations,
                    #     "date_time": newsObj.date_time
                    # }
                    # firebase.database().set(data)
                    global db

                    doc_ref = db.collection(u'news').document()
                    doc_ref.set({
                        u'title':newsObj.title,
                        u'news_id':newsObj.news_id,
                        u'description': newsObj.description,
                        u'summary': newsObj.summery,
                        u'link': newsObj.link,
                        u'category': newsObj.category,
                        u'locations': newsObj.locations,
                        u'date_time': newsObj.date_time

                    })

                    # db.collection(u'newsAppData').document(u'news').set(newsObj)
                    print("feed " + str(newsObj.news_id) + " : " + str(newsObj.title))
                    print('category: ', category, '. time ', newsObj.date_time, ' . locations:', newsObj.locations)
                    entityCount = entityCount + 1



        else:

            print('Connection failed with url :', url)
    WAIT_SECONDS = 100  # timer for thread
    print(time.ctime())
    news_in_db.clear()
    threading.Timer(WAIT_SECONDS, collect_news).start()


# thred1 = threading.Thread(target= collect_news)

# thred1.start()
if os.environ.get('RUN_MAIN', None) != 'true':
    default_app_config = 'mydjangoapp.apps.MydjangoappConfig'
    collect_news()
# collect_news()
#
# WAIT_SECONDS=1

# def run_thread():
#     print(time.ctime())
#     threading.Timer(WAIT_SECONDS, run_thread).start()
#
# run_thread()

# docs = db.collection(u'news').get()
#
# for doc in docs:
#     print('###################################################')
