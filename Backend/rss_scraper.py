import feedparser
import json
import geograpy

urlList = ["http://www.adaderana.lk/rss.php",
           "http://www.hirunews.lk/rss/english.xml",
           "http://www.gossiplankahotnews.com/feeds/posts/default/-/Hotnews",
           "https://www.news.lk/news?format=feed",
           #"https://srilankamirror.com/news?format=feed&type=rss",
           #"http://www.thesundayleader.lk/feed/",
           #"http://www.dinamina.lk/rss.xml",
           #"https://www.newsfirst.lk/feed/"
           ]

listItem = 0

while (listItem < len(urlList)):
    print("*** "+urlList[listItem]+" ***")
    feedF = feedparser.parse(urlList[listItem])
    feedList = []
    placesInFeed = []
    i = 0
    while (i < len(feedF['entries'])):
        feedList.append(feedF['entries'][i]['title'])
        print("feed " + str(i) + " : " + feedList[i])
        #print("description " + str(i) + " : " + feedF.entries[i].description)
        i = i + 1

    #
    places = geograpy.get_place_context(text=feedList[2])
    placesInFeed.append(places.places)
    print("places - %s" % [str(x) for x in placesInFeed])
    while (i < len(feedList)):
        places = geograpy.get_place_context(text=feedList[i])
        placesInFeed.append(places.places)

    listItem = listItem + 1





    # print("places - "+str(placesInFeed[i]))

# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
