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

k=0
while (k<len(feedList)):
    print("place "+str(k)+" - %s" % [str(x) for x in placesInFeed[k]])
    k=k+1


print("############################################################################################################")
print("############################################################################################################")
print("############################################################################################################")

locationName = input("Enter your location : ")
l=0
while (l<len(feedList)):
    i=0
    while (i < len(placesInFeed[l])):

        if placesInFeed[l][i] == locationName:
            # print("test :" + str(placesInFeed[l][i]))
            print(" News : "+feedList[l-1])
            # print("index:"+str(l))

        i=i+1
    l=l+1





# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
