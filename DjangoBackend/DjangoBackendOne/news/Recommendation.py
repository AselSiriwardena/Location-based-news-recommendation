import csv
import pandas as pd
import seaborn as sns

class Recommendation(object):

    def similarMovie(self):

     sns.set_style('dark')
     'exec(%matplotlib inline)'



     ratings_data = pd.read_csv(r"C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\ratings.csv")


     movie_names = pd.read_csv(r"C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\movies.csv")


     movie_data = pd.merge(ratings_data, movie_names, on='movieId')
     print(movie_data.head())

     movie_data.groupby('title')['rating'].mean().head()

     movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head()

     movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head()

     ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
     ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
     ratings_mean_count.head()

     user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')


     print("////////////////////////////////////////////////////////////////////////")

     userId=10;
     movieYetToWatch=[]

     ratings_data = pd.read_csv(r"C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\ratings.csv")

     userIdData=ratings_data.query('userId == '+str(userId)+'')   # Fetching data according to the user ID
     userMovieId=userIdData[userIdData.columns[1]].tolist()    # Add movieId's to a list

     movie_history=pd.read_csv(r"C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\movieHistory.csv")  # Getting data from the movieHistory

     userHisIdData=movie_history.query('userId == '+str(userId)+'')
     userHisMovieId=userHisIdData[userHisIdData.columns[1]].tolist()    # Add movieId's taken from movie history to a list

     temp3=set(userMovieId)-set(userHisMovieId)      #Check whether the selected movie available in the movie history
     movieYetToWatch=list(temp3)

     movie_names = pd.read_csv(r"C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\movies.csv")  #Getting list of movie data

     movie_namesx=movie_names.query('movieId == '+str(movieYetToWatch[0])+'')
     movie_namesxy=movie_namesx[movie_namesx.columns[1]].tolist()    # Add movieId's taken from movie history to a list
     print(movie_namesxy)

     forrest_gump_ratings = user_movie_rating[''+movie_namesxy[0]+'']

     movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

     corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
     corr_forrest_gump.dropna(inplace=True)
     corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)

     corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])

     print("SIMILAR MOVIES........")


    # print(corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head())

     similarMovie = corr_forrest_gump[corr_forrest_gump['rating_counts'] > 50].sort_values('Correlation',ascending=False).head()

     similarMovie = similarMovie.reset_index()
     similarMovie.columns = ['title', 'Correlation', 'rating_counts']
     print(similarMovie)
     print(similarMovie['title'].tolist())    # Final result to be sent for the recommendation

     row = [''+str(userId)+'',''+str(movieYetToWatch[0])+'']

   # Add the movie which is used to find similar movies  to the movie history
     with open(r'C:\Users\M.B.C. Kadawatha\Videos\ml-latest-small\movieHistory.csv','a') as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(row)

      csvFile.close()





