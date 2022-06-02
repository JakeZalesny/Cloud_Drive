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
    
    def log_action(self):
        if self.upload == True :
            data = {
                "User" : self.username,
                "Action": "Upload",
                "Object": self.filename,
                "Timestamp":firestore.SERVER_TIMESTAMP
            }

        elif self.download == True :
            pass
            
        elif self.delete == True :
            pass