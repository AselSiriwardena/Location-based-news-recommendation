# from firebase import firebase
# print('Hello Nish')

import pyrebase
# public database
# config = {
#     "apiKey": "AIzaSyDsTRtMepuPzzlHIlwP5t-vYqelNJFQLf0",
#     "authDomain": "locationpython-3edc5.firebaseapp.com",
#     "databaseURL": "https://locationpython-3edc5.firebaseio.com",
#     "projectId": "locationpython-3edc5",
#     "storageBucket": "locationpython-3edc5.appspot.com",
#     "messagingSenderId": "335224995856"
#   }
#private database
config = {
    "apiKey": "AIzaSyD8oXsTwcGZK738DlKbdU2wfsyo-pKPD50",
    "authDomain": "myfirst-62243.firebaseapp.com",
    "databaseURL": "https://myfirst-62243.firebaseio.com",
    "projectId": "myfirst-62243",
    "storageBucket": "myfirst-62243.appspot.com",
    "messagingSenderId": "505364342015"
  }

firebase = pyrebase.initialize_app(config)

dados = firebase.database()
dados.child().update({"location": "Matara "})