

import os

class CreateDirectories: 
    def __init__(self) -> None:
        #self.db = db
        self._username = os.environ.get('USERNAME')
        self._desktop_filepath = r'/Users/{}/Desktop/'.format(self._username)
        self._full_path = r'{}/Cloud Storage/'.format(self._desktop_filepath)
        self._upload_path = r'{}/Cloud Storage/Upload Files'.format(self._desktop_filepath)
        self._uploaded_path = r'{}/Cloud Storage/Uploaded Files'.format(self._desktop_filepath)
        self._download_path = r'{}/Cloud Storage/Downloaded Files'.format(self._desktop_filepath)
    

    
    def create_directories(self):
        directory = os.listdir(self._desktop_filepath)
        if "Cloud Storage" not in directory:
            os.chdir(self._desktop_filepath)
            os.makedirs(f'{self._upload_path}')
            os.makedirs(f'{self._uploaded_path}')
            os.makedirs(f'{self._download_path}')
    
    
    def get_upload_path(self):
        return self._upload_path

    
    def get_uploaded_path(self):
        return self._uploaded_path  

    def get_downloaded_path(self):
        return self._download_path  
