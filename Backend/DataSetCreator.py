import feedparser
from bs4 import BeautifulSoup
from nltk import word_tokenize


class DataSetGen:
    llog = feedparser.parse("http://www.adaderana.lk/rss.php")


    llog['feed']['title']

    len(llog.entries)

    post = llog.entries[2]
    post.title

    content = post.content[0].value
    content[:10]
    raw = BeautifulSoup(content).get_text()
    word_tokenize(raw)
