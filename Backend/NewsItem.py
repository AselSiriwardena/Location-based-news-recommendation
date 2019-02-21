class NewsItem:
    def __init__(self, title, content, link, img, date):
        self.title = title
        self.content = content
        self.link = link
        self.img = img
        self.PubDate = date

    def get_data(self):
        return self.title, self.content, self.link, self.img, self.date
