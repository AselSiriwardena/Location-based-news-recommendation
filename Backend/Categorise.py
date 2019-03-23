from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

# data = {}
# data['news'] = []
# f = open("/home/peshala/PycharmProjects/Test/News_Category_Dataset_v2.json", "r")
#
# for x in f:
#
#     # x.replace('"','\'')
#     # y = x+','
#     data['news'].append(x)
#
#
#
#
# # with open('/home/peshala/PycharmProjects/Test/Location-based-news-reccomendation/Backend/newsData.txt', 'w') as outfile:
# #     json.dump(data, outfile)
#
# # for x in data:
# #
# #     # print(data[x])
#
#
# config = json.loads(open('/home/peshala/PycharmProjects/Test/Location-based-news-reccomendation/Backend/newsData.txt').read())
#
# print(config['news'])


businessData=[]

f = open("/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/business/world-leaders-gather-to-face-uncertainty.txt", "r")
for x in f:
    businessData.append(x)

f2 = open("/home/peshala/PycharmProjects/Test/Datasets/news-articles-dataset-master/news/business/wal-mart-fights-back-at-accusers.txt", "r")
for x in f2:
    businessData.append(x)

for x in businessData:
    print(x)
