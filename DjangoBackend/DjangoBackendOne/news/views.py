from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from news.Recommendation import Recommendation
from django.views.decorators.csrf import csrf_protect

import csv


# cred = credentials.Certificate("../DjangoBackendOne/news/newsapp-54f7c-firebase-adminsdk-wzja4-dc085fad0b.json")
# firebase_admin.initialize_app(cred)
db = firestore.client()
# Create your   views here.


def get_news_by_category(request):

    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    category = body_data['category']


    print('category requested :',category)
    docs = db.collection(u'news').where(u'category', u'==', 'sports').get()

    categorizedNews= []

    for doc in docs:
        print(doc._data['title'])
        data = {
            "title": doc._data['title'],
            "category": doc._data['category'],
            "description":doc._data['description'],
            "summary":doc._data['summary'],
            "link":doc._data['link'],
            "date_time":doc._data['date_time'],

        }
        categorizedNews.append(data)

    return HttpResponse(categorizedNews)


def get_user_by_login(request):

     body_unicode = request.body.decode('utf-8')
     body_data = json.loads(body_unicode)

     object1=Recommendation()

     userId = body_data['userId']
     print('Requested userId...',str(userId))

     # location=request.GET.get('location')

     jsonRecoNewsList=object1.getRecommendation(userId)

     location = body_data['location']

     print('Requested User-Location...',str(location))

     return HttpResponse(jsonRecoNewsList)



def get_news_by_ratings(request):

    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    reco_userId = body_data['userId']
    print('Requested recommendation...',str(reco_userId))

    reco_newsId = body_data['newsId']
    print('Requested recommendation...',str(reco_newsId))

    reco_rating = body_data['ratings']
    print('Requested recommendation...',str(reco_rating))

    row = [''+str(reco_userId)+'',''+ str(reco_newsId)+'',''+ str(reco_rating)+'']

    with open(r'..\DjangoBackendOne\news\ratings.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()

    return HttpResponse('Successfully updated ratings dataset')








