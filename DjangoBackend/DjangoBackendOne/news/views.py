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


# @csrf_protect
def get_news_by_category(request):
    # category= request.POST.get('cname')
    # category = request.POST['cname']
    if request.method == "POST":

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        category= body_data['cname']
        print('category requested :',category)
        docs = db.collection(u'news').where(u'category', u'==', category).get()

        categorizedNews= []

        for doc in docs:

            data = {
                "title": doc._data['title'],
                "category": doc._data['category'],
                "description":doc._data['description'],
                "summary":doc._data['summary'],
                "link":doc._data['link'],
                "date_time":doc._data['date_time'],
                "image_link":doc._data['image_link']
            }
            categorizedNews.append(data)
            jsonobject = json.dumps(categorizedNews)
        return HttpResponse(jsonobject)
    else:

        return HttpResponseNotFound('<h1 style="color:red;font-size: 100px;">Page Not Found</h1>')



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




def get_all_news(request):
    # category= request.POST.get('cname')
    # category = request.POST['cname']
    if request.method == "GET":



        docs = db.collection(u'news').get()

        all_news= []

        for doc in docs:

            data = {
                "title": doc._data['title'],
                "category": doc._data['category'],
                "description":doc._data['description'],
                "summary":doc._data['summary'],
                "link":doc._data['link'],
                "date_time":doc._data['date_time'],
                "image_link":doc._data['image_link']
            }
            all_news.append(data)
            jsonobject = json.dumps(all_news)
        return HttpResponse(jsonobject)
    else:

        return HttpResponseNotFound('<h1 style="color:red;font-size: 100px;">Page Not Found</h1>')




def get_news_by_location(request):
    # category= request.POST.get('cname')
    # category = request.POST['cname']
    if request.method == "POST":

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        location= body_data['location']
        print('requested location :',location)
        docs = db.collection(u'news').get()

        all_news=[]

        try:
            for doc in docs:
                obj = News(doc._data['title'], doc._data['description'], doc._data['summary'], doc._data['link'],
                           doc._data['category'], doc._data['date_time'], doc._data['news_id'], doc._data['image_link'])
                obj.add_locations(doc._data['locations'])
                all_news.append(obj)

            print(' retrive_news_from_firebase  complete')
        except:
            print('retrive_news_from_firebase() Error')

        filtered_news=[]
        for news in all_news:
            for loc in news.locations:
                if location==loc:
                    filtered_news.append(news)

        news_in_json=[]

        for news in filtered_news:

            data = {
                "title": news.title,
                "category":news.category,
                "description":news.description,
                "summary":news.summary,
                "link":news.link,
                "date_time":news.date_time,
                "image_link":news.image
            }
            news_in_json.append(data)
            jsonobject = json.dumps(news_in_json)
        return HttpResponse(jsonobject)
    else:

        return HttpResponseNotFound('<h1 style="color:red;font-size: 100px;">Page Not Found</h1>')



