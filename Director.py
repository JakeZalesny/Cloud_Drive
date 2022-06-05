"""
DIRECTOR

ARGS: NONE
RTRNS: NONE

DESCRIPTION: 
Initializes all the classes in the program and calls them in 
the order needed to run the program. 
"""

from DeleteFile import DeleteFile
from DownloadFile import DownloadFile
from InitializeFirestore import InitializeFirestore
from LogActions import LogActions
from UI import UI
from UploadFile import UploadFile
from CreateDirectories import CreateDirectories


class Director:
    def __init__(self) -> None:
        self.CREATE_FOLDERS = CreateDirectories()
        self.USERNAME = self.CREATE_FOLDERS.get_username()
        self.INITIALIZE_FIRESTORE = InitializeFirestore(self.USERNAME)
        self.TOKEN = self.INITIALIZE_FIRESTORE.get_token()
        #self.INITIALIZE_FIRESTORE.initialize_db()
        #self.DB_CLIENT = self.INITIALIZE_FIRESTORE.get_db_client()
        self.STORAGE_CLIENT = self.INITIALIZE_FIRESTORE.get_storage()
        self.UPLOAD_PATH = self.CREATE_FOLDERS.get_upload_path()
        self.UPLOADED_PATH = self.CREATE_FOLDERS.get_uploaded_path()
        self.DOWNLOAD_PATH = self.CREATE_FOLDERS.get_downloaded_path()
        self.UPlOAD_FILE = UploadFile(self.UPLOAD_PATH, self.STORAGE_CLIENT)
        self.DELETE_FILE = DeleteFile(self.STORAGE_CLIENT, self.TOKEN)
        self.DOWNLOAD_FILE = DownloadFile(self.DOWNLOAD_PATH, self.STORAGE_CLIENT)
        self.UI = UI()
    
    def direct(self) -> None:
        self.CREATE_FOLDERS.create_directories()
        self.UI.display_UI()
        choice = self.UI.get_choice()
        upload = False
        delete = False
        download = False
        filename = "No File"
        #log_action = LogActions(self.USERNAME, delete, download, upload, self.DB_CLIENT, filename)
        while choice != 5 :
            match choice :
                case 1 :
                    self.UPlOAD_FILE.set_filename()
                    self.UPlOAD_FILE.create_filepath()
                    self.UPlOAD_FILE.set_folder()
                    upload = self.UPlOAD_FILE.upload_file()
                    #log_action = LogActions(self.USERNAME, delete, download, upload, self.DB_CLIENT, self.UPlOAD_FILE.get_filename())
                    #log_action.determine_action()
                    #log_action.log_action()
                case 2 :
                    self.DELETE_FILE.get_delete_filename()
                    delete = self.DELETE_FILE.delete_file()
                    #log_action = LogActions(self.USERNAME, delete, download, upload, self.DB_CLIENT, self.DELETE_FILE.get_delete_filename())
                    #log_action.determine_action()
                    #log_action.log_action()
                
                case 3 : 
                    self.DOWNLOAD_FILE.get_download_filename()
                    download = self.DOWNLOAD_FILE.download_file()
                    #log_action = LogActions(self.USERNAME, delete, download, upload, self.DB_CLIENT, self.DOWNLOAD_FILE.get_download_filename())
                    #log_action.determine_action()
                    #log_action.log_action()
                
                case 4:
                    #log_action.display_log()
                    pass

                case 5:
                    quit()
            
            
            self.UI.display_UI()
            choice = self.UI.get_choice()