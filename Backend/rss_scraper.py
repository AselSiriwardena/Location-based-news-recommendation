import feedparser
import json
import geograpy

url = "http://www.adaderana.lk/rss.php"
url2 = "http://www.hirunews.lk/rss/english.xml"
url3 = "http://www.hirunews.lk/rss/english.xml"
# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed


feedF = feedparser.parse(url2)
feedF2 = feedparser.parse(url)
feedF3 = feedparser.parse(url3)

feedList=[]
feedContent=[]
placesInFeed=[[]]
i=0
while (i<len(feedF['entries'])):
    # print(feedF['entries'][i]['title'])
    feedList.append(feedF['entries'][i]['title'])
    feedContent.append(feedF['entries'][i]['summary'])
    print("feed"+str(i)+" : "+feedList[i])
    i=i+1

j=0
while (j<len(feedF2['entries'])):
    # print(feedF['entries'][i]['title'])
    feedList.append(feedF2['entries'][j]['title'])
    feedContent.append(feedF2['entries'][j]['summary'])
    print("feed"+str(i+j)+" : "+feedList[i+j])
    j=j+1


k=0
while (k<len(feedF3['entries'])):
    # print(feedF['entries'][i]['title'])
    feedList.append(feedF3['entries'][k]['title'])
    feedContent.append(feedF3['entries'][k]['summary'])
    print("feed"+str(i+j+k)+" : "+feedList[i+j+k])
    k=k+1

#
# places = geograpy.get_place_context(text=feedList[1])
# placesInFeed.append(places.places)
# print("places - %s" % [str(x) for x in placesInFeed])
j=0
while (j<len(feedList)):
    places = geograpy.get_place_context(text=feedContent[j])
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
            print(" Content : "+feedContent[l-1])
            # print("index:"+str(l))

        i=i+1
    l=l+1





# while (i<len(placesInFeed)):
#     print("places - %s" % [str(x) for x in placesInFeed[i]])
