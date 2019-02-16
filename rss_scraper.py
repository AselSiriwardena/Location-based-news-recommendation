import feedparser
import json

url = "http://www.adaderana.lk/rss.php"
feedF = feedparser.parse( url )
print(feedF['entries'][0]['title'])