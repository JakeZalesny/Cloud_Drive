"""
INITIALIZE FIRESTORE

ARGS: NONE
RTRNS: DB CLIENT

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

class InitializeFirestore:
    def __init__(self) -> None:
        self.db = None
    
    def initialize_db(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS "] = "clouddrive-351300-821f95007881.json"

        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            "project_id": "clouddrive-351300", 
        })
        db = firestore.client()
        self.db = db
    
    def get_db_cliet(self):
        return self.db