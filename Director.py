"""
DIRECTOR

ARGS: NONE
RTRNS: NONE

DESCRIPTION: 
Initializes all the classes in the program and calls them in 
the order needed to run the program. 
"""

from InitializeFirestore import InitializeFirestore
from UploadFile import UploadFile


class Director:
    def __init__(self) -> None:
        self.INITIALIZE_FIRESTORE = InitializeFirestore()
        self.DB_CLIENT = self.INITIALIZE_FIRESTORE.get_db_client()
        self.UPlOAD_FILE = UploadFile(self.DB_CLIENT)
    
    def direct(self) -> None:
        pass