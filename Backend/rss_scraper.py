import feedparser
import json
import geograpy

# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed
url = ["http://www.adaderana.lk/rss.php",
       "http://www.hirunews.lk/rss/english.xml",
       "http://www.gossiplankahotnews.com/feeds/posts/default/-/Hotnews",
       "https://www.news.lk/news?format=feed",
       "https://srilankamirror.com/news?format=feed&type=rss",
       "http://www.thesundayleader.lk/feed/",
       "http://www.dinamina.lk/rss.xml",
       "https://www.newsfirst.lk/feed/",
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
for content in feedContent:

    if content!="":
        place = geograpy.get_place_context(text=content)
        placesInFeed.append(place.places)

    else:
        placesInFeed.append("null")

k=1
for place in placesInFeed:
    print("place " + str(k) + " - %s" % str(place))
    k = k + 1

print("############################################################################################################")
print("############################################################################################################")
print("############################################################################################################")

locationName = input("Enter your location : ")
l = 0
while l < len(feedTitle):
    entityCount = 0
    while entityCount < len(placesInFeed[l]):

        if placesInFeed[l][entityCount] == locationName:
            # print("test :" + str(placesInFeed[l][i]))
            print(" News : " + feedTitle[l - 1])
            print(" Content : " + feedContent[l - 1])
            # print("index:"+str(l))

        entityCount = entityCount + 1
    l = l + 1

# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
