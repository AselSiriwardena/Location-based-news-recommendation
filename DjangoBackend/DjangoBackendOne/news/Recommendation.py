import csv
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Recommendation(object):


 def getRecommendation(self,userId):

  #userId=18;  # userId is comming from frontend when user logs into the account for not I added a ID as 18
  jsonRecoNewsList = []

  sns.set_style('dark')
  'exec(%matplotlib inline)'

  ratings_data = pd.read_csv(r"..\DjangoBackend\DjangoBackendOne\news\ratings.csv")

  print("Just edited..")
  news_names = pd.read_csv(r"..\DjangoBackend\DjangoBackendOne\news\News.csv")

  news_data = pd.merge(ratings_data, news_names, on='newsId')


  news_data.groupby('title')['rating'].mean().head()

  news_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()

  news_data.groupby('title')['rating'].count().sort_values(ascending=False).head()


  ratings_mean_count = pd.DataFrame(news_data.groupby('title')['rating'].mean())
  ratings_mean_count['rating_counts'] = pd.DataFrame(news_data.groupby('title')['rating'].count())
  ratings_mean_count.head()

  user_news_rating = news_data.pivot_table(index='userId', columns='title', values='rating')

  print("////////////////////////////////////////////////////////////////////////")

  ratings_data = pd.read_csv(r"..\DjangoBackendOne\news\ratings.csv")

  userIdData=ratings_data.query('userId == '+str(userId)+'')   # Fetching data according to the user ID
  userNewsId=userIdData[userIdData.columns[1]].tolist()    # Add movieId's to a list

  news_history=pd.read_csv(r"..\DjangoBackendOne\news\newsHistory.csv")  # Getting data from the movieHistory

  userHisIdData=news_history.query('userId == ' + str(userId) + '')
  userHisNewsId=userHisIdData[userHisIdData.columns[1]].tolist()    # Add movieId's taken from movie history to a list

  temp3= set(userNewsId) - set(userHisNewsId)  # Check the news which are not available in the news history
  newsYetToWatch=list(temp3)

  if(len(list(temp3)) ==0):

      print("All the rated movies already have been recommended...")
      exit()

  else:

   news_names = pd.read_csv(r"..\DjangoBackendOne\news\News.csv")  #Getting list of movie data

   news_namesx=news_names.query('newsId == ' + str(newsYetToWatch[0]) + '')
   news_namesxy=news_namesx[news_namesx.columns[1]].tolist()    # Add movieId's taken from movie history to a list

   # Recommendation of the similar movies

   forrest_gump_ratings = user_news_rating['' + news_namesxy[0] + '']

   news_like_forest_gump = user_news_rating.corrwith(forrest_gump_ratings)

   corr_forrest_gump = pd.DataFrame(news_like_forest_gump, columns=['Correlation'])
   corr_forrest_gump.dropna(inplace=True)

   corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)


   corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])


   print("SIMILAR NEWS........")

   # Please add the move movieYetToWatch[0] to the movie history list in hare

   similarNews=corr_forrest_gump[corr_forrest_gump ['rating_counts'] > 10].sort_values('Correlation', ascending=False).head()
   print(similarNews)

   similarNews=similarNews.reset_index()
   similarNews.columns=['title', 'Correlation', 'rating_counts']
   print(similarNews)

   newsToBeRecommended=similarNews[similarNews.columns[0]].tolist()
   print(newsToBeRecommended)   # Final result...

   for x in range(len(newsToBeRecommended)):

    wholeNewsData=news_names.loc[news_names['title'] ==''+str(newsToBeRecommended[x])+'']

    data={
        'newsId':wholeNewsData[wholeNewsData.columns[0]].tolist()[0],
        'title':wholeNewsData[wholeNewsData.columns[1]].tolist()[0],
        'category':wholeNewsData[wholeNewsData.columns[2]].tolist()[0],
        'summary':wholeNewsData[wholeNewsData.columns[3]].tolist()[0],
        'description':wholeNewsData[wholeNewsData.columns[4]].tolist()[0],
        'link':wholeNewsData[wholeNewsData.columns[5]].tolist()[0],
    }

    jsonRecoNewsList.append(data)

   print(jsonRecoNewsList)

   row = ['' + str(userId) +'','' + str(newsYetToWatch[0]) + '']

   with open(r'..\DjangoBackendOne\news\newsHistory.csv','a') as csvFile:
       writer = csv.writer(csvFile)
       writer.writerow(row)

   csvFile.close()

  print("////////////////////////////////////////////////////////////////////////")

  return jsonRecoNewsList


