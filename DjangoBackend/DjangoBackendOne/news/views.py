from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse


# cred = credentials.Certificate("../DjangoBackendOne/news/newsapp-54f7c-firebase-adminsdk-wzja4-dc085fad0b.json")
# firebase_admin.initialize_app(cred)
db = firestore.client()
# Create your   views here.


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



