"""
MAIN:

ARGS: NONE
RTRNS: NONE

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS "] = "clouddrive-351300-821f95007881.json"

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    "project_id": "clouddrive-351300", 
})

db = firestore.client()

def main(): 
    pass 

if __name__ == "__main__":
    main()