import feedparser
import json
import geograpy

# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed
feedURL = ["https://www.newsfirst.lk/feed/",
           "http://www.adaderana.lk/rss.php",
           "http://www.hirunews.lk/rss/english.xml",
           "http://www.gossiplankahotnews.com/feeds/posts/default/-/Hotnews",
           "https://www.news.lk/news?format=feed",
           "https://srilankamirror.com/news?format=feed&type=rss",
           "http://www.thesundayleader.lk/feed/",
           "http://www.dinamina.lk/rss.xml",
           ]

feedTitle = []
feedContent = []
placesInFeed = [[]]
sourceCount = 0
entityCount = 0

while (sourceCount < len(feedURL)):
    print(feedURL[sourceCount])
    feedF = feedparser.parse(feedURL[sourceCount])

    for post in feedF.entries:
        # print(feedF['entries'][i]['title'])
        feedTitle.append(post.title)
        feedContent.append(post.summary)
        print("feed" + str(entityCount) + " : " + post.title)
        entityCount = entityCount+1
    sourceCount = sourceCount + 1
#
# places = geograpy.get_place_context(text=feedList[1])
# placesInFeed.append(places.places)
# print("places - %s" % [str(x) for x in placesInFeed])
j = 0
while (j < len(feedTitle)):
    places = geograpy.get_place_context(text=feedContent[j])
    placesInFeed.append(places.places)
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
