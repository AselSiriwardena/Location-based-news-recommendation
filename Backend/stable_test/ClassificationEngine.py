from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
# train = [
#      ('Cricket', 'spt'),
#      ('Player', 'spt'),
#      ('Win', 'spt'),
#      ('parliament', 'neg'),
#      ('votes', 'neg'),
#      ("election", 'neg'),
#      ("won", "spt")
#  ]



with open('data_two.json', 'r') as fp:
     cl = NaiveBayesClassifier(fp, format="json")
# cl = NaiveBayesClassifier(train)
# cl.classify("I feel amazing!")

test='music is lovely entertainment '
blob = TextBlob(test, classifier=cl)
# for s in blob.sentences:
#
#     print(s)
#     print(s.classify())
print(blob.classify())
