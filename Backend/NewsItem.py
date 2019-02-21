class NewsItem:
    def __init__(self, title, content, link, img, date):
        self.title = title
        self.content = content
        self.link = link
        self.img = img
        self.PubDate = date

    def get_data_all(self):
        return self.title, self.content, self.link, self.img, self.date

    def get_data_for_tile(self):
        return self.title, self.img, self.date
