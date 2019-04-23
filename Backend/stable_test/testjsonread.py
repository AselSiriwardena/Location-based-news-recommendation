# import json
# from textblob import TextBlob
# from textblob.classifiers import NaiveBayesClassifier
#
# #
# # with open('data_two.json', 'r') as myfile:
# #     data=myfile.read()
# #
# # obj= json.loads(data)
#
#
# # datarray={}
# #
# # for i in obj:
# #
# #     print("usd: " + str(i['category']))
# #     datarray["text"]=i['headline']
# #     datarray["label"] = i['category']
# #     json.dumps(datarray, ensure_ascii=False)
# #     print(json.dumps(datarray, ensure_ascii=False))
# #
# # with open('data_three.json', 'w') as outfile:
# #     json.dump(datarray, outfile)
#
# with open('data_two.json', 'r') as fp:
#     cl = NaiveBayesClassifier(fp, format="json")
# # cl = NaiveBayesClassifier(train)
# # cl.classify("I feel amazing!")
#
# test = 'Players sign performance based World Cup contract run win badminton'
# blob = TextBlob(test, classifier=cl)
#
# print(blob.classify())
import nltk
from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
import os
import csv

# Add the jar and model via their path (instead of setting environment variables):
jar = '../stanford-postagger-2018-10-16/stanford-postagger.jar '
model = '../stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path ="C:/Program Files/Java/jdk1.8.0_101/bin/java.exe"

os.environ['JAVAHOME'] = java_path
nltk.internals.config_java('C:/Program Files/Java/jdk1.8.0_101/bin/java.exe')
pos_tagger = StanfordPOSTagger(model, jar)
text = pos_tagger.tag(word_tokenize("What's the airspeed of an unladen swallow army?"))
print(text)
# st = StanfordPOSTagger('english-bidirectional-distsim.tagger') # doctest: +SKIP
# st.tag('What is the airspeed of an unladen swallow ?'.split())  # doctest: +SKIP
nouns=[]
adj=[]
for i in text:
    if i[1][0] == "N":
        nouns += [i[0]]
    elif i[1][0] == "J":
        adj += [i[0]]

for i in nouns:
    print(i)

sportKeyWords=[]
polKeyWords=[]
busKeyWords=[]
eduKeyWords=[]
healthKeyWords=[]
entKeyWords=[]
with open('ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')

            #checks the data in dataset are strings or null values
            # check the row 0 : business keywords
            if row[0].isdigit() or row[0] == '':
                row[0]

            else:
                busKeyWords.append(row[0])

            #check the row 1 : sport keywords
            if row[1].isdigit() or row[1]== '':
                row[1]

            else:
                sportKeyWords.append(row[1])

            # check the row 2 : politics keywords
            if row[2].isdigit() or row[2] == '':
                row[2]

            else:
                polKeyWords.append(row[2])

            # check the row 3 : education keywords
            if row[3].isdigit() or row[3] == '':
                row[3]

            else:
                eduKeyWords.append(row[3])

            # check the row 4 : helth keywords
            if row[4].isdigit() or row[4] == '':
                row[4]

            else:
                healthKeyWords.append(row[4])

            # check the row 5 : entertainment keywords
            if row[5].isdigit() or row[5] == '':
                row[5]

            else:
                entKeyWords.append(row[5])




            # busKeyWords.append(row[0])
            # polKeyWords.append(row[2])

            line_count += 1
    print(f'Processed {line_count} lines.')

i=1
for x in sportKeyWords:
    print(str(i),x)
    i+=1

i=1
for x in entKeyWords:
    print(str(i),x)
    i+=1