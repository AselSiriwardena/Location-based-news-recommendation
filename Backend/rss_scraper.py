import feedparser
import json
import geograpy

urlList = ["http://www.adaderana.lk/rss.php", "http://www.hirunews.lk/rss/english.xml", "http://fe1.virakesari.lk/feed"]
listItem = 0

while (listItem < len(urlList)):
    feedF = feedparser.parse(urlList[listItem])
    feedList = []
    placesInFeed = []
    i = 0
    while (i < len(feedF['entries'])):
        feedList.append(feedF['entries'][i]['title'])
        print("feed " + str(i) + " : " + feedList[i])
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
