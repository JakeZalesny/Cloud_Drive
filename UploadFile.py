"""
UPLOAD FILE

ARGS: DB, the connection to the database is received 
RTRNS: NONE 

"""

class UploadFile: 
    def __init__(self, upload_path, storage) -> None:
        self.file_name = None
        self.upload_path = upload_path
        self.storage = storage
        self.filepath = None
        self.full_path_upload = None
        self.log_file = None
    
    def set_filename(self) -> str:
        valid_filename = False
        while valid_filename == False:
            self.file_name = str(input("What is the name of the file you're trying to upload?"))
            if "." not in self.file_name :
                print("ERROR: Please specify the filetype")
            
            else :
                valid_filename == True
                break
    
    def get_filename(self) -> str:
        return self.file_name
    
    def create_filepath(self):
        self.filepath = f"{self.upload_path}/{self.file_name}"

    def set_folder(self):
        folder = input("Would you like to specify a folder? (Yes/No)")
        if folder.title() == "Yes":
            folder_name = input("What would you like to name the folder? ")
            self.full_path_upload = f"{folder_name}/{self.file_name}"
        
        else :
            self.full_path_upload = self.file_name
        
        return self.full_path_upload
    
    def upload_file(self):
        self.storage.child(self.full_path_upload).put(self.filepath)
        return True
    
    def get_log_file_upload(self):
        self.log_file = self.storage.child(self.full_path_upload).get_url(None)
        return self.log_file
