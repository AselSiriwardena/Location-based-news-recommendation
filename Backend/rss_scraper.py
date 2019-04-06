import feedparser
import json
import geograpy
import nltk

nltk.download('stopwords')
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed
url = ["http://www.adaderana.lk/rss.php",
       "http://www.hirunews.lk/rss/english.xml",
       "https://www.news.lk/news?format=feed",
       "https://srilankamirror.com/news?format=feed&type=rss",
       "http://www.thesundayleader.lk/feed/",
       "https://www.newsfirst.lk/feed/"
       ]

feedTitle = []
feedContent = []
placesInFeed = [[]]
entityCount = 1

for url in url:
    print(url)
    feedParsed = feedparser.parse(url)

    for post in feedParsed.entries:
        feedTitle.append(post.title)
        feedContent.append(post.summary)
        print("feed " + str(entityCount) + " : " + post.title)
        entityCount = entityCount + 1

# places = geograpy.get_place_context(text=feedList[1])
# placesInFeed.append(places.places)
# print("places - %s" % [str(x) for x in placesInFeed])

print("Processing....")
for content in feedContent:

    if content != "":
        place = geograpy.get_place_context(text=content)
        placesInFeed.append(place.places)

    else:
        placesInFeed.append("null")

k = 1
for place in placesInFeed:
    print("place " + str(k) + " - %s" % str(place))
    k = k + 1

print("############################################################################################################")
print("############################################################################################################")
print("############################################################################################################")


#####
businessData=[]
politicalData=[]
entertainmentData=[]

def stop_words_remove(sentence):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            return w




businessDataFile = open("/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/businessdata.txt", "r")
for x in businessDataFile:
    businessData.append(stop_words_remove(x))

# f2 = open(
#     "/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/business/wal-mart-fights-back-at-accusers.txt",
#     "r")
# for x in f2:
#   businessData.append(stop_words_remove(stop_words_remove(x)))
#
# entertainmentDataFile = open("/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/politics/lib-dems-target-the-student-vote.txt", "r")
# for x in entertainmentDataFile:
#     entertainmentData.append(stop_words_remove(x))
#
# f4 = open(
#     "/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/politics/minimum-rate-for-foster-parents.txt",
#     "r")
# for x in f4:
#     politicalData.append(stop_words_remove(x))
# for x in businessData:
#     print(x)
######

repeat = 0


class News(object):
    pass


def categriser(l):

    bCount=0
    pCount=0
    eCount=0
    sCount=0
    tCount=0
    bAverage=0
    pAverage=0
    eAverage=0

    categoryPercentage=[]
    categoryName=[]

    for x in businessData:
        bCount = bCount + 1
        bAverage = bAverage + fuzz.partial_ratio(x, feedContent[l - 1])
    for x in politicalData:
        pCount = pCount + 1
        pAverage = pAverage + fuzz.partial_ratio(x, feedContent[l - 1])
    for x in entertainmentData:
        eCount = eCount + 1
        eAverage = eAverage + fuzz.partial_ratio(x, feedContent[l - 1])

    businessPercentage=bAverage/bCount
    politicalPercentage=pAverage/pCount
    entertainmentPercentage=eAverage/eCount

    categoryPercentage.append(businessPercentage)
    categoryPercentage.append(entertainmentPercentage)
    categoryPercentage.append(politicalPercentage)


    maxValue=categoryPercentage[0]
    print(maxValue)
    for

while True:

    locationName = input("Enter your location : ")
    l = 0
    while l < len(feedTitle):
        entityCount = 0
        while entityCount < len(placesInFeed[l]):

            if placesInFeed[l][entityCount] == locationName:
                # print("test :" + str(placesInFeed[l][i]))
                print(" News : " + feedTitle[l - 1])
                print(" Content : " + feedContent[l - 1])
                categriser(l)

                # print("index:"+str(l))
                ###
                # similarityB = 0
                # avCountB = 0
                # for x in businessData:
                #     avCountB = avCountB + 1
                #     similarityB = similarityB + fuzz.partial_ratio(x, feedContent[l - 1])

                # print('avcountB :' + str(avCountB) + ' similarityB :' + str(similarityB))
                # averageB = similarityB / avCountB
                #
                # print('average: ' + str(averageB))
                # ###
                #
                # similarityE = 0
                # avCountE = 0
                # for x in politicalData:
                #     avCountE = avCountE + 1
                #     similarityE = similarityE + fuzz.partial_ratio(x, feedContent[l - 1])
                #
                # print('avcountE :' + str(avCountE) + 'similarityE:' + str(similarityE))
                # averageE = similarityE / avCountE

                # print(x)
                #
                # print('averageE: ' + str(averageE))
                ####

                # if (averageB > averageE):
                #     News.category = 'Bussiness'
                #     print('Category :' + News.category)
                #
                # else:
                #     News.category = 'Political'
                #     print('Category :' + News.category)

            entityCount = entityCount + 1
        l = l + 1

    # repeat = input("Enter again : ")

# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])



