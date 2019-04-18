class News:
    category = ''
    title = ''
    description = ''
    location = ''
    link = ''
    summery = ''

    def __init__(self,title, description,summery,link, location,category):
        self.category = category
        self.title = title
        self.description = description
        self.summery = summery
        self.link = link
        self.location = location

    def print_test(self):
        print(self.title)
