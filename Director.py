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
from CreateUploadFolder import CreateUploadFolder


class Director:
    def __init__(self) -> None:
        self.INITIALIZE_FIRESTORE = InitializeFirestore()
        self.DB_CLIENT = self.INITIALIZE_FIRESTORE.get_db_client()
        self.STORAGE_CLIENT = self.INITIALIZE_FIRESTORE.get_storage()
        self.CREATE_FOLDERS = CreateUploadFolder()
        self.UPLOAD_PATH = self.CREATE_FOLDERS.get_upload_path()
        self.UPLOADED_PATH = self.CREATE_FOLDERS.get_uploaded_path()
        self.UPlOAD_FILE = UploadFile(self.DB_CLIENT, self.UPLOAD_PATH, self.STORAGE_CLIENT)
    
    def direct(self) -> None:
        self.CREATE_FOLDERS.create_directories()