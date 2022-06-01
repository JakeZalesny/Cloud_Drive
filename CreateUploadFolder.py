

import os

class CreateUploadFolder: 
    def __init__(self) -> None:
        #self.db = db
        self._user_filepath = os.environ.get('USERNAME')
        self._desktop_filepath = r'/Users/{}/Desktop/'.format(self._user_filepath)
        self._full_path = r'{}/Cloud Storage'.format(self._desktop_filepath)
    
    def get_desktop_filepath(self):
        print(self._desktop_filepath)
    
    def create_directories(self):
        directory = os.listdir(self._desktop_filepath)
        if "Cloud Storage" not in directory:
            os.chdir(self._desktop_filepath)
            os.makedirs(f'{self._full_path}/Upload_Files')
            os.makedirs(f'{self._full_path}/Uploaded_Files')
    
