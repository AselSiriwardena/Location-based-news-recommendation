import feedparser
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from Backend.stable_test.News import News

with open('data.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")
url = ["http://www.adaderana.lk/rss.php",
       "http://www.hirunews.lk/rss/english.xml",
       "https://www.news.lk/news?format=feed",
       "https://srilankamirror.com/news?format=feed&type=rss",
       "http://www.thesundayleader.lk/feed/",
       "https://www.newsfirst.lk/feed/"
       ]

newsObjects = []

entityCount = 0


def classify_news(text):

    blob = TextBlob(text, classifier=cl)
    # for s in blob.sentences:
    #     print(s)
    #     print(s.classify())

    return blob.classify()


for url in url:
    # print(url)

    # read the rss feeds from urls
    feedParsed = feedparser.parse(url)
    # print(feedParsed)
    # check whether the rss reading success or not
    if feedParsed.feed != {}:

        for post in feedParsed.entries:
            newsObj = News(post.title, post.description, post.summary, post.link, '', '')
            newsObjects.append(newsObj)

            print("feed " + str(entityCount) + " : " + str(newsObjects[entityCount].title))
            category=classify_news(post.description)
            print('category: ',category)
            entityCount = entityCount + 1

    else:

        print('Connection failed with url :', url)



