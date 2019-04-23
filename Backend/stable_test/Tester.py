import feedparser
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from Backend.stable_test.News import News
import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
import os
import csv

jar = '../stanford-postagger-2018-10-16/stanford-postagger.jar '
model = '../stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path ="C:/Program Files/Java/jdk1.8.0_101/bin/java.exe"

os.environ['JAVAHOME'] = java_path
nltk.internals.config_java('C:/Program Files/Java/jdk1.8.0_101/bin/java.exe')
pos_tagger = StanfordPOSTagger(model, jar)


url = ["http://www.adaderana.lk/rss.php",
       "http://www.hirunews.lk/rss/english.xml",
       "https://www.news.lk/news?format=feed",
       "https://srilankamirror.com/news?format=feed&type=rss",
       "http://www.thesundayleader.lk/feed/",
       "https://www.newsfirst.lk/feed/"
       ]
newsObjects = []
entityCount = 0

nouns = []
adj = []

sportKeyWords=[]
polKeyWords=[]
busKeyWords=[]
eduKeyWords=[]
healthKeyWords=[]
entKeyWords=[]
with open('ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

            #checks the data in dataset are strings or null values
            # check the row 0 : business keywords
            if row[0].isdigit() or row[0] == '':
                row[0]

            else:
                busKeyWords.append(row[0])

            #check the row 1 : sport keywords
            if row[1].isdigit() or row[1]== '':
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
    counterName=None
    counterValue=None

def check_with_sport_data():
    global nouns
    sportCount=0
    for n in nouns:
        for s in sportKeyWords:
            if n==s:
                sportCount+=1

    countObj=Counter()

    countObj.counterName='sports'
    countObj.counterValue=sportCount
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


counterObjArray=[]
categoryName=''
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

    maxValue=counterObjArray[0].counterValue
    categoryName = counterObjArray[0].counterName

    for i in counterObjArray:

        if i.counterValue > maxValue:

            print('test counter details ',i.counterName,' value ',i.counterValue)
            maxValue=i.counterValue
            categoryName=i.counterName

    print('nouns test1 ', nouns)
    nouns.clear()
    print('nouns test ',nouns)
    return categoryName

for url in url:
    # print(url)

    # read the rss feeds from urls
    feedParsed = feedparser.parse(url)
    # print(feedParsed)
    # check whether the rss reading success or not
    if feedParsed.feed != {}:

        for post in feedParsed.entries:
            newsObj = News(post.title, post.description, post.summary, post.link, '', '')
            newsObjects.append(newsObj)

            print("feed " + str(entityCount) + " : " + str(newsObjects[entityCount].title))
            category=classify_news(post.title)
            print('category: ',category)
            entityCount = entityCount + 1

    else:

        print('Connection failed with url :', url)



