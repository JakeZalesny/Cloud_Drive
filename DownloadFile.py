"""
DOWNLOAD FILE

ARGS: DB CLIENT, STORAGE CLIENT
RTRNS: NONE

DESC: 
This class is what will be called when the user 
wants to download a file off of the storage.

"""
import os

class DownloadFile: 
    def __init__(self, download_path, storage_client) -> None:
        self.download_path = download_path
        self.storage = storage_client
        self.download_filename = None
    
    def get_download_filename(self):
        self.download_filename = str(input("What's the name of the file you would like to download? "))

    def download_file(self): 
        os.chdir(self.download_path)
        self.storage.child(self.download_filename).download(self.download_path, self.download_filename)
        return True