"""
LOG ACTIONS

ARGS: USERNAME, DELETE?, DOWNLOAD?, UPLOAD?
RTRNS: NONE

DESC: This class logs the actions taken on storage and puts them 
in the cloud store database. 

"""
from fileinput import filename
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

class LogActions: 
    def __init__(self, username: str, delete: bool, download: bool, upload: bool, db_client, filename) -> None:
        self.username = username
        self.delete = delete
        self.download = download
        self.upload = upload
        self.db = db_client
        self.filename = filename
        self.action = None

    def determine_action(self):
        if self.delete == True :
            self.action = "Delete"
        
        elif self.upload == True :
            self.action = "Upload"
        
        else :
            self.action = "Download"
    
    def log_action(self):
        document = "Log_1"
        data = {
            "User" : self.username,
            "Action": self.action,
            "Object": self.filename,
            "Timestamp": "something"
        }
        self.db.collection("Storage Log").document({document}).set(data)
    
    def display_log(self):
        results = self.db.collection("Storage Log").get()
        print(results)
