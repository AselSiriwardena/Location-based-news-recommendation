import feedparser
import json
import geograpy

url = "http://www.adaderana.lk/rss.php"
# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed


feedF = feedparser.parse( url )
feedList=[]
placesInFeed=[[]]
i=0
while (i<len(feedF['entries'])):
    # print(feedF['entries'][i]['title'])
    feedList.append(feedF['entries'][i]['title'])
    print("feed"+str(i)+" : "+feedList[i])
    i=i+1

#
# places = geograpy.get_place_context(text=feedList[1])
# placesInFeed.append(places.places)
# print("places - %s" % [str(x) for x in placesInFeed])
j=0
while (j<len(feedList)):
    places = geograpy.get_place_context(text=feedList[j])
    placesInFeed.append(places.places)
    j=j+1


print("places - %s" % [str(x) for x in placesInFeed])
# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
