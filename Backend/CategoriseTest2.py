import numpy as np
from matplotlib import pyplot as plt
import seaborn
from sklearn.datasets import fetch_20newsgroups #import newsgroups dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB

news = fetch_20newsgroups()
# print(news.target_names)

x_train,x_test,y_train,y_test = train_test_split(news.data,news.target)
model = make_pipeline(TfidfVectorizer(),MultinomialNB())
#tfidf : text freq inverse document freq is used to assign some weight to each word...
#multinomial is a form of binomial distr.

model.fit(x_train,y_train)
prediction = model.predict(x_test)

#here is a fn that can predict in which news category a sentence will fall under if it contains certain key words
def predict_category(string,train = x_train, model = model):
	predict = model.predict([string])
	print(news.target_names[predict[0]])

print(x_test[0])
predict_category(x_test[0])
predict_category('Every religion has its own God')
predict_category('India and Pakistan situation may lead to war')
predict_category('Raina owns a Porsche car')
predict_category('Linux is better than Windows and MAC OS')
predict_category('US has two satellites')
predict_category('My house is for sale')


confusion_matrix = confusion_matrix(y_test,prediction)
print(confusion_matrix)

seaborn.heatmap(confusion_matrix.T,xticklabels = news.target_names,yticklabels = news.target_names,square = True,annot=True,fmt='d',cbar=True)
# seaborn attributes explained: first arg is confusion_matrix ; xticklabels and yticklabels is to name the rows n cols ;
# square gives individual box fr each cell ; annot is used to specify the confused nos ; fmt is to make str as int
# fmt shud be specified if annot is true ; cbar is the side color bar by default it is true only....
# print(categories.target)
plt.xlabel("true category")
plt.ylabel("predicted category")
plt.show()