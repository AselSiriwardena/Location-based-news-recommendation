# from firebase import firebase
# print('Hello Nish')
import pyrebase
config = {
    "apiKey": "AIzaSyDsTRtMepuPzzlHIlwP5t-vYqelNJFQLf0",
    "authDomain": "locationpython-3edc5.firebaseapp.com",
    "databaseURL": "https://locationpython-3edc5.firebaseio.com",
    "projectId": "locationpython-3edc5",
    "storageBucket": "locationpython-3edc5.appspot.com",
    "messagingSenderId": "335224995856"
  }

firebase = pyrebase.initialize_app(config)

dados = firebase.database()
dados.child().update({"location": "Matara "})