import feedparser
import json

url = "http://www.adaderana.lk/rss.php"
# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed


feedF = feedparser.parse( url )
feedList=[]
i=0
while (i<len(feedF['entries'])):
    # print(feedF['entries'][i]['title'])
    feedList.append(feedF['entries'][i]['title'])
    print("feed"+str(i)+" : "+feedList[i])
    i=i+1



