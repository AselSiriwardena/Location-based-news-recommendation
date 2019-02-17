import feedparser
import json

url = "http://www.adaderana.lk/rss.php"
# url = "http://www.hirunews.lk/rss/english.xml"
# url = "http://fe1.virakesari.lk/feed" #getting another language RSS feed


feedF = feedparser.parse( url )
i=0
while (i<len(feedF['entries'])):
    print(feedF['entries'][i]['title'])
    i=i+1

# for i in feedF['entries']._len_():
#     print(feedF['entries'][i]['title'])