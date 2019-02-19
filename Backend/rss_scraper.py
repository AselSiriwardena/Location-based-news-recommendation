import feedparser
import json
import geograpy

# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed
#"http://www.thesundayleader.lk/feed/",
           #"http://www.dinamina.lk/rss.xml",
feedURL = ["http://www.adaderana.lk/rss.php",
           "http://www.hirunews.lk/rss/english.xml",
           "http://www.gossiplankahotnews.com/feeds/posts/default/-/Hotnews",
           "https://www.news.lk/news?format=feed",
           "https://srilankamirror.com/news?format=feed&type=rss",
           "https://www.newsfirst.lk/feed/"
           ]

feedTitle = []
feedContent = []
placesInFeed = [[]]
feedCount = 0



# feedF = feedparser.parse(feedURL[1])
# while (feedCount<len(feedF['entries'])):
#     print(feedURL[1])
#
#     feedTitle.append(feedF['entries'][feedCount]['title'])
#     feedContent.append(feedF['entries'][feedCount]['summary'])
#     print("feed" + str(feedCount) + " : " + feedTitle[feedCount])
#     #
#     # while (entityCount < len(feedF['entries'])):
#     #     # print(feedF['entries'][i]['title'])
#     #     feedTitle.append(feedF['entries'][entityCount]['title'])
#     #     feedContent.append(feedF['entries'][entityCount]['summary'])
#     #     print("feed" + str(entityCount) + " : " + feedTitle[entityCount])
#     #     entityCount = entityCount + 1
#     feedCount = feedCount+1
# #

feedList=[]
count1 = 0
countx = 0
while feedCount < len(feedURL):
    print(feedURL[feedCount])
    feedF = feedparser.parse(feedURL[feedCount])
    print("count1:" + str(count1))


    count1 = count1+len(feedF['entries'])

    entityCount = 0

    while entityCount < len(feedF['entries']):
        # print(feedF['entries'][i]['title'])
        feedTitle.append(feedF['entries'][entityCount]['title'])
        feedContent.append(feedF['entries'][entityCount]['summary'])
        print("feed" + str(countx) + " : " + feedTitle[countx])
        #print("feedConent:len: " + str(countx) + " " + feedContent[countx])
        entityCount = entityCount + 1
        countx=countx+1
        print("feedLen:" + str(len(feedF['entries'])))
        print("entitycount:" + str(entityCount))
    feedCount = feedCount+1
#
# places = geograpy.get_place_context(text=feedList[1])
# placesInFeed.append(places.places)
# print("places - %s" % [str(x) for x in placesInFeed])

print("feedTitleLen:" + str(len(feedTitle)))
print("feedConLen:" + str(len(feedContent)))
print("feedConent:" +feedContent[89])
j = 0
while (j < len(feedTitle)):
    print("feedConent:len: "+str(j)+" " + feedContent[j])
    if feedContent[j] != "":
        places = geograpy.get_place_context(text=feedContent[j])
        placesInFeed.append(places.places)
    else:
        placesInFeed.append("none")
    j = j + 1

k = 0
while (k < len(feedTitle)):
    print("place " + str(k) + " - %s" % [str(x) for x in placesInFeed[k]])
    k = k + 1

print("############################################################################################################")
print("############################################################################################################")
print("############################################################################################################")

locationName = input("Enter your location : ")
l = 0
while (l < len(feedTitle)):
    entityCount = 0
    while (entityCount < len(placesInFeed[l])):

        if placesInFeed[l][entityCount] == locationName:
            # print("test :" + str(placesInFeed[l][i]))
            print(" News : " + feedTitle[l - 1])
            print(" Content : " + feedContent[l - 1])
            # print("index:"+str(l))

        entityCount = entityCount + 1
    l = l + 1

# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
