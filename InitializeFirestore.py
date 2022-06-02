"""
INITIALIZE FIRESTORE

ARGS: NONE
RTRNS: DB CLIENT

DESCRIPTION: 
Initializest the firebase account and returns it making sure
that the other classes are able to use it.
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import os

class InitializeFirestore:
    def __init__(self) -> None:
        self.db = None
        self.storage = None
        self.config = {  
            "apiKey": "AIzaSyC4yyCVXLygEnxp1lQ29xbNxLSj9ziRulQ",
            "authDomain": "clouddrive-351300.firebaseapp.com",
            "projectId": "clouddrive-351300",
            "storageBucket": "clouddrive-351300.appspot.com",
            "messagingSenderId": "935060460328",
            "appId": "1:935060460328:web:7d4630993d4be23551361d",
            "measurementId": "G-R334D0KR8D",
            "databaseURL":"gs://clouddrive-351300.appspot.com"
            }
        self.firebase = pyrebase.initialize_app(self.config)

    def initialize_db(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS "] = "clouddrive-351300-38f1e56fcb9e.json"

        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            "project_id": "clouddrive-351300", 
        })
        db = firestore.client()
        self.db = db
    
    def get_db_client(self):
        return self.db
    
    def get_firebase(self):
        return self.firebase
    
    def get_storage(self):
        return self.firebase.storage()