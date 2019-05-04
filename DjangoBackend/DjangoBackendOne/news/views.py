from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse


# cred = credentials.Certificate("../DjangoBackendOne/news/newsapp-54f7c-firebase-adminsdk-wzja4-dc085fad0b.json")
# firebase_admin.initialize_app(cred)
db = firestore.client()
# Create your   views here.
jsonRecoNewsList=[]


@csrf_protect
def get_news_by_category(request):
    category= request.GET.get('category')
    print('category requested :',category)
    docs = db.collection(u'news').where(u'category', u'==', 'sports').get()

    categorizedNews= []

    for doc in docs:
        print(doc._data['title'])
        # obj= News(doc._data['title'],doc._data['description'],doc._data['summery'],doc._data['link'],doc._data['category'],doc._data['date_time'])
        # obj.add_locations(doc._data['locations'])
        data = {
            "title": doc._data['title'],
            "category": doc._data['category'],
            "description":doc._data['description'],
            "summary":doc._data['summary'],
            "link":doc._data['link'],
            "date_time":doc._data['date_time'],

        }
        categorizedNews.append(data)
        # categorizedNews.append(obj)
    return HttpResponse(categorizedNews)


def get_user_by_login(request):

     userId=request.GET.get('userId')
     print('Requested userId...',userId)

     location=request.GET.get('location')
     print('Requested User-Location...',location)

     return HttpResponse(jsonRecoNewsList)


def get_news_by_ratings(request):

    reco_userId=request.GET.get('userId')
    print('Requested recommendation...',reco_userId)

    reco_newsId=request.GET.get('newsId')
    print('Requested recommendation...',reco_newsId)

    reco_rating=request.GET.get('ratings')
    print('Requested recommendation...',reco_rating)

    row = [''+str(reco_userId)+'',''+ str(reco_newsId)+'',''+ str(reco_rating)+'']

    with open(r'..\DjangoBackendOne\news\ratings.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()

    return HttpResponse("Successfully updated ratings dataset..")








